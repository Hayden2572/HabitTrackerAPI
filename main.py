from fastapi import FastAPI
from routers import router as HabitRouter
from admin import router as AdminRouter
import uvicorn

app = FastAPI()
app.include_router(HabitRouter)
app.include_router(AdminRouter)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)