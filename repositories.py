from models import Habit
from sqlalchemy import select

class HabitRepository:
    def __init__(self, session):
        self.session = session

    async def CreateHabit(self, habitName: str, frequency: str) -> Habit:
        newHabit = Habit(habitName=habitName, frequency=frequency)

        self.session.add(newHabit)
        await self.session.commit()

        return newHabit
    
    async def GetAllHabits(self):
        result = await self.session.execute(select(Habit))
        return result.scalars().all()

    async def GetHabitByID(self, habitID:int):
        return await self.session.get(Habit, habitID)

    async def RemoveHabit(self, habitID: int):
        habit = await self.session.get(Habit, habitID)
        if habit:
            await self.session.delete(habit)
            await self.session.commit()

            return True
        else:
            return False

        