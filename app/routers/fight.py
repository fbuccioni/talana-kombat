from typing import Dict, List

from fastapi import APIRouter, Depends, HTTPException


from ..util import fight_engine
from ..fight import participants
from .. import models


router = APIRouter(
    prefix="/fight", tags=["Fight"],
    responses={404: {"detail": "Not found"}},
)


@router.post('', tags=["Fight"], response_model=List[str])
async def lets_fight(fight_sequence: models.Fight) -> List[str]:
    fight_sequence = fight_sequence.dict()

    fight = fight_engine.Fight() \
        .add_participants(
            participants.player1, participants.player2
        )

    # tupla de estadisticas largo, cant movs, cant golpes
    stats = []
    for p in ("player1", "player2"):
        stat = [
            7,
            len(fight_sequence[p]["movimientos"]),
            len(fight_sequence[p]["golpes"]),
        ]

        if stat[1]:
            stat[0] = len(
                fight_sequence[p]["movimientos"]
                + fight_sequence[p]["golpes"]
            )

        stats.append(stat)

    first = None

    # Ver por golpe mas corto
    if stats[0][0] != stats[1][0]:
        first = 0 if stats[0][0] < stats[1][0] else 1

    # menos cant de movimientos
    if first is None and stats[0][1] != stats[1][1]:
        first = 0 if stats[0][1] < stats[1][1] else 1

    # menos cantidad de golpes
    if first is None and stats[0][2] != stats[1][2]:
        first = 0 if stats[0][2] < stats[1][2] else 1

    if first is None:
        first = 0

    if first == 0:
        turns = ("player1", "player2")
    else:
        turns = ("player2", "player1")

    loop = True
    while loop:
        for p in turns:
            try:
                movements = fight_sequence[p]["movimientos"].pop(0)
                blow_type = fight_sequence[p]["golpes"].pop(0)
            except IndexError:
                loop = False

            try:
                fight.add_sequence(p, movements, blow_type)
            except fight_engine.exceptions.FightOverException:
                loop = False
                break

    return fight.relate()
