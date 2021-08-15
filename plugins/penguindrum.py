import http.server
import logging
import os
import threading
import typing
from typing import Optional

import msgpack
from PIL.Image import Image

import auto_derby
from auto_derby.single_mode import event, Context
from plugins.penguindrum_data import GENERATED_STORY_CHOICE_OPTIONS, _Option

LOGGER = logging.getLogger(__name__)


class _CharaInfo:
    def __init__(self, data):
        self._data = data

    def chara_id(self) -> int:
        return self._data['card_id'] // 100

    def turn(self) -> int:
        return self._data['turn']

    def shared_story_id(self, suffix: int, prefix: int = 50) -> int:
        return int('%2d%04d%03d' % (prefix, self.chara_id(), suffix))

    def used_vital(self) -> int:
        return self._data['max_vital'] - self._data['vital']

    def is_zekkouchou(self) -> bool:
        return self._data['motivation'] == 5

    def to_fake_context(self) -> Context:
        ctx = Context()

        ctx.speed, ctx.stamina, ctx.power, ctx.guts, ctx.wisdom = \
            self._data['speed'], self._data['stamina'], self._data['power'], self._data['guts'], self._data['wiz']

        turn = self.turn()
        ctx.date = (turn // 24, (turn % 24) // 2, turn % 1)

        ctx.vitality = 1

        return ctx


_Resolver = typing.Callable[[_CharaInfo, list[int]], int]


def _generic_resolve(chara_info: _CharaInfo, choice_ids: list[int], options: typing.Iterable[_Option]) -> int:
    if not chara_info.is_zekkouchou():
        for i, option in enumerate(options):
            if option.yaruki_up:
                return i + 1

    for i, option in enumerate(options):
        if 0 < option.vital <= chara_info.used_vital():
            return i + 1

    ctx = chara_info.to_fake_context()
    scores = [option.fake_training.score(ctx) for (i, option) in enumerate(options)]
    LOGGER.info("Fake training scores: %s", scores)
    return scores.index(max(scores)) + 1


def _make_choice_yaruki(zekkouchou_choice: int, else_choice: int) -> _Resolver:
    return lambda chara_info, choice_ids: zekkouchou_choice if chara_info.is_zekkouchou() else else_choice


SUMMER_CAMP_2ND_YEAR_RESOLVER: _Resolver = \
    lambda chara_info, choice_ids: _generic_resolve(chara_info, choice_ids, (_Option(power=10), _Option(guts=10)))

STORY_CHOICE_OPTIONS: dict[int, typing.Tuple[_Option, ...]] = GENERATED_STORY_CHOICE_OPTIONS.copy()

STORY_CHOICE_OPTIONS.update({
    # トレーナー並の知識
    400001025: (_Option(power=10), _Option(speed=10)),

    # 愉快ッ！　密着取材！
    400001027: (_Option(stamina=10), _Option(guts=10)),

    # 選んだ生き方
    809001001: (_Option(vital=14, yaruki_up=True), _Option(wiz=6, yaruki_up=True)),

    # キネマの思ひ出（お出かけ3）
    809001007: (_Option(vital=35, stamina=6, yaruki_up=True), _Option(stamina=12, guts=12, yaruki_up=True)),

    # トレーナー心得『指導は常に改良せよ』
    809004001: (_Option(vital=14, skill=18), _Option(speed=6, wiz=6)),
})

ALWAYS_CHOOSE_FIRST: _Resolver = lambda chara_info, choice_ids: 1
ALWAYS_CHOOSE_SECOND: _Resolver = lambda chara_info, choice_ids: 2
ALWAYS_CHOOSE_THIRD: _Resolver = lambda chara_info, choice_ids: 3

CHOOSE_FIRST_IF_1_ELSE_SECOND: _Resolver = lambda chara_info, choice_ids: 1 if choice_ids[0] == 1 else 2
CHOOSE_SECOND_IF_1_ELSE_FIRST: _Resolver = lambda chara_info, choice_ids: 2 if choice_ids[1] == 1 else 1

STORY_CHOICE_RESOLVERS: dict[int, _Resolver] = {
    # オグリの大食い選手権
    501006524: CHOOSE_FIRST_IF_1_ELSE_SECOND,

    # 宝塚記念の後に・キーワード②
    501007309: ALWAYS_CHOOSE_FIRST,
    501007310: ALWAYS_CHOOSE_FIRST,
    501007423: ALWAYS_CHOOSE_FIRST,
    501007424: ALWAYS_CHOOSE_FIRST,

    # ちょっと寄りたいステキな場所
    501007705: ALWAYS_CHOOSE_FIRST,

    # アイツの存在
    501009115: ALWAYS_CHOOSE_FIRST,
    501009413: ALWAYS_CHOOSE_FIRST,

    # 特急リドル便？
    501010524: CHOOSE_FIRST_IF_1_ELSE_SECOND,

    # バーガー・イン・ジャパン！
    501010525: CHOOSE_FIRST_IF_1_ELSE_SECOND,

    # レース場グルメの誘惑
    501013524: CHOOSE_FIRST_IF_1_ELSE_SECOND,

    # セイウンスカイ 晴天の攻防
    501020524: lambda chara_info, choice_ids: 2 if choice_ids[1] == 3 else 1 if choice_ids[0] == 1 else 3,

    # ちょっと寄り道！
    501052702: ALWAYS_CHOOSE_FIRST,

    # キングは疲れ知らずよ
    501061511: ALWAYS_CHOOSE_FIRST,

    # 勝者へ至るエチュード
    801015001: ALWAYS_CHOOSE_SECOND,

    # 08:36/朝寝坊、やばっ
    801040001: ALWAYS_CHOOSE_SECOND,

    # ワンダフル☆ミステイク！
    801044002: ALWAYS_CHOOSE_SECOND,

    # 温もり愛情弁当
    801051001: ALWAYS_CHOOSE_FIRST,

    # 付き合う権利をあげる！
    801061001: ALWAYS_CHOOSE_FIRST,

    # 太陽とエンカウント☆
    801065001: ALWAYS_CHOOSE_SECOND,

    # 思い込んだら一直線！
    801066001: ALWAYS_CHOOSE_SECOND,

    # あぁ、故郷
    801068002: ALWAYS_CHOOSE_SECOND,

    # 情熱のふたり
    809001004: ALWAYS_CHOOSE_FIRST,

    # 趣味を探して
    809004004: ALWAYS_CHOOSE_FIRST,

    # サイボーグではありません
    820009001: ALWAYS_CHOOSE_FIRST,

    # 私の、運勢……
    820017001: CHOOSE_SECOND_IF_1_ELSE_FIRST,

    # とっておきのお友だち？
    820023001: ALWAYS_CHOOSE_FIRST,

    # イタズラは計画的に
    820023002: ALWAYS_CHOOSE_FIRST,

    # 読書少女と魔法少女？
    820028001: ALWAYS_CHOOSE_FIRST,

    # ダシが重要！！
    830007002: ALWAYS_CHOOSE_FIRST,

    # ご利用は戦略的に☆
    830008001: ALWAYS_CHOOSE_FIRST,

    # 素敵な♪練習日和
    830010001: ALWAYS_CHOOSE_THIRD,

    # 常に心にステージを☆
    830017001: ALWAYS_CHOOSE_FIRST,

    # 怖くないもん！
    830026001: ALWAYS_CHOOSE_FIRST,

    # 捕まらないもん！
    830026002: ALWAYS_CHOOSE_FIRST,

    # ターボは強いんだもん！
    830026003: ALWAYS_CHOOSE_FIRST,

    # 情けは人のためならず
    830028002: _make_choice_yaruki(2, 1),

    # 求む、個性！
    830030001: _make_choice_yaruki(2, 1),

    # 思い出ほわほわ、わんこそば
    830031001: _make_choice_yaruki(2, 1),

    # 理の食VS暴の食
    830032002: ALWAYS_CHOOSE_FIRST,

    # 踏み出す、一歩
    830041001: CHOOSE_FIRST_IF_1_ELSE_SECOND,

    # チケゾー☆フレンドシップ！
    830046002: ALWAYS_CHOOSE_FIRST,

    # リアクションも1番！？
    830047001: ALWAYS_CHOOSE_FIRST,

    # ゴシップ狂想曲
    830058002: ALWAYS_CHOOSE_FIRST,

    # 『せんでん』始動！！
    830060001: ALWAYS_CHOOSE_FIRST,
}


class Plugin(auto_derby.Plugin):
    """Predict the future and make wise decisions."""

    def __init__(self):
        self._orig_get_choice = None
        self._last_response = None
        self._httpd = None
        self._server_thread = None
        self._17sai_flag = False  # Whether we just answered to 安心沢刺々美

    def install(self) -> None:
        self._orig_get_choice = event.get_choice
        event.get_choice = self.get_choice
        self.run_server()

    def run_server(self):
        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(_self):
                if _self.path == '/':
                    _self.send_response(200)
                    _self.end_headers()
                    _self.wfile.write('運命の果実を一緒に食べよう'.encode('utf-8'))
                    return
                _self.send_response(404)

            def do_POST(_self):
                if _self.path == '/notify/response':
                    content_len = int(_self.headers.get('Content-Length'))
                    self._last_response = _self.rfile.read(content_len)
                    _self.send_response(200)
                    _self.end_headers()
                    _self.wfile.write(b'OK')
                    return
                _self.send_response(404)

        address = ('127.0.0.1', int(os.getenv('PENGUINDRUM_SERVER_PORT', '2434')))

        self._httpd = http.server.HTTPServer(address, Handler)
        self._server_thread = threading.Thread(target=self._httpd.serve_forever)
        self._server_thread.setDaemon(True)
        self._server_thread.start()
        LOGGER.info("Server started at %s", address)

    def infer_choice(self, chara_info: _CharaInfo, story_id: int, choice_ids: list[int]) -> Optional[int]:
        LOGGER.info("Attempting to infer choice for story %d at turn %d, choice_ids %s",
                    story_id, chara_info.turn(), choice_ids)

        if (story_id == chara_info.shared_story_id(515)
                or story_id == chara_info.shared_story_id(802)):  # 愛嬌, 注目株, 練習上手 etc
            if choice_ids[0] == 2 and choice_ids[1] == 1:
                return 1
            if choice_ids[0] == 1 and choice_ids[1] == 2:
                return 2
            # Continue below

        if story_id in STORY_CHOICE_RESOLVERS:
            return STORY_CHOICE_RESOLVERS[story_id](chara_info, choice_ids)
        if story_id in STORY_CHOICE_OPTIONS:
            return _generic_resolve(chara_info, choice_ids, STORY_CHOICE_OPTIONS[story_id])

        if story_id == chara_info.shared_story_id(715):  # 追加の自主トレ
            return 2 if chara_info.used_vital() >= 5 else 1
        if story_id == chara_info.shared_story_id(101):  # 新年の抱負
            return 2 if chara_info.used_vital() >= 20 else 3
        if story_id == chara_info.shared_story_id(102):  # 初詣
            return 1 if chara_info.used_vital() >= 30 else 3
        if story_id == chara_info.shared_story_id(104):  # 夏合宿（2年目）にて
            return SUMMER_CAMP_2ND_YEAR_RESOLVER(chara_info, choice_ids)
        if (story_id == 400000043 or story_id == chara_info.shared_story_id(713)  # お大事に！
                or story_id == 400000044 or story_id == chara_info.shared_story_id(714)):  # 無茶は厳禁！
            return 2 if choice_ids[1] == 2 else 1
        if story_id == chara_info.shared_story_id(516):  # 太り気味
            return 2 if choice_ids[1] == 1 else 1
        if (story_id == chara_info.shared_story_id(708)  # レース勝利！
                or story_id in (501024724, 501040734, 501040738)
                or story_id == chara_info.shared_story_id(709)  # レース入着
                or story_id in (501040735, 501040739)
                or story_id == chara_info.shared_story_id(710)  # レース敗北
                or story_id in (501040736, 501040740)):
            return 2 if choice_ids[1] == 1 else 1
        if story_id == chara_info.shared_story_id(720):  # あんし〜ん笹針師、参☆上
            if self._17sai_flag:
                self._17sai_flag = False
                return 1
            self._17sai_flag = True
            if chara_info.turn() <= 24 and choice_ids[3] == 7:  # First year, 愛嬌
                return 4
            if choice_ids[1] == 3:  # Blue ball skills
                return 2
            if choice_ids[0] == 1:  # 5 size +20
                return 1
            if choice_ids[2] == 5:  # vital +40, max_vital +12
                return 3
            if choice_ids[3] == 7:  # 愛嬌 can +20 vital
                return 4
            return 5  # 帰れ
        if (story_id == chara_info.shared_story_id(711)  # 今度こそ負けない！
                or story_id in (501040737, 501040741)):
            return 2 if chara_info.is_zekkouchou() else 1
        if story_id == 400001024:  # 上々の面構えッ！
            return 2
        if story_id == 400000036:  # 乙名史記者の徹底取材
            return 1 if choice_ids[0] == 1 else 2
        return None

    def get_choice(self, event_screen: Image) -> int:
        if self._last_response is not None:
            try:
                response = msgpack.unpackb(self._last_response)
                chara_info = _CharaInfo(response['data']['chara_info'])
                unchecked_event_array = response['data']['unchecked_event_array']
                if len(unchecked_event_array) == 1:
                    event = unchecked_event_array[0]
                    story_id = event['story_id']
                    choice_ids = [choice['select_index'] for choice in event['event_contents_info']['choice_array']]
                    inferred_choice = self.infer_choice(chara_info, story_id, choice_ids)
                    if inferred_choice is not None:
                        LOGGER.info("Choosing %d", inferred_choice)
                        return inferred_choice
                    LOGGER.info("Do not have a preferred choice. Delegating to auto-derby.")
            except Exception as e:
                LOGGER.error(e)

        return self._orig_get_choice(event_screen)


auto_derby.plugin.register(__name__, Plugin())

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    plugin = Plugin()
    plugin.run_server()
