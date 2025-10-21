from database import engine, createSession
from fastapi import APIRouter
from models import Base
from models import User, Habit
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends


router = APIRouter()

@router.post("/admin-createdb", tags=["admin"], summary="create/recreate database")
async def createDB():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"status":"OK", "msg":"database created successfully"}

@router.get("/admin-getusers", tags=["admin"], summary="get all users")
async def getAllUsers(session: AsyncSession=Depends(createSession)):
    result = await session.execute(select(User))
    return result.scalars().all()

@router.get("/admin-gethabits", tags=["admin"], summary="get all habits")
async def getAllHabits(session: AsyncSession=Depends(createSession)):
    result = await session.execute(select(Habit))
    return result.scalars().all()