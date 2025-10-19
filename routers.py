from database import createSession
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from services import HabitService
from repositories import HabitRepository
import schemas

router = APIRouter()

@router.post("/habits", response_model=schemas.HabitModel, tags=["habits"], summary="create habit")
async def createHabit(habitData: schemas.HabitAddModel, session: AsyncSession=Depends(createSession), ):
    repository = HabitRepository(session=session)
    service = HabitService(repository=repository)
    try:
        return await service.createHabit(habitData.habitName, habitData.frequency)
    except ValueError as e:
        raise HTTPException(400, str(e))
    
@router.get("/habits", response_model=list[schemas.HabitModel], tags=["habits"], summary="get all habits")
async def getAllHabits(session: AsyncSession=Depends(createSession)):
    repository = HabitRepository(session=session)
    service = HabitService(repository=repository)

    return await service.getAllHabits()

@router.get("/habits/{habitID}", response_model=schemas.HabitModel, tags=["habits"], summary="get one habit")
async def getHabitByID(habitID: int, session: AsyncSession=Depends(createSession)):
    repository = HabitRepository(session=session)
    service = HabitService(repository=repository)

    try:
        return await service.getHabitByID(habitID=habitID)
    except ValueError as e:
        raise HTTPException(404, "Habit not found")
    
@router.delete("/habits/{habitID}", tags=["habits"], summary="delete habit by id")
async def deleteHabit(habitID: int, session: AsyncSession=Depends(createSession)):
    repository = HabitRepository(session=session)
    service = HabitService(repository=repository)

    if await service.deleteHabit(habitID=habitID):
        return {"status":"OK"}
    else:
        return {"status":"error"}