import auto_derby
from auto_derby import single_mode


class Plugin(auto_derby.Plugin):
    def install(self) -> None:
        class Race(auto_derby.config.single_mode_race_class):
            def score(self, ctx: single_mode.Context) -> float:
                ret = super().score(ctx)
                if self.name in {
                    '菊花賞',  # to override 秋天
                }:
                    ret += 200
                elif self.name in {
                    'ホープフルステークス',
                    '皐月賞',
                    '東京優駿（日本ダービー）',
                    '宝塚記念',
                    '天皇賞（秋）',
                    'ジャパンカップ',
                    '有馬記念',
                    '大阪杯',
                    '天皇賞（春）',
                }:
                    ret += 100
                return ret

        auto_derby.config.single_mode_race_class = Race


auto_derby.plugin.register(__name__, Plugin())
