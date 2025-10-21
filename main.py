from fastapi import FastAPI
from habitRouters import router as HabitRouter
from userRouters import router as UserRouter
from admin import router as AdminRouter
import uvicorn

app = FastAPI()
app.include_router(HabitRouter)
app.include_router(UserRouter)
app.include_router(AdminRouter)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)