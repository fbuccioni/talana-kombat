from fastapi import APIRouter

from . import fight

router = APIRouter(
    prefix="/api/v1",
    # dependencies=[Depends(get_token_header)],
    responses={404: {"detail": "Not found"}},
)

router.include_router(fight.router)
