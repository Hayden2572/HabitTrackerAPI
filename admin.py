from database import engine
from fastapi import APIRouter
from models import Base

router = APIRouter()

@router.post("/admin-createdb", tags=["admin"], summary="create/recreate database")
async def createDB():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"status":"OK", "msg":"database created successfully"}