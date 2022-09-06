from ..util import fight_engine


player1 = fight_engine.FightParticipant(
    "Tonyn Stallone", "player1"
)\
    .add_super_moves(
        fight_engine.FightMovement(
            name="Taladoken", damage=3,
            directions="DSD", blow_type="P"
        ),
        fight_engine.FightMovement(
            name="Remuyuken", damage=2,
            directions="SD", blow_type="K"
        )
    )

player2 = fight_engine.FightParticipant(
    "Arnaldor Shuatseneguer", "player2"
)\
    .add_super_moves(
        fight_engine.FightMovement(
            name="Remuyuken", damage=3,
            directions="SA", blow_type="K"
        ),
        fight_engine.FightMovement(
            name="Taladoken", damage=2,
            directions="ASA", blow_type="P"
        )
    )

player_moya = fight_engine.FightParticipant(
    "Moya", "playermoya"
)
