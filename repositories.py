from models import Habit, User
from sqlalchemy import select

class HabitRepository:
    def __init__(self, session):
        self.session = session

    async def CreateHabit(self, habitName: str, frequency: str, user_id: int) -> Habit:
        newHabit = Habit(habitName=habitName, frequency=frequency, user_id=user_id)

        self.session.add(newHabit)
        await self.session.commit()

        return newHabit
    
    async def GetAllHabits(self, userID: int):
        habits = await self.session.execute(select(Habit).where(Habit.user_id == userID))

        return habits.scalars().all()

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
        
class UserRepository:
    def __init__(self, session):
        self.session = session

    async def getUserByLogin(self, login: str):
        result = await self.session.execute(select(User).where(User.login == login))   

        return result.scalar_one_or_none()

    async def createUser(self, login: str, password: str):
        newUser = User(login=login, password=password)

        self.session.add(newUser)
        await self.session.commit()

        return newUser
    