import typing
from abc import abstractmethod, ABC

from auto_derby.single_mode import Training, Context


class _CharaInfo:
    def __init__(self, data):
        self._data = data
        self.fake_context = self._to_fake_context()

    def chara_id(self) -> int:
        return self._data['card_id'] // 100

    def turn(self) -> int:
        return self._data['turn']

    def shared_story_id(self, suffix: int, prefix: int = 50) -> int:
        return int('%2d%04d%03d' % (prefix, self.chara_id(), suffix))

    def remaining_vital(self) -> int:
        return self._data['vital']

    def used_vital(self) -> int:
        return self._data['max_vital'] - self.remaining_vital()

    def is_zekkouchou(self) -> bool:
        return self._data['motivation'] == 5

    def _to_fake_context(self) -> Context:
        ctx = Context.new()

        ctx.speed, ctx.stamina, ctx.power, ctx.guts, ctx.wisdom = \
            self._data['speed'], self._data['stamina'], self._data['power'], self._data['guts'], self._data['wiz']

        turn = self.turn()
        ctx.date = (turn // 24, (turn % 24) // 2, turn % 1)

        ctx.vitality = 1

        return ctx


class _BaseOption(ABC):
    @abstractmethod
    def get_option(self, choice_id):
        pass


class _Option(_BaseOption):
    def __init__(self,
                 speed: int = 0, stamina: int = 0, power: int = 0, guts: int = 0, wiz: int = 0, skill: int = 0,
                 yaruki_up: bool = False, vital: int = 0,
                 skill_hint: bool = False):
        self.speed, self.stamina, self.power, self.guts, self.wiz, self.skill = speed, stamina, power, guts, wiz, skill
        self.yaruki_up, self.vital = yaruki_up, vital
        self.fake_training = self._to_fake_training()

    def _to_fake_training(self) -> Training:
        training = Training.new()
        training.speed, training.stamina, training.power, training.guts, training.wisdom, training.skill = \
            self.speed, self.stamina, self.power, self.guts, self.wiz, self.skill
        return training

    def get_option(self, choice_id):
        return self

    def score(self, chara_info: _CharaInfo):
        ret = 0

        if self.yaruki_up and not chara_info.is_zekkouchou():
            ret += 1000

        vital_diff = 0
        if self.vital > 0:
            vital_diff = min(self.vital, chara_info.used_vital())
        elif self.vital < 0:
            vital_diff = -min(-self.vital, chara_info.remaining_vital())
        ret += vital_diff * 2

        ret += self.fake_training.score(chara_info.fake_context)

        return ret


GENERATED_STORY_CHOICE_OPTIONS: dict[int, typing.Tuple[_Option, ...]] = {
    # ダンスレッスン
    501001506: (_Option(guts=10), _Option(stamina=10)),

    # 青春のテニス日和
    501001510: (_Option(speed=10), _Option(stamina=10)),

    # カラオケグルメ♪
    501001511: (_Option(vital=10), _Option(power=10)),

    # ポーズはどうする？
    501001513: (_Option(power=20), _Option(skill=40)),

    # 想い、服に託して
    501001514: (_Option(stamina=20), _Option(guts=20)),

    # 今日も、明日からも
    501001515: (_Option(speed=20), _Option(wiz=20)),

    # 昼下がりの恩返し
    501001520: (_Option(vital=5, wiz=5), _Option(skill_hint=True)),

    # 特別だからこそ
    501001702: (_Option(stamina=10), _Option(speed=10)),

    # あなたと行きたい場所
    501001703: (_Option(wiz=10), _Option(stamina=10)),

    # 尊敬できる人だから
    501001704: (_Option(skill=30), _Option(stamina=5, guts=5), _Option(speed=5, power=5)),

    # もう少しだけ
    501001705: (_Option(skill_hint=True), _Option(skill_hint=True)),

    # 研究熱心
    501001706: (_Option(skill_hint=True), _Option(skill_hint=True)),

    # 炸裂、水着パワー！
    501001800: (_Option(speed=10, skill=15), _Option(wiz=20)),

    # ヘイカノジョ、遊びましょ♪
    501004511: (_Option(vital=10), _Option(vital=-5, power=5, guts=5)),

    # 夏、満喫大作戦！！
    501001801: (_Option(stamina=10, power=10), _Option(vital=10, speed=2, stamina=2, power=2, guts=2, wiz=2)),

    # もう1人のお母ちゃんへ
    501001802: (_Option(skill_hint=True), _Option(guts=20)),

    # ダンスレッスン
    501002506: (_Option(wiz=10), _Option(guts=10)),

    # スズカ流後輩指導？
    501002510: (_Option(speed=10), _Option(wiz=10)),

    # しっとりパーティータイム
    501002511: (_Option(vital=10), _Option(stamina=5, power=5)),

    # Landscape color
    501002513: (_Option(guts=20), _Option(power=20)),

    # 趣味、特技、休日の過ごし方
    501002514: (_Option(stamina=20), _Option(speed=10, wiz=10)),

    # ウマドル☆猛特訓！
    501002515: (_Option(speed=10, power=10), _Option(guts=10, wiz=10)),

    # 背を追ってくれるから
    501002520: (_Option(speed=5, skill=15), _Option(skill_hint=True)),

    # 私の小さな雪景色
    501002702: (_Option(stamina=10), _Option(wiz=10)),

    # あなたの喜ぶ景色
    501002703: (_Option(power=10), _Option(speed=5, guts=5)),

    # 私とあなたの、小さな雪景色
    501002704: (_Option(stamina=10), _Option(speed=10), _Option(power=10)),

    # 雨の日の過ごし方
    501002705: (_Option(guts=10), _Option(speed=5, wiz=5)),

    # ふたりの相性はいかに！？
    501002706: (_Option(power=5, guts=5), _Option(stamina=10)),

    # ダンスレッスン
    501003506: (_Option(stamina=10), _Option(power=10)),

    # "女帝"vs."帝王"
    501003510: (_Option(guts=10), _Option(skill=30)),

    # ボクとみんなとカップケーキ
    501003511: (_Option(vital=5, yaruki_up=True), _Option(speed=5, power=5)),

    # テイオーのジンクス
    501003513: (_Option(stamina=20), _Option(wiz=20)),

    # わがままテイオーと思い出の景色
    501003514: (_Option(guts=20), _Option(speed=10, power=10)),

    # カイチョーみたいな勝負服
    501003515: (_Option(speed=10, wiz=10), _Option(stamina=10, guts=10)),

    # テイオーの武者修行
    501003520: (_Option(guts=10, skill=15), _Option(skill_hint=True)),

    # カラオケでパワーアップ！？
    501003524: (_Option(guts=10), _Option(speed=10)),

    # テイオー、ウマドルになる！？
    501003525: (_Option(power=10), _Option(speed=10)),

    # 褒められちゃった！
    501003702: (_Option(stamina=10), _Option(speed=10)),

    # 叱られちゃった！
    501003703: (_Option(wiz=10), _Option(power=5, guts=5)),

    # 気づいちゃった！
    501003704: (_Option(speed=5, stamina=5), _Option(guts=5, wiz=5), _Option(power=10)),

    # ボクとマヤノとオトナの時間
    501003705: (_Option(guts=10), _Option(wiz=10)),

    # カイチョーとダジャレ
    501003706: (_Option(stamina=5, power=5), _Option(speed=10)),

    # 好敵手と書いて友と呼ぶ！
    501003800: (_Option(skill_hint=True), _Option(speed=10, skill=15)),

    # ワガハイがテイオー先輩だ！
    501003801: (_Option(skill_hint=True), _Option(wiz=10, skill=15)),

    # ネバー・ギブ・アップ・ワガハイ！
    501003802: (_Option(stamina=15, guts=5), _Option(power=5, wiz=15)),

    # ダンスレッスン
    501004506: (_Option(speed=10), _Option(wiz=10)),

    # スーパーカーでドライブ！
    501004510: (_Option(speed=10), _Option(wiz=10)),

    # 街のトレンドメーカー♪
    501004513: (_Option(speed=10, wiz=10), _Option(power=20)),

    # 家事テクだってお任せよ！
    501004514: (_Option(guts=20), _Option(stamina=10, power=10)),

    # マルゼンスキー、『好き』を語る
    501004515: (_Option(speed=20), _Option(stamina=10, guts=10)),

    # お姉さんの流儀☆
    501004520: (_Option(speed=5, skill=10, yaruki_up=True), _Option(skill_hint=True)),

    # レッツらお料理！
    501004524: (_Option(speed=10), _Option(guts=10)),

    # イケイケ必勝法！
    501004525: (_Option(stamina=10), _Option(wiz=10)),

    # ダンスにゾッコン！
    501004526: (_Option(speed=10), _Option(power=10)),

    # 支え合いの秘訣
    501004702: (_Option(speed=10), _Option(power=10)),

    # 頼れるお姉さんも、実は……
    501004703: (_Option(stamina=5, guts=5), _Option(speed=5, power=5)),

    # お任せハンドル
    501004704: (_Option(power=10), _Option(guts=10), _Option(wiz=10)),

    # 出会いはトレンディー☆
    501004705: (_Option(guts=10), _Option(wiz=10)),

    # お出かけ後のお楽しみ♪
    501004706: (_Option(speed=5, wiz=5), _Option(stamina=5, power=5)),

    # 憧れの『マルゼンさん』
    501004800: (_Option(speed=10, power=10), _Option(vital=15)),

    # ようこそ、バブリーランドへ
    501004801: (_Option(guts=20), _Option(wiz=20)),

    # マルゼンスキーの大切なもの
    501004802: (_Option(skill_hint=True), _Option(stamina=20)),

    # 第一幕　スマイル
    501005113: (_Option(guts=10), _Option(power=10)),

    # 第一幕　スマイル
    501005401: (_Option(guts=10), _Option(power=10)),

    # ダンスレッスン
    501005506: (_Option(speed=10), _Option(stamina=10)),

    # 秀麗なる門番
    501005510: (_Option(speed=10), _Option(power=10)),

    # ＠DREAM_MAKER
    501005511: (_Option(power=10), _Option(wiz=10)),

    # What a wonderful stage!
    501005513: (_Option(stamina=20), _Option(speed=10, power=10)),

    # my dear sister.
    501005514: (_Option(power=20), _Option(wiz=20)),

    # A Quiet Moment
    501005515: (_Option(guts=20), _Option(stamina=20)),

    # 2大スター競演
    501005520: (_Option(guts=10, skill=15), _Option(skill_hint=True)),

    # 愛した日々に悔いはない
    501005702: (_Option(wiz=10), _Option(power=10)),

    # 君のためだけ
    501005703: (_Option(guts=10), _Option(speed=10)),

    # 人生最大の幸運とは
    501005704: (_Option(stamina=10), _Option(power=10), _Option(speed=10)),

    # 舞台袖の一幕
    501005705: (_Option(guts=10), _Option(stamina=10)),

    # 星を見上げて
    501005706: (_Option(speed=10), _Option(power=10)),

    # ダンスレッスン
    501006506: (_Option(power=10), _Option(speed=10)),

    # 迷いウマ娘
    501006510: (_Option(guts=10), _Option(speed=10)),

    # 畑でビルドアップ
    501006511: (_Option(guts=10), _Option(power=10)),

    # 託された想い
    501006513: (_Option(stamina=10, power=10), _Option(wiz=20)),

    # オグリは森の案内ウマ娘？
    501006514: (_Option(speed=20), _Option(power=20)),

    # ぬいぐるみよりもずっと
    501006515: (_Option(guts=20), _Option(stamina=20)),

    # レースとグルメで満腹に
    501006520: (_Option(vital=10, skill=15), _Option(skill_hint=True)),

    # オグリ、決意する
    501006702: (_Option(speed=5, wiz=5), _Option(stamina=5, guts=5)),

    # オグリ、頑張る
    501006703: (_Option(guts=10), _Option(power=10)),

    # オグリ、成長する
    501006704: (_Option(wiz=10), _Option(stamina=10), _Option(power=10)),

    # 気になる隣の晩ご飯！
    501006705: (_Option(speed=10), _Option(guts=10)),

    # 高みのライバル
    501006706: (_Option(speed=5, stamina=5), _Option(power=5, wiz=5)),

    # ダンスレッスン
    501007506: (_Option(power=10), _Option(guts=10)),

    # ペア割常習犯
    501007510: (_Option(guts=10), _Option(stamina=10)),

    # 落としたものは？
    501007511: (_Option(vital=-10, power=20), _Option(speed=10)),

    # 主人公の赤！
    501007513: (_Option(wiz=20), _Option(guts=20)),

    # ゴルシ流デート
    501007514: (_Option(stamina=20), _Option(power=20)),

    # ゴルシの！いきなり過去編！
    501007515: (_Option(stamina=10, wiz=10), _Option(speed=20)),

    # えっアタシのバイト…やばすぎ？
    501007520: (_Option(stamina=10, skill=15), _Option(skill_hint=True)),

    # 翌日揃ってしわがれ声
    501007524: (_Option(stamina=10), _Option(guts=10)),

    # 左にホクロはないらしい
    501007702: (_Option(stamina=10), _Option(speed=10)),

    # 約15億年前からコンニチハ
    501007703: (_Option(guts=10), _Option(wiz=10)),

    # そして、少女は
    501007704: (_Option(speed=10), _Option(guts=10), _Option(power=10)),

    # 夜の公園で遊ぼう
    501007706: (_Option(guts=10), _Option(speed=10)),

    # ダンスレッスン
    501008506: (_Option(guts=10), _Option(stamina=10)),

    # たまにはガキの頃みたく
    501008510: (_Option(speed=10), _Option(power=10)),

    # 挑め、”宿命”
    501008511: (_Option(stamina=10), _Option(speed=10)),

    # 憧れヴィンテージ
    501008513: (_Option(power=20), _Option(stamina=20)),

    # クール・アンド・ヒート
    501008515: (_Option(speed=20), _Option(speed=10, power=10)),

    # 河川敷でガチバトル！
    501008520: (_Option(wiz=10, skill=15), _Option(skill_hint=True)),

    # カッコ良さの基準
    501008702: (_Option(wiz=10), _Option(guts=10)),

    # 響け、熱いサウンド！
    501008703: (_Option(speed=10), _Option(stamina=10)),

    # 共に極めよ、カッコ良さの道
    501008704: (_Option(power=10), _Option(speed=10), _Option(stamina=5, guts=5)),

    # “寄り道”しようぜ
    501008705: (_Option(speed=10), _Option(vital=5, yaruki_up=True)),

    # ダンスレッスン
    501009506: (_Option(guts=10), _Option(speed=10)),

    # おススメのお店
    501009510: (_Option(speed=5, power=5), _Option(guts=5, yaruki_up=True)),

    # 先輩のアドバイス
    501009511: (_Option(speed=10), _Option(power=10)),

    # 最高のポーズ
    501009513: (_Option(stamina=10, power=10), _Option(wiz=20)),

    # あの服が似合う自分
    501009514: (_Option(speed=20), _Option(guts=20)),

    # ついつい着たくなる！
    501009515: (_Option(stamina=10, wiz=10), _Option(speed=10, guts=10)),

    # 楽しめ！一番！
    501009520: (_Option(stamina=10, skill=15), _Option(skill_hint=True)),

    # 優等生としては……
    501009702: (_Option(wiz=10), _Option(skill=30)),

    # もうちょっとだけ
    501009703: (_Option(skill=30), _Option(power=10)),

    # 一番星の下で
    501009704: (_Option(skill=30), _Option(speed=5, stamina=5), _Option(power=10)),

    # 雨に降られて
    501009705: (_Option(guts=10), _Option(wiz=10)),

    # 休日の過ごし方
    501009706: (_Option(vital=10), _Option(yaruki_up=True, wiz=5)),

    # ダンスレッスン
    501010506: (_Option(power=10), _Option(speed=10)),

    # ハイド・アンド・シーク！
    501010510: (_Option(speed=10), _Option(stamina=10)),

    # シャル・ウィー・ハグ？
    501010511: (_Option(power=10), _Option(vital=10)),

    # ハヤウチ・バトル！
    501010513: (_Option(vital=10, speed=10), _Option(vital=10, wiz=10)),

    # 負けられない戦いが、あるのデス
    501010514: (_Option(wiz=20), _Option(stamina=20)),

    # TO THE NO.1！
    501010515: (_Option(power=10, guts=10), _Option(speed=10, wiz=10)),

    # 収穫フェスティバル！
    501010520: (_Option(power=10, skill=15), _Option(skill_hint=True)),

    # レイニー・パワフル！
    501010702: (_Option(power=10), _Option(skill=30)),

    # レイニー・チョイス！
    501010703: (_Option(speed=5, guts=5), _Option(stamina=5, wiz=5)),

    # レイニー・ピックアップ！
    501010704: (_Option(skill=30), _Option(power=5, wiz=5), _Option(speed=5, guts=5)),

    # レッツ・ミマワリ！
    501010705: (_Option(power=10), _Option(vital=10)),

    # 一緒に帰るデース！
    501010706: (_Option(yaruki_up=True, speed=5), _Option(yaruki_up=True, stamina=5)),

    # ダンスレッスン
    501011506: (_Option(power=10), _Option(guts=10)),

    # おつかいは人のためならず
    501011510: (_Option(speed=5, stamina=5), _Option(vital=5, wiz=5)),

    # ケッコウなオテマエデ！
    501011511: (_Option(wiz=5, skill=15), _Option(speed=10)),

    # 秘められた意味
    501011513: (_Option(stamina=10, guts=10), _Option(power=20)),

    # 譲れないこと
    501011514: (_Option(speed=20), _Option(stamina=20)),

    # でも負けるのは嫌
    501011515: (_Option(wiz=20), _Option(stamina=10, guts=10)),

    # トレセン学園百人一首クイーン決定戦
    501011520: (_Option(speed=10, wiz=5), _Option(skill_hint=True)),

    # 涼夏を求めて
    501011524: (_Option(guts=25), _Option(wiz=25)),

    # 大和撫子・ウマ娘？
    501011702: (_Option(power=5, wiz=5), _Option(speed=10)),

    # ふたつの原風景
    501011703: (_Option(guts=10), _Option(stamina=10)),

    # ナデシコ・ガール
    501011704: (_Option(power=10), _Option(wiz=10), _Option(speed=10)),

    # 小さな頃からの夢
    501011705: (_Option(speed=5, guts=5), _Option(stamina=5, wiz=5)),

    # 花瓶
    501011706: (_Option(guts=5, wiz=5), _Option(speed=5, stamina=5)),

    # たゆまぬ気魄【バトルクライ】
    501011800: (_Option(yaruki_up=True, power=10), _Option(vital=15)),

    # 邂逅する想慕【ミラージュメモリー】
    501011801: (_Option(guts=10, wiz=10), _Option(stamina=20)),

    # 永劫続く追撃【エンドレスマイターン】
    501011802: (_Option(skill_hint=True), _Option(speed=10, skill=15)),

    # ダンスレッスン
    501012506: (_Option(power=10), _Option(wiz=10)),

    # ヒシアマ寮長の朝ご飯
    501012510: (_Option(speed=10), _Option(power=10)),

    # ヒシアマ姐さんの裁縫テク
    501012511: (_Option(power=10), _Option(stamina=5, guts=5)),

    # 手も足も出せない相手……！？
    501012513: (_Option(power=20), _Option(guts=20)),

    # タイマン！　スケバン！　勝負服！
    501012514: (_Option(power=20), _Option(stamina=20)),

    # 友か、好敵手か
    501012515: (_Option(power=20), _Option(wiz=20)),

    # ヒシアマ姐さんの山菜採り
    501012520: (_Option(power=10, skill=15), _Option(skill_hint=True)),

    # 炎の思い出
    501012702: (_Option(power=10), _Option(wiz=10)),

    # クールでホットな姉妹
    501012703: (_Option(speed=10), _Option(stamina=10)),

    # 情熱は激流のごとく
    501012704: (_Option(speed=10), _Option(wiz=10), _Option(power=10)),

    # ヒシアマ姐さんの特等席
    501012705: (_Option(speed=5, power=5), _Option(guts=10)),

    # ヒシアマ姐さんと芸術
    501012706: (_Option(speed=10), _Option(stamina=10)),

    # ダンスレッスン
    501013506: (_Option(stamina=10), _Option(wiz=10)),

    # 孤島の女王
    501013510: (_Option(speed=10), _Option(stamina=10)),

    # その名はホヤ！
    501013511: (_Option(skill=30), _Option(stamina=10)),

    # 覚悟と使命の証
    501013513: (_Option(speed=10, wiz=10), _Option(power=20)),

    # 夜中のファンサ特訓
    501013514: (_Option(guts=20), _Option(speed=20)),

    # ご令嬢の風格
    501013515: (_Option(stamina=10, power=10), _Option(wiz=20)),

    # 思い出クッキング
    501013520: (_Option(vital=15), _Option(skill_hint=True)),

    # 銀幕の2人
    501013702: (_Option(stamina=10), _Option(wiz=5, skill=15)),

    # エキサイティングお嬢様
    501013703: (_Option(guts=10), _Option(power=10)),

    # 果てなき王国
    501013704: (_Option(stamina=10), _Option(wiz=10), _Option(speed=5, power=5)),

    # 掘り出し物
    501013705: (_Option(speed=10), _Option(guts=10)),

    # ラーメン3杯分の誘惑
    501013706: (_Option(skill=30), _Option(speed=5, stamina=5)),

    # 同室のあの子~そうだと思いましたわ~
    501013800: (_Option(skill_hint=True), _Option(stamina=10, skill=15)),

    # メジロ家のあの子たち~難しい選択~
    501013801: (_Option(speed=10, power=10), _Option(stamina=7, guts=7, wiz=7)),

    # ライバルのあの子~どんな舞台でも~
    501013802: (_Option(skill_hint=True), _Option(wiz=10, skill=15)),

    # ダンスレッスン
    501014506: (_Option(stamina=10), _Option(wiz=10)),

    # オリジナル・マスク
    501014510: (_Option(speed=10), _Option(power=10)),

    # サルサ・ロハ
    501014511: (_Option(stamina=10), _Option(power=10)),

    # 世界最強の決意を
    501014513: (_Option(power=20), _Option(stamina=20)),

    # サボテン料理をご馳走デース！
    501014514: (_Option(speed=10, stamina=10), _Option(wiz=20)),

    # 勇気の入場曲
    501014515: (_Option(power=20), _Option(speed=10, power=10)),

    # 特大ピザを狙え！
    501014520: (_Option(power=10, skill=15), _Option(skill_hint=True)),

    # 憧れのレスラー
    501014702: (_Option(stamina=10), _Option(speed=10)),

    # 衝撃の引退
    501014703: (_Option(guts=10), _Option(power=10)),

    # もう1度、決意を
    501014704: (_Option(guts=10), _Option(stamina=10), _Option(speed=5, stamina=5)),

    # 夜の学園のご老公？
    501014705: (_Option(yaruki_up=True, guts=5), _Option(vital=10)),

    # 贈る花言葉
    501014706: (_Option(yaruki_up=True, wiz=5), _Option(vital=10)),

    # 衣装に宿る熱き炎！
    501014800: (_Option(skill_hint=True), _Option(speed=7, power=7, guts=7)),

    # 熱！伝！導！
    501014801: (_Option(power=20), _Option(yaruki_up=True, wiz=10)),

    # 過去からの挑戦状！
    501014802: (_Option(speed=10, power=10), _Option(skill_hint=True)),

    # ダンスレッスン
    501015506: (_Option(stamina=10), _Option(speed=10)),

    # 聞こえる声は
    501015510: (_Option(power=10), _Option(wiz=10)),

    # 幾重もの輝き
    501015511: (_Option(vital=-10, power=20), _Option(speed=10)),

    # "覇王"として
    501015513: (_Option(wiz=20), _Option(power=20)),

    # 愛しき瞳の為に
    501015514: (_Option(stamina=10, guts=10), _Option(speed=20)),

    # 意志の力
    501015515: (_Option(wiz=20), _Option(speed=10, power=10)),

    # 尽くせ、礼
    501015520: (_Option(speed=10, skill=15), _Option(skill_hint=True)),

    # パジャマ姿の姫君
    501015702: (_Option(speed=10), _Option(stamina=10)),

    # 鏡が映すのは
    501015703: (_Option(wiz=10), _Option(guts=10)),

    # 輝きを君に
    501015704: (_Option(power=10), _Option(guts=10), _Option(wiz=10)),

    # 素晴らしき美を維持するために……
    501015705: (_Option(speed=10), _Option(wiz=10)),

    # 夕暮れ時のオペラオー劇場
    501015706: (_Option(power=10), _Option(vital=10)),

    # ダンスレッスン
    501016506: (_Option(stamina=10), _Option(wiz=10)),

    # 憧憬
    501016510: (_Option(power=10), _Option(vital=-10, power=20)),

    # 超越
    501016511: (_Option(power=10), _Option(stamina=5, guts=5)),

    # 意匠
    501016513: (_Option(speed=20), _Option(power=20)),

    # 武骨
    501016514: (_Option(stamina=20), _Option(wiz=20)),

    # 不動
    501016515: (_Option(speed=20), _Option(guts=20)),

    # 手腕
    501016520: (_Option(speed=15), _Option(skill_hint=True)),

    # 孤高のグルメ？
    501016702: (_Option(speed=5, power=5), _Option(stamina=10)),

    # ブライアンは見た……！
    501016703: (_Option(stamina=10), _Option(guts=10)),

    # ファミリーレストラン
    501016704: (_Option(speed=10), _Option(stamina=10), _Option(guts=10)),

    # 孤高の責任
    501016705: (_Option(stamina=5, guts=5), _Option(power=5, wiz=5)),

    # 得意距離？
    501016706: (_Option(stamina=10), _Option(wiz=10)),

    # ダンスレッスン
    501017506: (_Option(wiz=10), _Option(power=10)),

    # 前を往く者
    501017510: (_Option(speed=5, power=5), _Option(stamina=5, guts=5)),

    # 皇帝の社会勉強
    501017511: (_Option(vital=-10, stamina=10, power=10), _Option(wiz=5, skill=15)),

    # 道半ば、顧みて
    501017513: (_Option(speed=20), _Option(power=20)),

    # 笑う会長は服着たがる
    501017514: (_Option(wiz=20), _Option(guts=20)),

    # 道の果て、遠く望む
    501017515: (_Option(stamina=20), _Option(guts=20)),

    # 皇帝の余暇
    501017520: (_Option(wiz=10, skill=15), _Option(skill_hint=True)),

    # いついかなる時も
    501017524: (_Option(vital=-10, guts=20), _Option(vital=10)),

    # 突然の厚意
    501017525: (_Option(vital=-10, stamina=20), _Option(vital=10)),

    # 有言実行
    501017526: (_Option(vital=-10, power=20), _Option(vital=10)),

    # 竜吟虎嘯
    501017702: (_Option(speed=10), _Option(stamina=10)),

    # 徳高望重
    501017703: (_Option(wiz=10), _Option(power=10)),

    # 清風明月
    501017704: (_Option(speed=10), _Option(wiz=10), _Option(stamina=10)),

    # 皇帝の日課
    501017705: (_Option(power=10), _Option(guts=10)),

    # 皇帝の道
    501017706: (_Option(wiz=10), _Option(power=10)),

    # ダンスレッスン
    501018506: (_Option(power=10), _Option(speed=10)),

    # "女帝"と"帝王"
    501018510: (_Option(power=10), _Option(wiz=10)),

    # 花壇制作大作戦
    501018511: (_Option(vital=5, wiz=5), _Option(vital=-10, speed=10, power=10)),

    # 君に花を
    501018513: (_Option(wiz=20), _Option(speed=20)),

    # 麗しきストレス発散法？
    501018514: (_Option(stamina=20), _Option(guts=20)),

    # 道導
    501018515: (_Option(speed=20), _Option(power=20)),

    # "女帝"と"皇帝"
    501018520: (_Option(skill_hint=True), _Option(yaruki_up=True, skill=15)),

    # 捕獲せよ！
    501018524: (_Option(vital=10), _Option(vital=-10, yaruki_up=True, speed=10)),

    # 尻尾ケアは大切に
    501018525: (_Option(vital=10), _Option(vital=-10, yaruki_up=True, power=10)),

    # フリーダム目安箱
    501018526: (_Option(vital=10), _Option(vital=-10, yaruki_up=True, wiz=10)),

    # 小さな出会い
    501018702: (_Option(wiz=10), _Option(guts=10)),

    # さつまいもケーキ
    501018703: (_Option(power=10), _Option(stamina=10)),

    # 麗姿、瞳に焼き付いて
    501018704: (_Option(speed=10), _Option(power=10), _Option(stamina=10)),

    # 点滅信号、渡るべからず
    501018705: (_Option(wiz=10), _Option(power=10)),

    # 静寂に燃えて
    501018706: (_Option(stamina=10), _Option(speed=10)),

    # 隣に立つのは……！
    501018800: (_Option(skill_hint=True), _Option(guts=10, wiz=10)),

    # ネバー・エンディング・ロード
    501018801: (_Option(skill_hint=True), _Option(power=20)),

    # 女帝、甘える
    501018802: (_Option(speed=10, stamina=10), _Option(stamina=10, power=10)),

    # ダンスレッスン
    501020506: (_Option(guts=10), _Option(stamina=10)),

    # 検証〜ネコ語は実在するのか？
    501020510: (_Option(stamina=10), _Option(wiz=10)),

    # 闇の仕事？
    501020511: (_Option(speed=10), _Option(power=10)),

    # お香でおやすみ
    501020513: (_Option(wiz=20), _Option(stamina=20)),

    # 策士VS王
    501020514: (_Option(guts=20), _Option(speed=20)),

    # 誰がために君は走る
    501020515: (_Option(stamina=20), _Option(power=20)),

    # セイちゃん脱出作戦
    501020520: (_Option(speed=10, skill=15), _Option(skill_hint=True)),

    # ネコの名人
    501020702: (_Option(wiz=10), _Option(speed=10)),

    # ネコとの散歩
    501020703: (_Option(stamina=10), _Option(guts=10)),

    # ネコとの別れ
    501020704: (_Option(wiz=10), _Option(stamina=10), _Option(power=10)),

    # お昼寝マイスター
    501020705: (_Option(stamina=10), _Option(wiz=10)),

    # 曇りのち……
    501020706: (_Option(guts=10), _Option(speed=10)),

    # ダンスレッスン
    501023506: (_Option(speed=10), _Option(guts=10)),

    # 料理と姉妹の思い出
    501023510: (_Option(power=10), _Option(stamina=5, wiz=5)),

    # 彼女の新たな側面
    501023511: (_Option(speed=10), _Option(stamina=10)),

    # 持つべきか、捨てるべきか
    501023513: (_Option(wiz=20), _Option(stamina=10, power=10)),

    # 理論に基づいた昔ばなし
    501023514: (_Option(power=20), _Option(guts=20)),

    # 暴れ龍との攻防
    501023520: (_Option(power=5, guts=10), _Option(skill_hint=True)),

    # カフェで読書を
    501023702: (_Option(stamina=10), _Option(speed=10)),

    # 明暗を分かつ
    501023703: (_Option(wiz=10), _Option(guts=10)),

    # 緊急プレゼンテーション
    501023704: (_Option(wiz=10), _Option(power=10), _Option(stamina=10)),

    # かくれんぼマイスター
    501023705: (_Option(guts=10), _Option(speed=10)),

    # ゲームに関する実践証明
    501023706: (_Option(wiz=10), _Option(power=10)),

    # ダンスレッスン
    501024506: (_Option(guts=10), _Option(speed=10)),

    # 勉強はマヤにおまかせ☆
    501024510: (_Option(power=5, guts=5), _Option(wiz=10)),

    # 大人なモデルの秘訣！
    501024511: (_Option(vital=-10, stamina=20), _Option(speed=10)),

    # マヤのドキドキ☆肝試し！
    501024513: (_Option(power=20), _Option(guts=20)),

    # 甘いキモチをキミに♪
    501024514: (_Option(stamina=20), _Option(wiz=20)),

    # マヤノ・テイクオフ☆
    501024515: (_Option(speed=20), _Option(stamina=20)),

    # マヤちんのレース講座☆
    501024520: (_Option(stamina=10, skill=15), _Option(skill_hint=True)),

    # マヤのワクワク☆配信！
    501024702: (_Option(stamina=5, power=5), _Option(guts=10)),

    # マヤのルンルン☆配信！
    501024703: (_Option(speed=10), _Option(stamina=10)),

    # マヤのキラキラ☆決心！
    501024704: (_Option(speed=5, stamina=5), _Option(power=10), _Option(wiz=10)),

    # マヤの大切な人！
    501024705: (_Option(speed=10), _Option(guts=10)),

    # 星に願いを
    501024706: (_Option(wiz=10), _Option(speed=10)),

    # You’re My Sunshine☆
    501024800: (_Option(stamina=20), _Option(power=20)),

    # Meant To Be♪
    501024801: (_Option(skill_hint=True), _Option(skill_hint=True)),

    # With My Whole Heart!
    501024802: (_Option(stamina=10, skill=15), _Option(vital=15)),

    # ダンスレッスン
    501026506: (_Option(skill=20), _Option(stamina=10)),

    # 『オペレーション：オーダー遂行』
    501026510: (_Option(stamina=10), _Option(power=10)),

    # 『オペレーション：補習』
    501026511: (_Option(vital=10, yaruki_up=True), _Option(wiz=10)),

    # 憧れの光跡
    501026513: (_Option(speed=20), _Option(power=20)),

    # 笑顔の連鎖
    501026514: (_Option(stamina=20), _Option(guts=20)),

    # 頼るべきは
    501026515: (_Option(wiz=20), _Option(power=20)),

    # 『オペレーション：外出時トラブル』
    501026520: (_Option(stamina=10, skill=15), _Option(skill_hint=True)),

    # 思い出を作ろう
    501026702: (_Option(speed=10), _Option(guts=10)),

    # ブルボンの挑戦？
    501026703: (_Option(power=10), _Option(wiz=10)),

    # かけがえのないすべて
    501026704: (_Option(stamina=10), _Option(speed=10), _Option(power=10)),

    # 『オペレーション：ダンスフィーバー』
    501026705: (_Option(stamina=5, guts=5), _Option(stamina=5, wiz=5)),

    # 『オペレーション：エンジョイ縁日』
    501026706: (_Option(power=10), _Option(stamina=5, guts=5)),

    # ダンスレッスン
    501027506: (_Option(power=10), _Option(speed=10)),

    # マッスル・ジェラシー
    501027510: (_Option(guts=10), _Option(wiz=10)),

    # ポニー少女とオオカミ王子
    501027511: (_Option(vital=5, stamina=5), _Option(vital=5, speed=5)),

    # 周りから見た勝負服姿
    501027513: (_Option(guts=20), _Option(speed=20)),

    # ドキドキ水族館
    501027514: (_Option(power=10, wiz=10), _Option(stamina=10, wiz=10)),

    # 本当の爽やかさ
    501027515: (_Option(stamina=20), _Option(power=20)),

    # 積み上げた本当のこと
    501027520: (_Option(power=10, skill=15), _Option(skill_hint=True)),

    # 息詰まる息抜き
    501027702: (_Option(stamina=10), _Option(power=10)),

    # はやる気持ち
    501027703: (_Option(wiz=10), _Option(speed=10)),

    # 息抜きと信頼と
    501027704: (_Option(speed=10), _Option(stamina=10), _Option(power=10)),

    # 頼れる助っ人、登場！
    501027705: (_Option(power=10), _Option(guts=10)),

    # ウマドルの小さなファンたち
    501027706: (_Option(power=10), _Option(wiz=10)),

    # ダンスレッスン
    501030506: (_Option(stamina=10), _Option(speed=10)),

    # 参考にしたくて
    501030510: (_Option(vital=-10, guts=20), _Option(vital=5, skill=15)),

    # 素敵な世界に会いたくて
    501030511: (_Option(stamina=10), _Option(speed=5, wiz=5)),

    # 相応しくない自分
    501030513: (_Option(guts=20), _Option(power=20)),

    # 甘く賑やかな幸福
    501030514: (_Option(speed=10, stamina=10), _Option(wiz=20)),

    # 相応しい自分
    501030515: (_Option(guts=10, wiz=10), _Option(stamina=10, power=10)),

    # 何事も前向きに？
    501030520: (_Option(stamina=5, guts=10), _Option(skill_hint=True)),

    # てんとう虫が離れても
    501030702: (_Option(stamina=10), _Option(wiz=10)),

    # 雲が空を覆っても
    501030703: (_Option(speed=5, power=5), _Option(guts=10)),

    # わたしのたいよう
    501030704: (_Option(guts=5, wiz=5), _Option(speed=5, power=5), _Option(stamina=10)),

    # ライスにお任せ……！
    501030705: (_Option(guts=10), _Option(speed=10)),

    # 夕焼けの1ページ
    501030706: (_Option(power=5, guts=5), _Option(stamina=5, wiz=5)),

    # ダンスレッスン
    501032506: (_Option(stamina=10), _Option(speed=10)),

    # マイペース・タキオン
    501032510: (_Option(guts=10), _Option(speed=5, power=5)),

    # 最強の協力者！？
    501032511: (_Option(vital=-20, stamina=15, guts=10), _Option(vital=5, wiz=5)),

    # 信念を表すもの
    501032513: (_Option(stamina=20), _Option(speed=20)),

    # データを手に入れろ！
    501032514: (_Option(wiz=20), _Option(power=20)),

    # だだっ子タキオン
    501032515: (_Option(stamina=10, guts=10), _Option(wiz=20)),

    # 正義の圧？
    501032520: (_Option(wiz=10, skill=15), _Option(skill_hint=True)),

    # 速くなれるお薬依頼？
    501032702: (_Option(power=5, guts=5), _Option(speed=5, wiz=5)),

    # 研究の真意
    501032703: (_Option(wiz=10), _Option(speed=10)),

    # 目指す場所に近道はない
    501032704: (_Option(guts=10), _Option(wiz=10), _Option(power=10)),

    # 黒い空からの贈り物
    501032705: (_Option(speed=5, power=5), _Option(guts=10)),

    # 肉体改造思いのまま！
    501032706: (_Option(power=5, wiz=5), _Option(stamina=10)),

    # ダンスレッスン
    501035506: (_Option(guts=10), _Option(wiz=10)),

    # 雨ニモ負ケズ
    501035510: (_Option(vital=-10, stamina=10, skill=15), _Option(power=10)),

    # この壁を越えてゆけ！
    501035511: (_Option(yaruki_up=True, guts=5), _Option(yaruki_up=True, power=5)),

    # 全力テスト！
    501035513: (_Option(guts=20), _Option(speed=20)),

    # 全力ファッション！
    501035514: (_Option(stamina=20), _Option(power=10, guts=10)),

    # 全力がんばる！
    501035515: (_Option(speed=10, wiz=10), _Option(power=20)),

    # 新たな気づき
    501035520: (_Option(speed=10, skill=15), _Option(skill_hint=True)),

    # 三国志演技
    501035702: (_Option(stamina=5, skill=15), _Option(power=5, skill=15)),

    # いきなりフットサル！？
    501035703: (_Option(guts=10), _Option(speed=10)),

    # 最後の片道切符
    501035704: (_Option(guts=10), _Option(speed=10), _Option(power=10)),

    # 悩みなんて吹き飛ばせ！
    501035705: (_Option(yaruki_up=True, power=5), _Option(speed=5, skill=15)),

    # よく泣くお姉ちゃん
    501035706: (_Option(guts=5, skill=15), _Option(yaruki_up=True, power=5)),

    # ダンスレッスン
    501038506: (_Option(speed=10), _Option(guts=10)),

    # せーのっ！
    501038510: (_Option(speed=10), _Option(wiz=10)),

    # World is……？
    501038511: (_Option(power=10), _Option(speed=10)),

    # どんなカレンがお・す・き？
    501038513: (_Option(speed=10, power=10), _Option(stamina=10, guts=10)),

    # カレン的SNSとの付き合い方♪
    501038514: (_Option(speed=20), _Option(wiz=20)),

    # これがカレンの勝負服
    501038515: (_Option(speed=10, stamina=10), _Option(speed=10, power=10)),

    # お勉強させてもらいます♪
    501038520: (_Option(vital=-10, speed=20), _Option(skill_hint=True)),

    # まずは、なかよくなるため
    501038702: (_Option(power=10), _Option(wiz=10)),

    # もっと、つながるため
    501038703: (_Option(guts=10), _Option(power=10)),

    # すべてはーーーのため
    501038704: (_Option(speed=5, power=5), _Option(speed=10), _Option(speed=5, wiz=5)),

    # 思い出の味
    501038705: (_Option(stamina=10), _Option(power=10)),

    # ガタン、ゴトン、ころん
    501038706: (_Option(wiz=10), _Option(stamina=10)),

    # ダンスレッスン
    501040506: (_Option(guts=10), _Option(wiz=10)),

    # サロン・ド・ボーテ　シチー
    501040510: (_Option(guts=10), _Option(speed=10)),

    # 食べないのは悪手だよ
    501040511: (_Option(power=10), _Option(stamina=10)),

    # order from client
    501040513: (_Option(speed=20), _Option(guts=20)),

    # 子どもと大人
    501040514: (_Option(wiz=20), _Option(stamina=10, guts=10)),

    # 心に描いたもの
    501040515: (_Option(speed=20), _Option(power=20)),

    # 寮対抗クイズバトル
    501040520: (_Option(speed=10, power=5), _Option(skill_hint=True)),

    # ま、やる以上はね
    501040702: (_Option(wiz=10), _Option(speed=5, skill=15)),

    # 表立っては言わないけど
    501040703: (_Option(stamina=5, power=5), _Option(guts=10)),

    # たまには裸足になりたい
    501040704: (_Option(stamina=10), _Option(speed=10), _Option(power=10)),

    # 寄り道したいお年頃
    501040705: (_Option(stamina=10), _Option(speed=10)),

    # ヨガのポーズ！
    501040706: (_Option(guts=10), _Option(power=10)),

    # ダンスレッスン
    501041506: (_Option(guts=10), _Option(wiz=10)),

    # マクラノバクシン！
    501041510: (_Option(wiz=10), _Option(stamina=10)),

    # 求む、生徒の声！！
    501041511: (_Option(vital=-10, stamina=10, power=10), _Option(speed=10)),

    # 恋はバクシン！
    501041513: (_Option(stamina=10, wiz=10), _Option(guts=20)),

    # 委員長のいない日
    501041514: (_Option(speed=20), _Option(power=20)),

    # 勝負服でバクシン！
    501041515: (_Option(power=10, guts=10), _Option(wiz=20)),

    # バクシン的な謎解き！
    501041520: (_Option(guts=10, skill=15), _Option(skill_hint=True)),

    # クラスメイトとバクシン！
    501041702: (_Option(power=5, guts=5), _Option(speed=5, wiz=5)),

    # 最高のバクシン！
    501041703: (_Option(wiz=10), _Option(stamina=5, guts=5)),

    # これからもバクシン！
    501041704: (_Option(speed=10), _Option(guts=5, wiz=5), _Option(power=10)),

    # 大切な方と、一緒にッ！
    501041705: (_Option(guts=10), _Option(speed=5, stamina=5)),

    # 最速の王
    501041706: (_Option(power=5, wiz=5), _Option(stamina=10)),

    # ダンスレッスン
    501045506: (_Option(stamina=10), _Option(speed=10)),

    # 1日体験☆陶芸教室
    501045510: (_Option(speed=5, wiz=5), _Option(stamina=10)),

    # 迷子を捜せ！
    501045511: (_Option(vital=-10, stamina=10, power=10), _Option(wiz=10)),

    # 自己満足な願い
    501045513: (_Option(power=20), _Option(stamina=20)),

    # 命には愛を込めて
    501045514: (_Option(speed=10, stamina=10, wiz=20), _Option(wiz=20)),

    # 焦らずにいきましょう
    501045515: (_Option(guts=20), _Option(stamina=10, power=10)),

    # 危険なご褒美
    501045520: (_Option(guts=10, skill=15), _Option(skill_hint=True)),

    # 息抜きは甘え？
    501045702: (_Option(stamina=10), _Option(wiz=10)),

    # 不安を拭って
    501045703: (_Option(power=10), _Option(speed=5, guts=5)),

    # 分かち合いましょう
    501045704: (_Option(stamina=10), _Option(speed=10), _Option(power=10)),

    # ギュッとマッサージ！
    501045705: (_Option(guts=10), _Option(speed=5, wiz=5)),

    # 星を見るなら2人で
    501045706: (_Option(power=5, guts=5), _Option(stamina=10)),

    # ダンスレッスン
    501046506: (_Option(guts=10), _Option(wiz=10)),

    # 研究対象はウマドル？
    501046510: (_Option(power=10), _Option(wiz=10)),

    # ドキドキ☆シチュエーション
    501046511: (_Option(power=10), _Option(stamina=10)),

    # 磨いて☆DIAMOND
    501046513: (_Option(speed=20), _Option(power=10, guts=10)),

    # ウマドル☆Friendship！
    501046514: (_Option(wiz=20), _Option(power=20)),

    # ドタバタ☆KIDSパニック！
    501046515: (_Option(speed=20), _Option(stamina=20)),

    # 燃やせ☆ウマドル魂
    501046520: (_Option(stamina=10, guts=10), _Option(skill_hint=True)),

    # テストdeリカバリー☆
    501046702: (_Option(wiz=10), _Option(power=10)),

    # 届いてforYou☆恩返し♪
    501046703: (_Option(speed=10), _Option(power=10)),

    # メモリー☆聖地巡礼
    501046704: (_Option(power=10), _Option(guts=10), _Option(speed=10)),

    # シェアリング☆メモリー
    501046705: (_Option(stamina=10), _Option(guts=10)),

    # フューチャー☆ロケハン
    501046706: (_Option(wiz=10), _Option(power=10)),

    # ダンスレッスン
    501050506: (_Option(guts=10), _Option(wiz=10)),

    # 後日レポート提出済
    501050510: (_Option(speed=10), _Option(stamina=5, power=5)),

    # Unknown music
    501050511: (_Option(power=10), _Option(wiz=10)),

    # アタシのまま、強く
    501050513: (_Option(power=20), _Option(speed=20)),

    # タイシンのSOS
    501050514: (_Option(speed=10, wiz=10), _Option(stamina=20)),

    # ハラハラなサバイバル
    501050515: (_Option(power=20), _Option(guts=10, wiz=10)),

    # 距離
    501050520: (_Option(yaruki_up=True, guts=10), _Option(skill_hint=True)),

    # 『bg』
    501050702: (_Option(stamina=10), _Option(speed=10)),

    # 『easy game』
    501050703: (_Option(power=10), _Option(guts=10)),

    # 『gg』
    501050704: (_Option(guts=10), _Option(wiz=10), _Option(stamina=10)),

    # 寡黙なふたり
    501050705: (_Option(stamina=10), _Option(speed=10)),

    # かごの扉はその手で開けろ
    501050706: (_Option(stamina=5, guts=5), _Option(speed=5, power=5)),

    # ダンスレッスン
    501052506: (_Option(speed=10), _Option(wiz=10)),

    # 腕相撲で勝負！
    501052510: (_Option(wiz=10), _Option(power=10)),

    # 大事な探しもの
    501052511: (_Option(vital=-10, guts=20), _Option(stamina=10)),

    # 大好きな勝負服！
    501052513: (_Option(speed=20), _Option(power=20)),

    # 一緒に取材！
    501052514: (_Option(power=20), _Option(stamina=20)),

    # 綱引き大会！
    501052515: (_Option(guts=20), _Option(speed=20)),

    # 砂の修業！
    501052520: (_Option(guts=10, skill=15), _Option(vital=15)),

    # 公園って楽しい！
    501052703: (_Option(speed=10), _Option(power=10)),

    # 秘密のおやすみ計画！
    501052704: (_Option(speed=10), _Option(power=10), _Option(wiz=10)),

    # かっくいいね！
    501052705: (_Option(skill=30), _Option(wiz=10)),

    # 食べるの忘れてた！
    501052706: (_Option(guts=10), _Option(stamina=10)),

    # ダンスレッスン
    501056506: (_Option(power=10), _Option(wiz=10)),

    # 呪いのカメラ
    501056510: (_Option(wiz=10), _Option(skill=30)),

    # マンハッタンの夢
    501056511: (_Option(skill_hint=True), _Option(stamina=10)),

    # 選ばれし者の間
    501056513: (_Option(guts=20), _Option(speed=20)),

    # 開運！　ラッキーテレフォン
    501056514: (_Option(stamina=10, wiz=10), _Option(power=20)),

    # 流星群でグングンと
    501056515: (_Option(speed=10, power=10), _Option(stamina=10, guts=10)),

    # プリティー・ガンマンズ
    501056520: (_Option(skill=15, yaruki_up=True), _Option(power=10)),

    # フクキタル的厄除けキタル
    501056702: (_Option(guts=10), _Option(power=10)),

    # ピンチの後は……？
    501056703: (_Option(speed=10), _Option(stamina=5, wiz=5)),

    # フクキタル的オマジナイ
    501056704: (_Option(speed=5, guts=5), _Option(stamina=5, power=5), _Option(wiz=10)),

    # レッツ・バンジー☆
    501056705: (_Option(stamina=10), _Option(speed=5, wiz=5)),

    # お礼参り
    501056706: (_Option(power=5, guts=5), _Option(speed=5, stamina=5)),

    # ダンスレッスン
    501058506: (_Option(guts=10), _Option(power=10)),

    # ベストショットの行方
    501058510: (_Option(wiz=10), _Option(stamina=10)),

    # 不屈の1歩は小さな1歩
    501058511: (_Option(guts=10), _Option(vital=10)),

    # 熱闘！激辛勝負
    501058513: (_Option(stamina=20), _Option(speed=20)),

    # あんしんかばん
    501058514: (_Option(wiz=10, skill=15), _Option(power=20)),

    # うみゃうみゃうみゃ
    501058515: (_Option(power=10, wiz=10), _Option(guts=20)),

    # 救いの言葉
    501058520: (_Option(power=10, skill=15), _Option(skill_hint=True)),

    # 貴方のこぶしが名残に揺れて
    501058702: (_Option(power=10), _Option(stamina=10)),

    # 私は独りでさまようばかり
    501058703: (_Option(stamina=10), _Option(guts=10)),

    # 募る想い、嗚呼届いていますか
    501058704: (_Option(power=10), _Option(speed=10), _Option(guts=10)),

    # ミルク味の夕暮れ
    501058705: (_Option(wiz=10), _Option(speed=5, stamina=5)),

    # 等価交換？
    501058706: (_Option(speed=10), _Option(wiz=10)),

    # ダンスレッスン
    501060506: (_Option(speed=10), _Option(guts=10)),

    # 雨の日の遊戯
    501060510: (_Option(wiz=10), _Option(vital=-10, stamina=10, guts=10)),

    # ガラじゃないですし
    501060511: (_Option(vital=5, yaruki_up=True), _Option(speed=5, power=5)),

    # ネイチャさんとお疲れトレーナー
    501060513: (_Option(power=20), _Option(stamina=20)),

    # ほろ苦いキラキラ
    501060514: (_Option(power=20), _Option(speed=20)),

    # 願いを叶えるクリスマスカラー
    501060515: (_Option(guts=20), _Option(stamina=20)),

    # 嵐の如き助っ人
    501060520: (_Option(skill_hint=True), _Option(speed=5, stamina=5, power=5)),

    # おふくろからの電話
    501060702: (_Option(stamina=10), _Option(speed=10)),

    # アタシもたまには
    501060703: (_Option(stamina=5, guts=5), _Option(stamina=5, power=5)),

    # 黄昏ビタースイート
    501060704: (_Option(speed=10), _Option(guts=10), _Option(wiz=10)),

    # 映す想い
    501060705: (_Option(speed=10), _Option(power=10)),

    # お魚、観ましょ
    501060706: (_Option(guts=10), _Option(speed=10)),

    # ダンスレッスン
    501061506: (_Option(guts=10), _Option(speed=10)),

    # 映画は学びでいっぱいよ
    501061510: (_Option(speed=5, guts=5), _Option(stamina=10)),

    # 私に1番似合う服
    501061513: (_Option(speed=10, guts=10), _Option(power=20)),

    # 走るだけがすべてではないのよ
    501061514: (_Option(stamina=20), _Option(speed=10, power=10)),

    # マナーくらい常識よ？
    501061515: (_Option(guts=20), _Option(stamina=10, wiz=10)),

    # 学力だって一流よ
    501061520: (_Option(wiz=10, skill=15), _Option(skill_hint=True)),

    # 放課後サイダー
    501061524: (_Option(guts=10), _Option(speed=10)),

    # 三人寄れば一流の知恵
    501061525: (_Option(wiz=10), _Option(stamina=10)),

    # 一流のスポット
    501061702: (_Option(guts=10), _Option(speed=10)),

    # 一流の収穫
    501061703: (_Option(power=5, guts=5), _Option(speed=5, stamina=5)),

    # 一流の条件
    501061704: (_Option(power=10), _Option(wiz=10), _Option(guts=10)),

    # 人混みなんて問題じゃないわ
    501061705: (_Option(speed=10), _Option(power=10)),

    # 門限破りは二流よ
    501061706: (_Option(guts=5, wiz=5), _Option(speed=5, power=5)),

    # 曲がり角には、気をつけます！
    801001001: (_Option(skill_hint=True), _Option(guts=15)),

    # あれもこれもで、悩んじゃいます！
    801001002: (_Option(vital=10, yaruki_up=True), _Option(vital=-10, stamina=15, skill=15)),

    # どこまでも
    801002001: (_Option(speed=10, stamina=5), _Option(speed=15)),

    # どうすれば
    801002002: (_Option(speed=5, stamina=5, wiz=5), _Option(skill_hint=True)),

    # ボクのやり方
    801003001: (_Option(yaruki_up=True, skill=15), _Option(guts=15)),

    # ボクの武器
    801003002: (_Option(yaruki_up=True, guts=10), _Option(skill_hint=True)),

    # 可愛い後輩ちゃんのためだもの
    801004001: (_Option(skill_hint=True), _Option(vital=5, speed=10)),

    # マブいドライブだっちゅ～の
    801004002: (_Option(yaruki_up=True, speed=5), _Option(yaruki_up=True, wiz=5)),

    # スライハンド
    801005001: (_Option(wiz=5, skill=15), _Option(power=5, skill=15)),

    # ミスディレクション
    801005002: (_Option(skill_hint=True), _Option(skill=30)),

    # 何と答えれば……
    801006001: (_Option(vital=5, power=5), _Option(vital=-10, guts=15)),

    # 人混みは大変だ……
    801006002: (_Option(power=5, skill=15), _Option(skill_hint=True)),

    # 冒険家ゴールドシップ
    801007001: (_Option(stamina=15), _Option(guts=10, skill=15)),

    # 甦れ！ゴルシ印のソース焼きそば！
    801007002: (_Option(yaruki_up=True, stamina=5), _Option(skill_hint=True)),

    # 憧れのセリフ
    801008001: (_Option(power=10), _Option(power=5, skill=15)),

    # 大通りの強敵
    801008002: (_Option(skill_hint=True), _Option(power=5, skill=15)),

    # 明日は私が勝つんだから！
    801009001: (_Option(wiz=10), _Option(yaruki_up=True, skill=15)),

    # このくらい平気なんだから！
    801009002: (_Option(skill_hint=True), _Option(vital=20, yaruki_up=True)),

    # イエス！　レッツ・ハグ☆
    801010001: (_Option(speed=10), _Option(speed=5, power=5)),

    # オゥ！トゥナイト・パーティー☆
    801010002: (_Option(vital=-10, speed=5, power=10), _Option(skill_hint=True)),

    # 文殿、思ひ煩ふ
    801011001: (_Option(wiz=10), _Option(guts=5, wiz=5)),

    # 昼つ方、打ち語らふ
    801011002: (_Option(skill_hint=True), _Option(skill_hint=True)),

    # ヒシアマ姐さん奮闘記～問題児編～
    801012001: (_Option(vital=10, wiz=5), _Option(vital=-10, speed=10, guts=5)),

    # ヒシアマ姐さん奮闘記～追い込み編～
    801012002: (_Option(skill_hint=True), _Option(power=5, skill=15)),

    # 高みに至る為
    801013002: (_Option(stamina=5, guts=5), _Option(skill_hint=True)),

    # メラメラ・ファイアー！
    801014001: (_Option(stamina=10), _Option(vital=-10, power=20)),

    # シークレット・ノート
    801014002: (_Option(power=10), _Option(skill_hint=True)),

    # 有限の時を越えて
    801015002: (_Option(vital=10, skill=15), _Option(skill_hint=True)),

    # 孤狼
    801016002: (_Option(speed=3, stamina=3, power=3), _Option(skill_hint=True)),

    # "皇帝"の激励
    801017001: (_Option(speed=10), _Option(vital=-10, skill=30)),

    # 生徒会長の思い
    801017002: (_Option(skill_hint=True), _Option(stamina=15)),

    # 峻厳にして優渥
    801018001: (_Option(skill_hint=True), _Option(vital=10, wiz=10)),

    # 俊敏にして剛腕
    801018002: (_Option(power=15), _Option(speed=10, stamina=5)),

    # ウマ娘ちゃん欠乏症
    801019001: (_Option(vital=5, speed=5), _Option(speed=5, power=5)),

    # エモのためなら雨の中でも
    801019002: (_Option(skill_hint=True), _Option(skill_hint=True)),

    # ゆる募、ネコの捕まえ方
    801020001: (_Option(vital=10, wiz=5), _Option(vital=-10, speed=15, stamina=5)),

    # ゆる募、助言者
    801020002: (_Option(wiz=15), _Option(skill_hint=True)),

    # タマモ先輩の学園案内
    801021001: (_Option(wiz=10), _Option(stamina=5, guts=5)),

    # 負けられん戦い！
    801021002: (_Option(skill_hint=True), _Option(stamina=5, wiz=5)),

    # ときめきシューズ
    801022001: (_Option(speed=5, skill=10), _Option(vital=-10, stamina=5, skill=20)),

    # 思い出クローバー
    801022002: (_Option(skill_hint=True), _Option(guts=15)),

    # ぎりぎり様相論
    801023001: (_Option(power=15), _Option(speed=10, skill=15)),

    # 脱・無難論
    801023002: (_Option(vital=-10, skill_hint=True), _Option(vital=10, stamina=10)),

    # マヤノ的おやつ会議！
    801024001: (_Option(stamina=5, guts=5), _Option(stamina=10)),

    # マヤノ的ファッション会議！
    801024002: (_Option(skill_hint=True), _Option(stamina=10)),

    # 夜の独走
    801025001: (_Option(stamina=10), _Option(vital=10, stamina=5)),

    # 静けさを嗜む
    801025002: (_Option(stamina=5, skill=15), _Option(skill_hint=True)),

    # 他人に危害を及ぼしてはならない
    801026001: (_Option(vital=-10, stamina=5, power=15), _Option(vital=10, wiz=5)),

    # 命令は守らなければならない
    801026002: (_Option(skill_hint=True), _Option(speed=10, skill=15)),

    # あくまで薦められただけ
    801027002: (_Option(skill_hint=True), _Option(vital=30)),

    # どーんと☆召し上がれ♪
    801028001: (_Option(vital=10), _Option(vital=-5, power=15)),

    # どーんと☆お任せあれ♪
    801028002: (_Option(stamina=10), _Option(vital=-15, skill_hint=True)),

    # イカすライブのために
    801029001: (_Option(guts=10), _Option(vital=-10, guts=15)),

    # シチースポットを目指して
    801029002: (_Option(vital=-10, yaruki_up=True, guts=10), _Option(skill_hint=True)),

    # お花屋さんでの1ページ
    801030001: (_Option(yaruki_up=True), _Option(stamina=10)),

    # 曇りの日の1ページ
    801030002: (_Option(speed=5, guts=5), _Option(skill_hint=True)),

    # 鬼ごっこ、なの！
    801031001: (_Option(vital=10, speed=5), _Option(skill_hint=True)),

    # 要検証・睡眠時間と作業能率
    801032001: (_Option(power=5, wiz=5), _Option(wiz=10)),

    # 要検証・他者の介在による偶発性
    801032002: (_Option(skill_hint=True), _Option(wiz=10)),

    # 全・力・筋・肉！！
    801035001: (_Option(stamina=5, skill=15), _Option(yaruki_up=True, skill=15)),

    # 全・力・競・走！！
    801035002: (_Option(skill_hint=True), _Option(skill=30)),

    # //要検証
    801036001: (_Option(vital=10, guts=5), _Option(vital=-10, stamina=5, guts=10)),

    # 想定外のお昼
    801037001: (_Option(vital=15), _Option(speed=5, guts=5)),

    # 想定外への対応
    801037002: (_Option(guts=10), _Option(skill_hint=True)),

    # プリンセス、殴る！
    801039001: (_Option(guts=10), _Option(yaruki_up=True)),

    # プリンセス、逃走！
    801039002: (_Option(vital=10), _Option(skill_hint=True)),

    # 13:12/昼休み、気合い入れなきゃ
    801040002: (_Option(skill=30), _Option(skill_hint=True)),

    # 優等生の一石二鳥！！
    801041001: (_Option(speed=15), _Option(speed=5, power=10)),

    # 走りだすほどの！！
    801041002: (_Option(skill_hint=True), _Option(vital=-10, speed=10, power=5)),

    # 全力でパッション！
    801042001: (_Option(vital=10, yaruki_up=True), _Option(power=5, guts=5)),

    # 全力でシンキング！
    801042002: (_Option(wiz=20), _Option(vital=-10, skill_hint=True)),

    # ガブッと、撲滅！
    801043001: (_Option(speed=3, yaruki_up=True), _Option(vital=10, skill=5)),

    # ガブッと、突撃！
    801043002: (_Option(skill=15), _Option(speed=3, skill_hint=True)),

    # ミラクル☆エスケープ
    801044001: (_Option(vital=10, speed=5), _Option(vital=-10, speed=20)),

    # お手伝いもお任せ♪
    801045001: (_Option(vital=15), _Option(stamina=10)),

    # お気遣いもお任せ♪
    801045002: (_Option(skill_hint=True), _Option(vital=10, stamina=5)),

    # ライブはコーレスが命☆
    801046001: (_Option(stamina=5, guts=10), _Option(wiz=15)),

    # かわいかったら見に来てね☆
    801046002: (_Option(vital=-10, power=10, skill_hint=True), _Option(vital=10, wiz=5)),

    # 読書家あるある
    801047001: (_Option(speed=5, wiz=5), _Option(vital=10, power=5)),

    # 託された物語
    801047002: (_Option(stamina=10, wiz=10), _Option(skill_hint=True)),

    # 別に、ほっといて
    801050001: (_Option(stamina=5, skill=15), _Option(power=5, skill=15)),

    # 別に、邪魔しないで
    801050002: (_Option(skill_hint=True), _Option(skill_hint=True), _Option(skill=30)),

    # きれいに咲こうねっ♪
    801051002: (_Option(wiz=15), _Option(speed=10, power=5)),

    # うららん☆テスト勉強
    801052001: (_Option(vital=10, wiz=5), _Option(yaruki_up=True, wiz=5)),

    # うららん☆ふくへーダッシュ！
    801052002: (_Option(skill_hint=True), _Option(yaruki_up=True, vital=10)),

    # トラブル、上等っス！
    801053002: (_Option(stamina=5, guts=5), _Option(vital=-10, skill_hint=True)),

    # ヒーローの苦悩
    801054001: (_Option(vital=15), _Option(vital=5, power=5)),

    # 必殺技を手に入れろ！
    801054002: (_Option(skill_hint=True), _Option(vital=30)),

    # 問答無用のマーベラス☆
    801055001: (_Option(vital=10, speed=5), _Option(yaruki_up=True, speed=5)),

    # マーベラスにするために☆
    801055002: (_Option(vital=10, yaruki_up=True), _Option(skill_hint=True)),

    # 全力スピリチュアル
    801056001: (_Option(wiz=5, skill=15), _Option(vital=-10, speed=5, stamina=5, power=5)),

    # 信仰心と親切心が交わる時ーー
    801056002: (_Option(skill=30), _Option(vital=20)),

    # 私……改革ですっ
    801058001: (_Option(vital=10), _Option(guts=15)),

    # にんじん……買ってくださいっ
    801058002: (_Option(vital=10, wiz=5), _Option(skill_hint=True)),

    # やってみてもいい
    801059001: (_Option(vital=15), _Option(yaruki_up=True, skill=15)),

    # 喜んでくれるかな……
    801059002: (_Option(skill=45), _Option(skill_hint=True)),

    # （ニャンとも）ガラじゃない
    801060001: (_Option(vital=20), _Option(vital=10, wiz=5)),

    # 助言する権利をあげる！
    801061002: (_Option(guts=10, wiz=5), _Option(skill_hint=True)),

    # これも普通の努力です！
    801062001: (_Option(speed=10), _Option(power=10)),

    # これも普通のハプニング！？
    801062002: (_Option(stamina=5, guts=10), _Option(skill_hint=True)),

    # イクノ式万全メソッド
    801063001: (_Option(wiz=10), _Option(skill=30)),

    # イクノ式マネジメント論
    801063002: (_Option(stamina=20), _Option(skill_hint=True)),

    # 逃げられない選択？
    801064001: (_Option(vital=-15, guts=20), _Option(power=5, skill=15)),

    # ポジティブな逃げ
    801064002: (_Option(guts=15), _Option(skill_hint=True)),

    # 笑顔フォーエバー
    801065002: (_Option(speed=5, power=10), _Option(skill_hint=True)),

    # 燃えてきた！！
    801066002: (_Option(vital=15), _Option(skill_hint=True)),

    # 新しいもの、大好きです！
    801067001: (_Option(guts=10), _Option(vital=-10, stamina=20)),

    # 難しいこと、大好きです！
    801067002: (_Option(stamina=5, guts=10), _Option(skill_hint=True)),

    # あぁ、友情
    801068001: (_Option(yaruki_up=True, power=5), _Option(vital=10)),

    # 今日の格言！
    801069001: (_Option(vital=-10, power=20), _Option(vital=5, skill=10)),

    # いつか咲く、その日まで……
    801069002: (_Option(vital=5, stamina=5), _Option(skill_hint=True)),

    # 硝子の少女は学びたい
    801071001: (_Option(speed=10), _Option(vital=10, wiz=5)),

    # 硝子の少女は遊びたい
    801071002: (_Option(speed=10, wiz=10), _Option(skill_hint=True)),

    # 剛毅朴訥、仁に近し
    801072001: (_Option(speed=10), _Option(yaruki_up=True, power=5)),

    # 嗚呼、守りたい……！
    801072002: (_Option(stamina=10, power=10), _Option(skill_hint=True)),

    # #bff #Party!
    820024001: (_Option(power=10), _Option(speed=10)),

    # イクノ式サポートメソッド
    820025002: (_Option(wiz=15, skill_hint=True), _Option(wiz=15, skill_hint=True)),

    # 背、追いかけて
    820026001: (_Option(vital=5, wiz=3), _Option()),

    # ありがとうを言いたくて……！
    820027002: (_Option(power=5, skill_hint=True), _Option(wiz=5, skill_hint=True)),

    # 言葉はノンノン♪　ボディで語るの！
    820029001: (_Option(yaruki_up=True, skill_hint=True), _Option(power=10, guts=10), _Option(vital=30)),

    # ココ掘れ、ウインディ！
    820031001: (_Option(speed=10), _Option(vital=-5, skill=30)),

    # あこがれの……
    830018002: (_Option(vital=-10, wiz=20), _Option(wiz=5, skill=15)),

    # 本当に応えるべきは……
    830024002: (_Option(power=5, skill=10, skill_hint=True), _Option(stamina=5, skill=10, skill_hint=True)),

    # 少しでも近づけるように
    830025002: (_Option(vital=-10, speed=15), _Option(vital=-10, skill=20), _Option(vital=-10, skill_hint=True)),

    # 振り逃げランナウェイ
    830027001: (_Option(vital=-15, stamina=10, guts=10), _Option(vital=-15, guts=10, wiz=10)),

    # ラブ逃げエスケープ
    830027002: (_Option(vital=10, guts=5, wiz=5), _Option(vital=10, skill_hint=True)),

    # ポジティブ逃げネバギバ！
    830027003: (_Option(vital=-20, stamina=5, guts=5, skill_hint=True), _Option(vital=10, skill_hint=True)),

    # あなたにだけは絶対に
    830029003: (_Option(vital=-20, stamina=30, skill_hint=True), _Option(vital=5, guts=5, skill_hint=True)),

    # 学級委員長のすンげぇ特訓
    830031002: (_Option(yaruki_up=True, power=5), _Option(power=3, guts=3, wiz=3)),

    # あたし、勝ちたいンです！
    830031003: (_Option(yaruki_up=True, skill_hint=True), _Option(power=3, guts=3, wiz=3, skill_hint=True)),

    # つつましく！豪快に！
    830039001: (_Option(yaruki_up=True, speed=5), _Option(skill=10, skill_hint=True)),

    # ぶちかませ！お姫様ロード！
    830039003: (_Option(speed=15, guts=15, skill_hint=True), _Option(vital=25, skill=25)),

    # どぎまぎアフタヌーンティー
    830048001: (_Option(vital=10, yaruki_up=True), _Option(wiz=10, skill=15, skill_hint=True)),

    # いきなりマーダーミステリー！　その1
    830055001: (_Option(wiz=5, skill=10), _Option(vital=10)),

    # いきなりマーダーミステリー！　その2
    830055002: (_Option(wiz=5, skill_hint=True), _Option(vital=5, skill=10)),

    # 魅惑の招待状
    830056001: (_Option(power=10), _Option(guts=10)),

    # 舞踏家のプライド
    830056002: (_Option(vital=-5, stamina=10, power=5, skill=5), _Option(vital=15, skill=5)),

    # なかよし☆こよしちゃん　～探求編～
    830059001: (_Option(skill=10), _Option(yaruki_up=True)),
}
