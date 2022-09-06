from typing import Optional, Set, Type, Sequence

from .movement import FightMovement
from .base import FightEngine


class FightParticipant(FightEngine):
    name: str
    alias: Optional[str]
    super_moves: Set[Type[FightMovement]]
    health: int = 10

    def __init__(self, name: str, alias: str = None, health = None):
        if health is None:
            health = type(self).health

        self.name = name
        self.alias = alias
        self.super_moves = set()
        self.health = health

    def short_name(self):
        return self.name.split(' ')[0]

    def add_super_moves(self, *super_moves: Type[FightMovement]):
        for super_move in super_moves:
            self.super_moves.add(super_move)

        return self
