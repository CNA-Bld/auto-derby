from abc import ABC, abstractmethod

from auto_derby.single_mode import Context, Training


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
