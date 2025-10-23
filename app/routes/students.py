from fastapi import APIRouter

router = APIRouter(prefix="/students", tags=["students"])


@router.get("/ping")
async def ping():
    return {"message": "students router alive"}
