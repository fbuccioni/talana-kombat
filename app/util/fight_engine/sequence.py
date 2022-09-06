import random

from .base import FightEngine
from .movement import FightMovement
from .participant import FightParticipant


class FightSequence(FightEngine):
    movement: FightMovement
    participant: FightParticipant
    orientation: str

    def __init__(self, movement: FightMovement, participant: FightParticipant, orientation: str):
        self.movement = movement
        self.participant = participant
        self.orientation = orientation

    def damage(self):
        super_move = self.movement.has_super_move_from(self.participant.super_moves)
        if super_move:
            return super_move.damage

        if self.movement.blow_type == "":
            return 0

        return self.movement.damage

    def relate(self) -> str:
        super_move = self.movement.has_super_move_from(self.participant.super_moves)
        short_name = self.participant.short_name()

        if super_move:
            conn = random.choice(("usa", "hace un", "se aplica", "conecta", "destella", "arrasa con un", "lanza un"))
            return f"{short_name} {conn} {super_move.name}"

        if self.movement.blow_type == "":
            return f"{short_name} solo se mueve"

        if self.movement.blow_type == "P":
            blow = "un " + random.choice(("combo", "piña", "puño", "tsuki"))
        else:
            blow = "una " + random.choice(("patada", "mawashi"))

        conn = random.choice(("lanza", "se aplica", "conecta", "arrasa con"))

        return f"{short_name} {conn} {blow}"