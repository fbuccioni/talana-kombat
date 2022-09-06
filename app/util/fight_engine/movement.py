import hashlib
from typing import Optional, Sequence, Type
from .exceptions import FightMovementException
from .base import FightEngine


class FightMovement(FightEngine):
    max_directions: int = 5
    damage: int = 1

    name: str
    directions: str
    blow_type: str

    def __init__(
        self, directions: str, blow_type: str,
        name: Optional[str] = None, damage: Optional[int] = None
    ):
        if len(directions) > self.max_directions:
            raise FightMovementException(
                f"Directions cannot be more than f{self.max_directions}"
            )

        if len(blow_type) > 1:
            raise FightMovementException("Blow type must be 1 characted.")

        if damage is None:
            damage = type(self).damage

        self.directions = directions
        self.blow_type = blow_type
        self.name = name
        self.damage = damage

    def __str__(self):
        desc = 'Fight movement <'

        if self.name:
            desc += f"name: {self.name}: "

        return desc + (
            f"direction: {self.directions}, "
            f"blow type: {self.blow_type}, "
            f"damage: {self.damage}>"
        )

    def __repr__(self):
        return self.__str__()

    def __hash__(self) -> int:
        hashstr = f"{self.directions}|{self.blow_type}"
        return int(hashlib.sha1(hashstr.encode()).hexdigest(), 16)

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.__hash__() == other.__hash__()

    def has_super_move_from(self, super_moves: Sequence[Type["FightMovement"]]):
        dir_len: int = len(self.directions)

        for super_move in super_moves:
            sup_move_dir_len = len(super_move.directions)

            if (
                (dir_len == sup_move_dir_len and super_move == self)
                or (
                    dir_len > sup_move_dir_len
                    and (
                        f"{self.directions[-sup_move_dir_len:]}|{self.blow_type}"
                        == f"{super_move.directions}|{super_move.blow_type}"
                    )
                )
            ):
                return super_move
