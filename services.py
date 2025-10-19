from repositories import HabitRepository
from models import Habit

class HabitService:
    def __init__(self, repository: HabitRepository):
        self.repository = repository

    async def createHabit(self, habitName:str, frequency:str) -> Habit:
        if frequency not in ["daily", "weekly", "monthly"]:
            raise ValueError("Invalid frequency")
        
        return await self.repository.CreateHabit(habitName=habitName, frequency=frequency)
    
    async def getAllHabits(self):
        return await self.repository.GetAllHabits()
    
    async def getHabitByID(self, habitID: int):
        habit = await self.repository.GetHabitByID(habitID=habitID)

        if habit:
            return habit
        else:
            raise ValueError("Invalid ID")
        
    async def deleteHabit(self, habitID: int):
        result = await self.repository.RemoveHabit(habitID=habitID)

        if result:
            return True
        else:
            return False