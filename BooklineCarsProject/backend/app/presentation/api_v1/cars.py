from fastapi import APIRouter

import datetime
import json

users_router = r = APIRouter()

@r.get("/cars/available")
async def get_available_cars(
    specifiedDate: datetime.datetime 
):
    return None