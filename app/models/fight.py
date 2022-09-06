from typing import List, Literal

from pydantic import BaseModel, Field, constr

MovementStr = constr(regex=r"^[WASD]{0,5}$", max_length=5, to_upper=True)


class FightParticipant(BaseModel):
    movimientos: List[MovementStr] = Field(title="Lista de movimientos")
    golpes: List[Literal["", "P", "K", "p", "k"]] = Field(title="Lista de golpes")


class Fight(BaseModel):
    player1: FightParticipant
    player2: FightParticipant
