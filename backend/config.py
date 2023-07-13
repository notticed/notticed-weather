from fastapi import FastAPI, Request, Response, Depends,HTTPException
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from hashing import *
from connection import *
import json
import base64
from urllib.request import urlopen
from datetime import datetime

app = FastAPI()
API_KEY = "a8af76f21f133929f58bb3d5bab2a0d6"

# cors policy
origins = "https://weather-backend-yiwj.onrender.com/"
@app.middleware("http")
async def add_cors_headers(request, call_next):
  response = await call_next(request)
  response.headers["Access-Control-Allow-Origin"] = origins
  response.headers["Access-Control-Allow-Credentials"] = "true"
  response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
  response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
  return response

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


class User(BaseModel):
  email: str
  password: str



def user_payload(email, password):
  return {
    'email': email,
    'password': hashing(password)
  }

def kelvin_convert(temp):
  return temp - 273.15