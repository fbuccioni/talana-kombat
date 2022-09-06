from typing import List, Type, Union, Sequence, Optional

from .sequence import FightSequence
from .base import FightEngine
from .exceptions import FightException, FightOverException
from .movement import FightMovement
from .participant import FightParticipant


class Fight(FightEngine):
    movement_class: Type[FightMovement] = FightMovement
    health: int = 6
    participants: List[FightParticipant]
    sequence: List[FightSequence]

    def __init__(self, health: Optional[int] = None):
        self.sequence = []
        self.super_moves = set()
        self.participants = []

        if health:
            self.health = health

    def add_participants(self, *participants: Sequence[FightParticipant]) -> "Fight":
        if len(participants) != 2:
            raise FightException("Participants must be 2")

        for participant in participants:
            participant.health = self.health

        self.participants = participants

        return self

    def participant_by_name(self, name: str) -> Optional[str]:
        return next((p for p in self.participants if p.name == name), None)

    def participant_by_alias(self, alias: str) -> Optional[str]:
        return next((p for p in self.participants if p.alias == alias), None)

    def participant_by_name_or_alias(self, name_or_alias: str) -> Optional[str]:
        p = self.participant_by_name(name_or_alias)
        if p: return p
        p = self.participant_by_alias(name_or_alias)
        return p

    def add_sequence(
        self,  participant: Union[FightParticipant, str],  directions: str, blow_type: str
    ) -> "Fight":
        if self.is_over():
            raise FightOverException(f"Fight is over")

        if isinstance(participant, str):
            participant = self.participant_by_name_or_alias(participant)
            if not participant:
                raise FightException(f"There's no {participant} in this fight")

        if participant not in self.participants:
            raise FightException(f"This is not the fight of {participant.name}")

        orientation = "R" if participant == self.participants[0] else "L"
        rival = self.participants[1 if orientation == "R" else 0]

        sequence = FightSequence(
            movement=self.movement_class(directions, blow_type),
            participant=participant,
            orientation=orientation
        )

        rival.health -= sequence.damage()
        self.sequence.append(sequence)

        return self

    def is_over(self):
        return (
            len(self.participants) == 0 or (
                self.participants[0].health < 1
                or self.participants[1].health < 1
            )
        )

    def relate(self):
        relate_list = [s.relate() for s in self.sequence]

        if self.is_over():
            if self.participants[0].health < 1:
                loser, winner = self.participants
            else:
                winner, loser = self.participants

            relate_list.append(f"Ha ganado {winner.short_name()} con {winner.health}")

        return relate_list