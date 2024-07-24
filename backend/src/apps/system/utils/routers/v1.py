# Built-in Dependencies

# Third-Party Dependencies
import fastapi

# Local Dependencies

router = fastapi.APIRouter(tags=["System - Utils"])


@router.get("/system/utils/ping", status_code=200)
async def ping() -> dict:
    return {"message": "pong"}
