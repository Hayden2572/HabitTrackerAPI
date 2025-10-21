from database import createSession
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from services import HabitService, security
from repositories import HabitRepository
import schemas

router = APIRouter()

@router.post("/habits", response_model=schemas.HabitModel, tags=["habits"], summary="create habit")
async def createHabit(user_id: int, habitData: schemas.HabitAddModel, session: AsyncSession=Depends(createSession), ):
    repository = HabitRepository(session=session)
    service = HabitService(repository=repository)
    try:
        return await service.createHabit(
            habitName=habitData.habitName,
            frequency=habitData.frequency,
            user_id=user_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    
@router.get("/habits", response_model=list[schemas.HabitModel], tags=["habits"], summary="get all habits", dependencies=[Depends(security.access_token_required)])
async def getAllHabits(user_id: int, session: AsyncSession=Depends(createSession)):
    repository = HabitRepository(session=session)
    service = HabitService(repository=repository)

    return await service.getAllHabits(userID=user_id)

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
    
