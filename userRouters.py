from database import createSession
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Depends, Response
from services import UserService, config
from repositories import UserRepository
from schemas import LoginModel, RegistrationModel, UserResponseModel

router = APIRouter()

@router.post("/register", tags=["users"], summary="register user")
async def register(userData: RegistrationModel, session: AsyncSession=Depends(createSession)):
    repository = UserRepository(session=session)
    service = UserService(repository=repository)

    result = await service.registerUser(login=userData.login, password=userData.password)
    if result:
        return {"status":"OK", "msg":"user created successfully"}
    else:
        return {"status":"error"}

@router.post("/login", tags=["users"], summary="login user")
async def login(response: Response, userData: LoginModel, session: AsyncSession=Depends(createSession)):
    repository = UserRepository(session=session)
    service = UserService(repository=repository)

    result = await service.authUser(login=userData.login, password=userData.password)

    if result:
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, result[1])
        return {"token":result[1], "user_info":UserResponseModel(id=result[0].id, login=result[0].login)}
    else:
        raise HTTPException(401, "invalid login or password")