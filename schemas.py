from pydantic import BaseModel

#habits schemas
class HabitAddModel(BaseModel):
    habitName: str
    frequency: str

class HabitModel(BaseModel):
    id: int
    habitName: str
    frequency: str
    user_id: int

#user schemas
class RegistrationModel(BaseModel):
    login: str
    password: str

class LoginModel(BaseModel):
    login: str
    password: str

class UserResponseModel(BaseModel):
    id: int
    login: str
    
    class Config:
        from_attributes = True
