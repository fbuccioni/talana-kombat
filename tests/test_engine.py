from app.util import fight_engine
from app.fight import participants


def test_fight_participants():
    fight = fight_engine.Fight()

    try:
        fight.add_participants(
            participants.player1,
            participants.player2,
            participants.player_moya
        )
    except fight_engine.exceptions.FightException:
        pass
    else:
        assert False

    try:
        fight.add_participants(participants.player1)
    except fight_engine.exceptions.FightException:
        pass
    else:
        assert False

    fight.add_participants(
        participants.player1,
        participants.player2,
    )


def test_fight_sequence():
    fight = fight_engine.Fight() \
        .add_participants(
            participants.player1,
            participants.player2,
        )

    try:
        fight.add_sequence(
            "player1", "DSDASA", "P"
        )
    except fight_engine.exceptions.FightMovementException:
        pass
    else:
        assert False

    fight.add_sequence(
        "player1", "DSD", "P"
    )

    fight.add_sequence(
        "player2", "", "P"
    )

    fight.add_sequence(
        "player2", "WA", ""
    )


def test_sequence_relate_super_move():
    fight = fight_engine.Fight(health=20) \
        .add_participants(
            participants.player1,
            participants.player2,
        )

    for participant in (participants.player1, participants.player2):
        for movement in participant.super_moves:
            fight.add_sequence(participant, movement.directions, movement.blow_type)
            assert movement.name in fight.sequence[-1].relate()

        for movement in participant.super_moves:
            fight.add_sequence(participant, "AS" + movement.directions, movement.blow_type)
            assert movement.name in fight.sequence[-1].relate()