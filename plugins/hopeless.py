import auto_derby
from auto_derby import single_mode


class Plugin(auto_derby.Plugin):
    def install(self) -> None:
        class Race(auto_derby.config.single_mode_race_class):
            def score(self, ctx: single_mode.Context) -> float:
                ret = super().score(ctx)
                if self.name == "ホープフルステークス":
                    ret += 100
                return ret

        auto_derby.config.single_mode_race_class = Race


auto_derby.plugin.register(__name__, Plugin())
