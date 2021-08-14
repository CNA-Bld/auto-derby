import http.server
import logging
import threading
import typing
from typing import Optional

import msgpack
from PIL.Image import Image

import auto_derby
from auto_derby.single_mode import event, Context, Training

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


def _fake_training(
        speed: int = 0, stamina: int = 0, power: int = 0, guts: int = 0, wiz: int = 0, skill: int = 0) -> Training:
    training = Training.new()
    training.speed, training.stamina, training.power, training.guts, training.wisdom, training.skill = \
        speed, stamina, power, guts, wiz, skill
    return training


_Resolver = typing.Callable[[_CharaInfo, list[int]], int]


def _make_choice_yaruki(zekkouchou_choice: int, else_choice: int) -> _Resolver:
    return lambda chara_info, choice_ids: zekkouchou_choice if chara_info.is_zekkouchou() else else_choice


def _make_choice_vital(used_threshold: int, low_choice: int, high_choice: int) -> _Resolver:
    return lambda chara_info, choice_ids: low_choice if chara_info.used_vital() >= used_threshold else high_choice


def _make_choice_fake_training(*options: Training) -> _Resolver:
    def resolve(chara_info: _CharaInfo, choice_ids: list[int]) -> int:
        ctx = chara_info.to_fake_context()
        scores = [option.score(ctx) for option in options]
        LOGGER.info("Fake training scores: %s", scores)
        return scores.index(max(scores)) + 1

    return resolve


SUMMER_CAMP_2ND_YEAR_RESOLVER = _make_choice_fake_training(_fake_training(power=10), _fake_training(guts=10))

STORY_CHOICE_RESOLVERS: dict[int, _Resolver] = {
    # ========== Support card events

    # スーパークリークSSR お手伝いもお任せ♪
    801045001: _make_choice_vital(15, 1, 2),

    # エイシンフラッシュSR 想定外のお昼
    801037001: _make_choice_vital(15, 1, 2),

    # キタサンブラックSSR あぁ、友情
    801068001: lambda chara_info, choice_ids: 2 if chara_info.is_zekkouchou() and chara_info.used_vital() >= 10 else 1,

    # マンハッタンカフェSR 夜の独走
    801025001: _make_choice_vital(10, 2, 1),

    # メジロドーベルSSR 踏み出す、一歩
    830041001: lambda chara_info, choice_ids: 1 if choice_ids[0] == 1 else 2,

    # キタサンブラックSSR 情けは人のためならず
    830028002: _make_choice_yaruki(2, 1),

    # シーキングザパールSR 言葉はノンノン♪　ボディで語るの！
    820029001: lambda chara_info, _: 1 if not chara_info.is_zekkouchou() else 3 if chara_info.used_vital() >= 30 else 2,

    # ダイワスカーレットSR このくらい平気なんだから！
    801009002: lambda chara_info, _: 1 if chara_info.is_zekkouchou() and chara_info.used_vital() < 20 else 2,

    # ========== Chara events

    # セイウンスカイ 晴天の攻防
    501020524: lambda chara_info, choice_ids: 2 if choice_ids[1] == 3 else 1 if choice_ids[0] == 1 else 3,

    # トウカイテイオー（新衣装） ボクとみんなとカップケーキ
    501003511: _make_choice_yaruki(2, 1),

    # トウカイテイオー カイチョーとダジャレ
    501003706: _make_choice_fake_training(_fake_training(stamina=5, power=5), _fake_training(speed=10)),

    # ========== Chara events 515/802

    # トウカイテイオー（新衣装） ネバー・ギブ・アップ・ワガハイ！
    501003802: _make_choice_fake_training(_fake_training(stamina=15, guts=5), _fake_training(power=5, wiz=15)),

    # ========== Chara events 506 (ダンスレッスン)

    # トウカイテイオー
    501003506: _make_choice_fake_training(_fake_training(stamina=10), _fake_training(power=10)),
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

        self._httpd = http.server.HTTPServer(('127.0.0.1', 2434), Handler)
        self._server_thread = threading.Thread(target=self._httpd.serve_forever)
        self._server_thread.setDaemon(True)
        self._server_thread.start()
        LOGGER.info("Server started")

    def infer_choice(self, chara_info: _CharaInfo, story_id: int, choice_ids: list[int]) -> Optional[int]:
        LOGGER.info("Attempting to infer choice for story %d at turn %d, choice_ids %s",
                    story_id, chara_info.turn(), choice_ids)

        if story_id in STORY_CHOICE_RESOLVERS:
            return STORY_CHOICE_RESOLVERS[story_id](chara_info, choice_ids)

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
        if (story_id == chara_info.shared_story_id(515)
                or story_id == chara_info.shared_story_id(802)):  # 愛嬌, 注目株, 練習上手 etc
            if choice_ids[0] == 2 and choice_ids[1] == 1:
                return 1
            if choice_ids[0] == 1 and choice_ids[1] == 2:
                return 2
            if story_id in STORY_CHOICE_RESOLVERS:
                return STORY_CHOICE_RESOLVERS[story_id](chara_info, choice_ids)
            return None
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
