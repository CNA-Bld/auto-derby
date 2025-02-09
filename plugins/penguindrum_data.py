import typing

from plugins.penguindrum_models import _Option

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
    # 聖夜に並んで走るため
    501006800: (_Option(skill=30), _Option(speed=10, power=5)),

    # みんなのオグリキャップ
    501006801: (_Option(skill_hint=True), _Option(power=10, guts=5)),

    # 先取り大人のクリスマス！？
    501006802: (_Option(vital=20, yaruki_up=True, skill_hint=True), _Option(speed=10, wiz=20, skill_hint=True)),

    # 心に咲く、熱
    501017800: (_Option(speed=10, power=10), _Option(skill_hint=True)),

    # 経験を授けよ
    501017801: (_Option(power=20), _Option(skill_hint=True)),

    # 鮮やかな記憶
    501017802: (_Option(stamina=10, guts=10), _Option(skill=40)),

    # ダンスレッスン
    501019506: (_Option(power=10), _Option(wiz=10)),

    # 萌えは無限の可能性
    501019510: (_Option(speed=10), _Option(stamina=10)),

    # 公式が最大手すぐる件
    501019511: (_Option(power=5, guts=5), _Option(vital=5, wiz=5)),

    # "推し"えて、デジタル先生！
    501019513: (_Option(wiz=20), _Option(power=20)),

    # あなたの背中を"推し"たくて……
    501019514: (_Option(speed=10, power=10), _Option(stamina=10, guts=10)),

    # "推し"みない愛を推しに！
    501019515: (_Option(stamina=10, skill=15), _Option(power=20)),

    # 毎日がコラボカフェ
    501019520: (_Option(skill_hint=True), _Option(skill_hint=True)),

    # ウマ娘ちゃんクイズ☆～関係性編～
    501019524: (_Option(speed=15, skill_hint=True), _Option(speed=5)),

    # ウマ娘ちゃんクイズ☆～嗜好編～
    501019525: (_Option(stamina=5), _Option(stamina=15, skill_hint=True)),

    # ウマ娘ちゃんクイズ☆～ルーツ編～
    501019526: (_Option(power=15, skill_hint=True), _Option(power=5)),

    # 推し事探訪　～入門編～
    501019702: (_Option(stamina=10), _Option(speed=10)),

    # 推し事探訪　～極編～
    501019703: (_Option(stamina=10), _Option(wiz=10)),

    # 推し事探訪　～免許皆伝編～
    501019704: (_Option(guts=10), _Option(speed=10), _Option(skill=30)),

    # ヲタク最高すぎるんだが？
    501019705: (_Option(speed=10), _Option(guts=10)),

    # 推し接近アラート、発令！？
    501019706: (_Option(power=10), _Option(vital=10)),

    # もうひとつの星
    501023800: (_Option(vital=-10, speed=30, guts=10, skill_hint=True), _Option(vital=15, skill=20, skill_hint=True)),

    # お願い、お姉さん！
    501023801: (_Option(speed=15), _Option(stamina=15)),

    # 助っ人参上！
    501023802: (_Option(stamina=5, skill=15), _Option(skill_hint=True)),

    # 勝てなかったけど……
    501024725: (_Option(vital=-20, guts=9, skill=52), _Option()),

    # ダンスレッスン
    501025506: (_Option(wiz=10), _Option(stamina=10)),

    # 漆黒のバリスタ
    501025510: (_Option(stamina=10), _Option(speed=10)),

    # ドキドキ怪奇探索ツアー
    501025511: (_Option(power=10), _Option(vital=-10, guts=20)),

    # ズット、ズット、待ッテイタ……
    501025513: (_Option(power=20), _Option(speed=20)),

    # 影ナル者
    501025514: (_Option(wiz=20), _Option(speed=10, guts=10)),

    # 夢幻ナル世界ノ中デ
    501025515: (_Option(power=20), _Option(guts=20)),

    # ライ　ホウ　シャ
    501025520: (_Option(stamina=10, skill=15), _Option(skill_hint=True)),

    # 私だけのコーヒー
    501025702: (_Option(guts=10), _Option(stamina=5, skill=15)),

    # アナタだけの好み
    501025703: (_Option(speed=10), _Option(wiz=10)),

    # 2人だけのフレーバー
    501025704: (_Option(stamina=10), _Option(power=10), _Option(speed=5, stamina=5)),

    # カフェはカフェでも
    501025705: (_Option(wiz=10), _Option(stamina=10)),

    # それは百鬼夜行のように
    501025706: (_Option(guts=10), _Option(power=10)),

    # ダンスレッスン
    501028506: (_Option(power=10), _Option(wiz=10)),

    # レッスン☆サバイバル生活
    501028510: (_Option(vital=-10, stamina=10, guts=10), _Option(vital=-10, stamina=20)),

    # 集まれ☆お料理好き
    501028511: (_Option(power=10), _Option(guts=10)),

    # 届けボーノ！
    501028513: (_Option(speed=20), _Option(guts=20)),

    # 大きくな～れ！
    501028514: (_Option(wiz=10, skill=15), _Option(vital=15)),

    # 堂々と行こう！
    501028515: (_Option(power=20), _Option(stamina=20)),

    # 腹が減っては巡回できぬ☆
    501028520: (_Option(vital=20), _Option(skill_hint=True)),

    # お夜食ちゃんこの効能
    501028524: (_Option(vital=70), _Option(vital=40, yaruki_up=True)),

    # はっけよい、陶芸教室！
    501028702: (_Option(wiz=10), _Option(power=10)),

    # はっけよい、お弁当！
    501028703: (_Option(guts=10), _Option(power=10)),

    # はっけよい、好き！
    501028704: (_Option(speed=10), _Option(skill=30), _Option(stamina=5, guts=5)),

    # 宇宙の食卓
    501028705: (_Option(wiz=10), _Option(vital=10)),

    # みんなでビッグチャレンジ！
    501028706: (_Option(speed=5, power=5), _Option(stamina=5, skill=15)),

    # ライスのトリート大作戦！
    501030800: (_Option(skill_hint=True), _Option(stamina=20)),

    # ライスのヴァンパイア退治大作戦！
    501030801: (_Option(vital=15), _Option(speed=10, power=10)),

    # ライスのトリック大作戦！
    501030802: (_Option(wiz=20), _Option(skill_hint=True)),

    # ダンスレッスン
    501037506: (_Option(speed=10), _Option(wiz=10)),

    # 天道の守護者
    501037510: (_Option(stamina=10), _Option(power=10)),

    # 教え導くためならば
    501037511: (_Option(speed=10), _Option(guts=10)),

    # 誇りをまとうに相応しく
    501037513: (_Option(power=20), _Option(skill=40)),

    # 闇の中にうごめく影は……
    501037514: (_Option(speed=10, guts=10), _Option(stamina=20)),

    # 賭するは名誉
    501037515: (_Option(guts=20), _Option(wiz=20)),

    # 空飛ぶガイダンス
    501037520: (_Option(speed=5, stamina=5, power=5), _Option(skill_hint=True)),

    # トレンドを追って
    501037702: (_Option(wiz=10), _Option(stamina=10)),

    # 和の心に触れて
    501037703: (_Option(guts=10), _Option(speed=10)),

    # 馴染みゆく日々の中で
    501037704: (_Option(power=10), _Option(guts=10), _Option(stamina=10)),

    # 誠意を貴方へ
    501037705: (_Option(speed=10), _Option(wiz=10)),

    # 追憶のFreizeitpark
    501037706: (_Option(power=10), _Option(stamina=10)),

    # ダンスレッスン
    501039506: (_Option(power=10), _Option(wiz=10)),

    # じゃじゃウマ娘のパーティー
    501039510: (_Option(speed=5, power=5), _Option(wiz=10)),

    # マスコット対決！
    501039511: (_Option(speed=10), _Option(power=10)),

    # 決意はドレスにこめて
    501039513: (_Option(speed=20), _Option(guts=20)),

    # 受け止めます、姫のパワーで！
    501039514: (_Option(stamina=10, power=10), _Option(wiz=10, skill=15)),

    # いつか一流のプリンセスに
    501039515: (_Option(power=20), _Option(stamina=10, wiz=10)),

    # 王子様の優雅なる休日
    501039520: (_Option(guts=15), _Option(skill_hint=True)),

    # 元ガキ大将の風格
    501039702: (_Option(stamina=5, skill=15), _Option(power=10)),

    # 元ガキ大将の背中
    501039703: (_Option(power=10), _Option(wiz=10)),

    # 元ガキ大将の誓い
    501039704: (_Option(speed=10), _Option(stamina=10), _Option(power=10)),

    # 努力の円舞曲
    501039705: (_Option(power=10), _Option(guts=10)),

    # この胸にあふれる想いは！
    501039706: (_Option(power=5, guts=5), _Option(speed=10)),

    # モデルのお仕事
    501040524: (_Option(vital=-15, skill=40), _Option(yaruki_up=True)),

    # シチーガールの今の気分♪
    501040800: (_Option(speed=20), _Option(vital=15)),

    # 金色の佳景、極まる
    501040801: (_Option(stamina=10, power=10), _Option(skill_hint=True)),

    # 本番前の、静かな余談
    501040802: (_Option(power=20), _Option(skill_hint=True)),

    # Search  or Mommy
    501045800: (_Option(wiz=20), _Option(skill_hint=True)),

    # Accident or Ghost
    501045801: (_Option(stamina=10, skill=15), _Option(power=20)),

    # Curse or Wrap
    501045802: (_Option(skill_hint=True), _Option(speed=20)),

    # ダンスレッスン
    501048506: (_Option(guts=10), _Option(power=10)),

    # 激辛上等コールバトル！
    501048510: (_Option(guts=10), _Option(power=10)),

    # 少しずつ伸びてるから！
    501048511: (_Option(wiz=10), _Option(speed=5, stamina=5)),

    # ラメの輝きに託して
    501048513: (_Option(guts=20), _Option(speed=20)),

    # 基本フリータイムっしょ！
    501048514: (_Option(wiz=20), _Option(power=20)),

    # 勝利の味ってヤツ！
    501048515: (_Option(stamina=10, skill=15), _Option(guts=10, wiz=10)),

    # 盛って盛って、めっちゃ盛んぞー！
    501048520: (_Option(stamina=10, skill=15), _Option(skill_hint=True)),

    # 大事なのは今っしょ！
    501048702: (_Option(wiz=10), _Option(stamina=10)),

    # ほんの少しのキッカケ
    501048703: (_Option(power=10), _Option(wiz=10)),

    # 背伸びから始まること
    501048704: (_Option(guts=10), _Option(power=10), _Option(wiz=10)),

    # ギャル、絵画を語る
    501048705: (_Option(speed=10), _Option(power=10)),

    # まっ、流行ってすぐ変わるし！
    501048706: (_Option(speed=10), _Option(guts=10)),

    # 私がお守りです
    501056800: (_Option(stamina=20), _Option(skill_hint=True)),

    # 今だけ！パワースポット
    501056801: (_Option(stamina=10, power=10), _Option(wiz=20)),

    # フクキタル来れば福来たる
    501056802: (_Option(speed=20), _Option(speed=7, stamina=7, power=7)),

    # ダンスレッスン
    501059506: (_Option(power=10), _Option(guts=10)),

    # 嵐の大特訓
    501059510: (_Option(vital=-10, stamina=20), _Option(power=10)),

    # きゅんきゅんティータイム！？
    501059511: (_Option(guts=10), _Option(wiz=5, skill=15)),

    # メジロの色
    501059513: (_Option(stamina=20), _Option(power=20)),

    # 香りの魔術師
    501059514: (_Option(wiz=20), _Option(guts=10, skill=15)),

    # ワンクッション親子
    501059515: (_Option(speed=20), _Option(power=20)),

    # ヤミナベス女王杯！？
    501059520: (_Option(speed=15), _Option(skill_hint=True)),

    # 今のアタシは……
    501059702: (_Option(power=10), _Option(wiz=10)),

    # アタシ、やってみる
    501059703: (_Option(stamina=10), _Option(wiz=10)),

    # 願い、花火に寄せて
    501059704: (_Option(speed=10), _Option(stamina=10), _Option(power=10)),

    # ゆたかなる友情
    501059705: (_Option(wiz=10), _Option(guts=10)),

    # 夕陽にときめいて
    501059706: (_Option(speed=10), _Option(wiz=10)),

    # #あなただけのカワイイ
    801038001: (_Option(speed=5, wiz=10), _Option(speed=10, power=5)),

    # #カワイイフォーユー☆
    801038002: (_Option(skill=15), _Option(skill_hint=True)),

    # スマホって時間泥棒じゃん？
    801048001: (_Option(yaruki_up=True, speed=5), _Option(stamina=10)),

    # レビューって半分賭けじゃん？
    801048002: (_Option(vital=10, yaruki_up=True), _Option(skill_hint=True)),

    # 夕暮れにひと勝負
    801049001: (_Option(vital=15), _Option(guts=15)),

    # 夕暮れの独り飯
    801049002: (_Option(skill_hint=True), _Option(skill_hint=True)),

    # 教えてやろうか？
    801070001: (_Option(vital=-5, stamina=20), _Option(wiz=10)),

    # 助けてやろうか？
    801070002: (_Option(wiz=5, skill_hint=True), _Option(skill=15)),

    # ずうっと、つやつや、魔法の花
    830034002: (_Option(stamina=5, power=10), _Option(vital=15, power=5)),

    # 奏でようWINNING!
    830062001: (_Option(guts=10, skill_hint=True), _Option(speed=10, skill_hint=True)),

    # 読書少女と秘密の作戦会議
    830065002: (_Option(stamina=5, skill_hint=True), _Option(speed=5, skill_hint=True), _Option(wiz=30)),

    # ステータス『つまらない？』
    830066001: (_Option(speed=10, skill_hint=True), _Option(wiz=15)),

    # 素直トレーニング！
    830073002: (_Option(power=10, skill_hint=True), _Option(stamina=10, skill_hint=True)),

    # キラッと輝くマーベラス☆
    830074002: (_Option(vital=10), _Option(skill_hint=True)),

    # マーベラス売りの少女
    400004324: (_Option(vital=10), _Option(skill_hint=True)),

    # 家族（？）でショッピング！
    400004325: (_Option(skill=24), _Option(skill_hint=True)),

    # 凸凹コンビ
    400004326: (_Option(power=6, guts=6), _Option(skill_hint=True)),

    # ワールドワイド・ウインディ
    400004327: (_Option(speed=6, guts=6), _Option(skill_hint=True)),

    # ベガとスピカ
    400004328: (_Option(speed=6, wiz=6), _Option(skill_hint=True)),

    # 『退学』を賭けた勝負
    400004329: (_Option(stamina=6, wiz=6), _Option(skill_hint=True)),

    # パワフル最強シンデレラ！
    400004330: (_Option(yaruki_up=True), _Option(skill_hint=True)),

    # ヴィクトリー倶楽部、参上！
    400004331: (_Option(stamina=6, wiz=6), _Option(skill_hint=True)),

    # 甘えたがりのお年頃
    400004332: (_Option(speed=6, wiz=6), _Option(skill_hint=True)),

    # カワイイを守りたい！
    400004333: (_Option(stamina=6, power=6), _Option(skill_hint=True)),

    # 語り合いたい！
    400004334: (_Option(stamina=6, guts=6), _Option(skill_hint=True)),

    # 同じ傘の下で
    400004335: (_Option(speed=6, guts=6), _Option(skill_hint=True)),

    # ゴルシちゃん主催！人狼は誰だ！？
    400004336: (_Option(power=6, wiz=6), _Option(skill_hint=True)),

    # ドキドキフルーツフェス
    400004337: (_Option(stamina=6, power=6), _Option(skill_hint=True)),

    # サプライズ大作戦！
    400004338: (_Option(yaruki_up=True), _Option(skill_hint=True)),

    # ひとり暮らしの生活
    400004339: (_Option(power=6, guts=6), _Option(skill_hint=True)),

    # アグネスデジタル、爆発す
    400004341: (_Option(yaruki_up=True), _Option(skill_hint=True)),

    # 『全力』&『普通』ダイエット！
    400004342: (_Option(stamina=6, guts=6), _Option(skill_hint=True)),

    # タイキとパールと外国語
    400004343: (_Option(speed=6, wiz=6), _Option(skill_hint=True)),

    # タマモのゲームセンター奮闘記
    400004344: (_Option(guts=6, wiz=6), _Option(skill_hint=True)),

    # アルダンからは逃げ切れない
    400004345: (_Option(speed=6, guts=6), _Option(skill_hint=True)),

    # 委員たちの井戸端会議
    400004346: (_Option(speed=6, power=6), _Option(skill_hint=True)),

    # 意外な美化委員
    400004347: (_Option(power=6, wiz=6), _Option(skill_hint=True)),

    # マルゼンさんへの気持ち
    400004348: (_Option(skill=24), _Option(skill_hint=True)),

    # 怖くないって怖いです
    400004349: (_Option(stamina=6, guts=6), _Option(skill_hint=True)),

    # 目が離せないお嬢様たち
    400004350: (_Option(guts=6, wiz=6), _Option(skill_hint=True)),

    # ゴルシを治せ！？
    400004351: (_Option(speed=6, power=6), _Option(skill_hint=True)),

    # じいちゃん子たちの集い
    400004352: (_Option(stamina=6, wiz=6), _Option(skill_hint=True)),

    # ふたりと宿根草
    400004353: (_Option(speed=6, power=6), _Option(skill_hint=True)),

    # 名探偵のボクにお任せ！
    400004354: (_Option(speed=6, stamina=6), _Option(skill_hint=True)),

    # キセキのカタチ
    501005800: (_Option(guts=10), _Option(vital=15, yaruki_up=True, skill=10)),

    # 目に映る君は
    501005802: (_Option(wiz=10), _Option(skill_hint=True)),

    # 新たな魅力を……
    501015802: (_Option(skill_hint=True), _Option(power=10)),

    # 『リーニュ・ドロワット』の前に
    501020800: (_Option(vital=30), _Option(wiz=10)),

    # みんなには、一応秘密で
    501020802: (_Option(stamina=15), _Option(skill_hint=True)),

    # ダンスレッスン
    501021506: (_Option(power=10), _Option(wiz=10)),

    # 浪花魂みせたるわい！
    501021510: (_Option(speed=5, power=5), _Option(stamina=10)),

    # これなんぼやと思う？
    501021511: (_Option(power=10), _Option(stamina=10)),

    # 稲妻ハート
    501021513: (_Option(guts=20), _Option(vital=15)),

    # たこパ、やったるで！
    501021514: (_Option(speed=10, power=10), _Option(guts=10, wiz=10)),

    # ウチに似合う服
    501021515: (_Option(speed=20), _Option(power=10, guts=10)),

    # 大人ってなんなん？
    501021520: (_Option(speed=5, power=10), _Option(skill_hint=True)),

    # 姉ちゃんにまかしとき！
    501021702: (_Option(power=10), _Option(stamina=10)),

    # 行ったれ！牧場体験！
    501021703: (_Option(vital=10), _Option(stamina=10)),

    # 助け、助けられ
    501021704: (_Option(guts=10), _Option(wiz=10), _Option(speed=10)),

    # おとろしないで、おいなりさん
    501021705: (_Option(speed=10), _Option(guts=10)),

    # 恐怖のネバネバ
    501021706: (_Option(wiz=10), _Option(power=10)),

    # ダンスレッスン
    501022506: (_Option(power=10), _Option(wiz=10)),

    # 殿下の華麗なるたしなみ
    501022510: (_Option(power=10), _Option(wiz=10)),

    # 殿下と刺激的なお茶会
    501022511: (_Option(speed=5, guts=5), _Option(stamina=5, power=5)),

    # 約束のシャムロック
    501022513: (_Option(power=20), _Option(speed=20)),

    # よしよし殿下
    501022514: (_Option(stamina=10, guts=10), _Option(wiz=20)),

    # 殿下と映画鑑賞会
    501022515: (_Option(power=10, guts=10), _Option(wiz=10, skill=15)),

    # 遠くの地より花は来りて
    501022520: (_Option(stamina=10, skill=15), _Option(skill_hint=True)),

    # こういうの、ロマンでしょう？
    501022702: (_Option(wiz=10), _Option(power=10)),

    # 異国の地ならなんでも
    501022703: (_Option(guts=10), _Option(speed=10)),

    # 大儀であります
    501022704: (_Option(stamina=10), _Option(wiz=10), _Option(power=10)),

    # 殿下がバザーにやってきた！
    501022705: (_Option(wiz=10), _Option(power=10)),

    # 殿下、推し文化に触れる
    501022706: (_Option(speed=10), _Option(guts=10)),

    # Not Found
    501026801: (_Option(vital=10, speed=10, stamina=15), _Option(vital=10, skill_hint=True)),

    # ダンスレッスン
    501033506: (_Option(wiz=10), _Option(speed=10)),

    # 必殺・アヤベさん
    501033510: (_Option(vital=-10, power=20), _Option(guts=10)),

    # 同室シスターにはかなわない
    501033511: (_Option(speed=10), _Option(vital=5, power=5)),

    # 想いよ届け
    501033513: (_Option(power=20), _Option(stamina=20)),

    # 静かに通じて
    501033514: (_Option(wiz=20), _Option(speed=20)),

    # たった1つの使命
    501033515: (_Option(power=10, guts=10), _Option(speed=20)),

    # 雲の向こう、宙のかなた
    501033520: (_Option(power=10, skill=15), _Option(skill_hint=True)),

    # それは、当たり前
    501033702: (_Option(power=10), _Option(wiz=10)),

    # 言葉+……
    501033703: (_Option(vital=10), _Option(speed=10)),

    # ようやく、受け取るモノ
    501033704: (_Option(guts=10), _Option(stamina=10), _Option(wiz=10)),

    # もふもふ審美眼
    501033705: (_Option(wiz=10), _Option(power=10)),

    # 夢で見た光景
    501033706: (_Option(stamina=10), _Option(speed=10)),

    # その時間は贈り物
    501037801: (_Option(vital=10, speed=15, wiz=10), _Option(vital=10, skill_hint=True)),

    # 見習いお姉さん
    501051510: (_Option(wiz=10), _Option(vital=10)),

    # メイド・イン・フラワー
    501051511: (_Option(speed=10), _Option(yaruki_up=True, guts=5)),

    # 色形、重ねて私
    501051513: (_Option(speed=20), _Option(vital=10, wiz=10)),

    # お姉さんらしく
    501051514: (_Option(power=20), _Option(wiz=10, skill=15)),

    # 小さな体に大きな愛
    501051515: (_Option(stamina=20), _Option(guts=20)),

    # 凜と咲く
    501051520: (_Option(vital=5, stamina=5, power=5), _Option(skill_hint=True)),

    # フラワーの知恵袋
    501051702: (_Option(stamina=10), _Option(wiz=10)),

    # フラワー・リラクゼーション
    501051703: (_Option(vital=5, speed=5), _Option(vital=5, guts=5)),

    # フラワー日和
    501051704: (_Option(stamina=10), _Option(speed=10), _Option(wiz=10)),

    # 寄り添う花
    501051705: (_Option(guts=10), _Option(speed=10)),

    # 近日公開予定
    501051706: (_Option(wiz=10), _Option(power=10)),

    # ダンスレッスン
    501062506: (_Option(guts=10), _Option(wiz=10)),

    # 恋は焼きサバの味
    501062510: (_Option(stamina=10), _Option(yaruki_up=True, speed=5)),

    # シュビビッと解決！
    501062511: (_Option(power=10), _Option(vital=5, skill=15)),

    # 『普通』の先へ
    501062513: (_Option(power=20), _Option(guts=20)),

    # 神父マチタンと結婚式
    501062514: (_Option(wiz=20), _Option(stamina=10, skill=15)),

    # 敏腕看板娘、誕生
    501062515: (_Option(stamina=10, power=10), _Option(guts=10, wiz=10)),

    # お待ちかねのランチ
    501062520: (_Option(yaruki_up=True, stamina=10), _Option(skill_hint=True)),

    # 私だってやる時は……！？
    501062702: (_Option(stamina=10), _Option(wiz=10)),

    # おもてなしの反対
    501062703: (_Option(guts=10), _Option(stamina=10)),

    # いつも、いつまでも！
    501062704: (_Option(wiz=10), _Option(speed=10), _Option(guts=10)),

    # 目指せ！頼れるお姉ちゃん
    501062705: (_Option(power=10), _Option(guts=10)),

    # マチタンの初代帽子
    501062706: (_Option(stamina=5, wiz=5), _Option(speed=10)),

    # ダンスレッスン
    501067506: (_Option(speed=10), _Option(power=10)),

    # しゃっくりSOS
    501067510: (_Option(stamina=10), _Option(power=10)),

    # 禁断のブレンド
    501067511: (_Option(wiz=10), _Option(yaruki_up=True, stamina=5)),

    # 剛なるダイヤは真綿の中に
    501067513: (_Option(guts=20), _Option(stamina=20)),

    # スイーピー5☆入団テスト！
    501067514: (_Option(speed=20), _Option(power=10, skill=15)),

    # サトノ家として、ウマ娘として
    501067515: (_Option(wiz=20), _Option(stamina=10, power=10)),

    # 大きすぎる志
    501067520: (_Option(power=10, guts=5), _Option(skill_hint=True)),

    # 裏路地アドベンチャー
    501067702: (_Option(wiz=10), _Option(power=10)),

    # フレッシュ！
    501067703: (_Option(speed=10), _Option(stamina=10)),

    # ハートビート・エキサイト
    501067704: (_Option(stamina=10), _Option(guts=10), _Option(wiz=10)),

    # コンビニ前にはご注意を
    501067705: (_Option(stamina=10), _Option(guts=10)),

    # たくさんの彩りの中で
    501067706: (_Option(speed=10), _Option(guts=10)),

    # ダンスレッスン
    501068506: (_Option(guts=10), _Option(wiz=10)),

    # 魔女さんとキタサン
    501068510: (_Option(stamina=10), _Option(yaruki_up=True, speed=5)),

    # 先輩と！
    501068511: (_Option(speed=10), _Option(vital=10)),

    # フォーゲットミーノット！
    501068513: (_Option(stamina=20), _Option(speed=20)),

    # 陰に日なたに
    501068514: (_Option(speed=10, wiz=10), _Option(power=20)),

    # かわいいの才能っ！
    501068515: (_Option(stamina=10, wiz=10), _Option(guts=20)),

    # ちょいとドラマへの出演も目指し
    501068520: (_Option(speed=5, guts=10), _Option(skill_hint=True)),

    # 緊急開店！キタちゃんマッサージ
    501068524: (_Option(speed=20), _Option(vital=10, guts=10), _Option(skill_hint=True)),

    # 寄ってらっしゃい見てらっしゃい！
    501068702: (_Option(stamina=10), _Option(wiz=10)),

    # 妖怪変化もなんのその！
    501068703: (_Option(speed=5, stamina=5), _Option(guts=10)),

    # 主役はみなさまお祭りワッショイ！
    501068704: (_Option(wiz=10), _Option(power=10), _Option(speed=10)),

    # ほろ甘の思い出
    501068705: (_Option(stamina=10), _Option(guts=5, wiz=5)),

    # あなたの声なら
    501068706: (_Option(wiz=10), _Option(power=10)),

    # ダンスレッスン
    501069506: (_Option(wiz=10), _Option(power=10)),

    # 最近流行りのブティックで
    501069510: (_Option(speed=10), _Option(wiz=10)),

    # 風紀委員長賞、受賞者ですから
    501069511: (_Option(vital=5, power=5), _Option(stamina=10)),

    # 『そこにあるのが、日常である』
    501069513: (_Option(power=10, wiz=10), _Option(stamina=20)),

    # 『想いはバブリーに包め』
    501069514: (_Option(guts=10, skill=15), _Option(wiz=20)),

    # 『花は桜木、ウマ娘は……』
    501069515: (_Option(power=20), _Option(speed=20)),

    # どすこい！決まり手指導！？
    501069520: (_Option(speed=10, guts=5), _Option(skill_hint=True)),

    # チヨノオーは頼られたい
    501069702: (_Option(guts=10), _Option(stamina=10)),

    # 頼りになる人ツアー？
    501069703: (_Option(power=10), _Option(speed=10)),

    # 頼られる意味
    501069704: (_Option(wiz=10), _Option(speed=10), _Option(power=10)),

    # カーレースフレンド
    501069705: (_Option(speed=10), _Option(stamina=10)),

    # ウマ娘演歌大会！
    501069706: (_Option(power=10), _Option(speed=5, guts=5)),

    # ダンスレッスン
    501071506: (_Option(speed=10), _Option(power=10)),

    # 前門の母、後門の姉
    501071510: (_Option(speed=10), _Option(stamina=10)),

    # 乙女の語らい
    501071511: (_Option(yaruki_up=True, guts=5), _Option(wiz=10)),

    # 信じ合うこと
    501071513: (_Option(speed=20), _Option(guts=20)),

    # ガラスのワルツ
    501071514: (_Option(power=10, guts=10), _Option(wiz=20)),

    # 思い出光る昼下がり
    501071515: (_Option(stamina=20), _Option(wiz=20)),

    # 体が勝手に……？
    501071520: (_Option(speed=10, skill=15), _Option(skill_hint=True)),

    # アルダンの寄り道講座・初級編
    501071702: (_Option(power=10), _Option(wiz=10)),

    # アルダンの寄り道講座・追憶編
    501071704: (_Option(speed=10), _Option(wiz=10), _Option(stamina=10)),

    # 人と観る映画
    501071705: (_Option(wiz=10), _Option(speed=10)),

    # 意外なたくましさ？
    501071706: (_Option(stamina=10), _Option(guts=10)),

    # ダンスレッスン
    501074506: (_Option(power=10), _Option(speed=10)),

    # 輪の中でも変わらずに
    501074510: (_Option(power=10), _Option(yaruki_up=True, skill=15)),

    # 未来が分かる魔法かも？
    501074511: (_Option(vital=-10, stamina=20), _Option(speed=5, skill=15)),

    # 蒼き想いを秘めて
    501074513: (_Option(stamina=20), _Option(wiz=20)),

    # ブライトお嬢様は怖いものなし？
    501074514: (_Option(guts=10, skill=15), _Option(speed=20)),

    # こころ、穏やかに
    501074515: (_Option(stamina=10, guts=10), _Option(power=20)),

    # お世話できますもの～！
    501074520: (_Option(speed=5, power=10), _Option(skill_hint=True)),

    # ブライト・イン・アンダーワールド
    501074702: (_Option(stamina=10), _Option(wiz=10)),

    # ブライト・イン・ニューワールド
    501074703: (_Option(guts=10), _Option(speed=10)),

    # ブライト・イン・ワンダーワールド
    501074704: (_Option(stamina=10), _Option(power=10), _Option(wiz=10)),

    # 支えられて、見守られて
    501074705: (_Option(speed=10), _Option(wiz=10)),

    # 招き猫さんを救え！
    501074706: (_Option(guts=10), _Option(power=10)),

    # 不器用なトライアングラム
    801033001: (_Option(power=15), _Option(vital=10)),

    # 孤高のケフェウス
    801033002: (_Option(skill_hint=True), _Option(wiz=10)),

    # 喧嘩だワッショイ
    801034001: (_Option(vital=-5, power=15), _Option(yaruki_up=True, guts=5)),

    # 神輿だワッショイ
    801034002: (_Option(skill=15), _Option(skill_hint=True)),

    # のんびり、ゆったり。
    801074001: (_Option(stamina=15, guts=5), _Option(speed=15, power=5)),

    # しっかり、じっくり。
    801074002: (_Option(vital=10, skill_hint=True), _Option(wiz=20)),

    # きっちり、点検！
    801077001: (_Option(vital=20), _Option(vital=-10, speed=25)),

    # しっかり、努力！
    801077002: (_Option(stamina=10), _Option(skill_hint=True)),

    # 人情ラプソディ
    820022001: (_Option(yaruki_up=True, speed=5), _Option(vital=10, stamina=5)),

    # 商いの道は人の道
    820022002: (_Option(speed=10, skill=10, skill_hint=True), _Option(stamina=10, skill=10, skill_hint=True)),

    # 千里の道も筋トレから！
    820040002: (_Option(vital=25), _Option(stamina=10, power=5, skill_hint=True)),

    # あいさつバクシン運動です！！
    820042001: (_Option(vital=-10, speed=30), _Option(vital=-10, skill=30)),

    # #Currenみつけた
    820044001: (_Option(speed=20), _Option(skill=10, skill_hint=True)),

    # What is ウマドル？
    820045001: (_Option(skill_hint=True), _Option(vital=10, power=5)),

    # 頑張れる秘訣は……！
    820046002: (_Option(wiz=10, skill_hint=True), _Option(speed=10, skill_hint=True)),

    # アヤベさんは挫けない
    830077003: (_Option(power=15, wiz=10, skill_hint=True), _Option(speed=15, skill=30)),

    # 覇王の危機！？
    830079001: (_Option(vital=10), _Option(stamina=5, skill_hint=True)),

    # 距離感とかあるし
    830084001: (_Option(speed=10, stamina=5), _Option(vital=10)),

    # ヲタクの責務
    830085002: (_Option(stamina=15, skill_hint=True), _Option(wiz=15, skill_hint=True)),

    # 期待をその背に！
    830086002: (_Option(vital=-10, speed=15, stamina=15, skill_hint=True), _Option(vital=20, skill=10)),

    # わたくし、捜しますわ～
    830087001: (_Option(yaruki_up=True, stamina=10), _Option(vital=10, wiz=10)),

    # マーベラス☆ダイブ！！
    830089001: (_Option(wiz=10, skill=10), _Option(vital=-10, guts=25)),

    # 重なるハイとロー
    830092001: (_Option(speed=10, power=10), _Option(skill_hint=True)),

    # 届かない『キモチ』
    830093001: (_Option(stamina=10, skill_hint=True), _Option(power=10, skill_hint=True)),
}
