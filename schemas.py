from pydantic import BaseModel

class HabitAddModel(BaseModel):
    habitName: str
    frequency: str

class HabitModel(BaseModel):
    id: int
    habitName: str
    frequency: str