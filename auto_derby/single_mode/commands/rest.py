# -*- coding=UTF-8 -*-
# pyright: strict

from __future__ import annotations

import random

from ... import action, templates
from ...scenes.single_mode.command import CommandScene
from .. import Context, Training
from .command import Command
from .globals import g


class RestCommand(Command):
    def execute(self, ctx: Context) -> None:
        g.on_command(ctx, self)
        CommandScene.enter(ctx)
        x_offset, y_offset = random.randint(-10, 100), random.randint(-50, 20)
        action.tap_image(
            templates.SINGLE_MODE_REST, x=x_offset, y=y_offset
        )

    def score(self, ctx: Context) -> float:
        return g.rest_score(ctx)


def default_score(ctx: Context) -> float:
    t = Training.new()
    t.vitality = 50 / ctx.max_vitality
    return t.score(ctx)


g.rest_score = default_score
