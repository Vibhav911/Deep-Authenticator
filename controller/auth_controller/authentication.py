from datetime import datetime, timedelta
from typing import Optional
import sys

from fastapi import APIRouter, Response, Request, status, HTTPException
from jose import JWTError, jwt
from pydantic import BaseModel
from starlette.responses import JSONResponse, RedirectResponse
from face_auth.exception import AppException

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={"401": {"description": "Not Authorized!!!"}}
)

class Login(BaseModel):
    "Base Model for login"
    email_id: str
    password: str
    
@router.get("/", response_class=JSONResponse)
async def authentication_page(request: Request):
    try:
        response = JSONResponse(status_code=status.HTTP_200_OK,
            content={"message": "Authentication Page !!!"}
        )
        return response
        
    except Exception as e:
        raise AppException(e, sys)
        
@router.post("/", response_class=JSONResponse)
async def login(request: Request, login: Login):
    try:
        pass
    
    except Exception as e:
        raise AppException(e, sys)
