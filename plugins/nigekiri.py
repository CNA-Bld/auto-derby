from typing import Tuple, Iterator

import auto_derby
from auto_derby import single_mode
from auto_derby.constants import RuningStyle


class Plugin(auto_derby.Plugin):

    def install(self) -> None:
        class Race(auto_derby.config.single_mode_race_class):
            def style_scores_v2(self, ctx: single_mode.Context) -> Iterator[Tuple[RuningStyle, float]]:
                ret = super().style_scores_v2(ctx)
                return [(RuningStyle.LEAD, max([i[1] for i in ret]))]

        auto_derby.config.single_mode_race_class = Race


auto_derby.plugin.register(__name__, Plugin())
