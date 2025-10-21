from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

DATABASE_URL = "postgresql+asyncpg://adminhabit:root@localhost:5432/habittracker"

engine = create_async_engine(DATABASE_URL)
SessionMaker = async_sessionmaker(engine, expire_on_commit=False)

async def createSession():
    async with SessionMaker() as session:
        yield session