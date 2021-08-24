from typing import Tuple

import auto_derby
from auto_derby import single_mode


class Plugin(auto_derby.Plugin):

    def install(self) -> None:
        class Race(auto_derby.config.single_mode_race_class):
            def style_scores(self, ctx: single_mode.Context) -> Tuple[float, float, float, float]:
                ret = super().style_scores(ctx)
                return 0, 0, 0, max(ret)

        auto_derby.config.single_mode_race_class = Race


auto_derby.plugin.register(__name__, Plugin())
