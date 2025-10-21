from repositories import HabitRepository, UserRepository
from models import Habit
from passlib.context import CryptContext
from authx import AuthX, AuthXConfig

config = AuthXConfig()
config.JWT_SECRET_KEY = "ANDREY_LOH"
config.JWT_ACCESS_COOKIE_NAME = "access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

def createToken(security: AuthX, userID: int):
        return security.create_access_token(uid=str(userID))

class HabitService:
    def __init__(self, repository: HabitRepository):
        self.repository = repository

    async def createHabit(self, habitName:str, frequency:str, user_id: int) -> Habit:
        if frequency not in ["daily", "weekly", "monthly"]:
            raise ValueError("Invalid frequency")
        
        return await self.repository.CreateHabit(habitName=habitName, frequency=frequency, user_id=user_id)
    
    async def getAllHabits(self, userID: int):
        return await self.repository.GetAllHabits(userID=userID)
    
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
    
class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
        self.pwdContext = CryptContext(
            schemes=["sha256_crypt"],
            deprecated="auto"
        )
    
    def _hashPassword(self, password: str) -> str:
        return self.pwdContext.hash(password)

    def _verifyPassword(self, password: str, hashPassword: str) -> bool:
        return self.pwdContext.verify(password, hashPassword)
    
    async def authUser(self, login: str, password: str):
        user = await self.repository.getUserByLogin(login=login)

        if user and self._verifyPassword(password=password, hashPassword=user.password):
            token = createToken(security=security, userID=user.id)

            return [user, token]
        else:
            return None

    async def registerUser(self, login: str, password: str):
        if not  await self.repository.getUserByLogin(login=login):
            hashedPassword = self._hashPassword(password=password)

            await self.repository.createUser(login=login, password=hashedPassword)
            return True
        else:
            return False