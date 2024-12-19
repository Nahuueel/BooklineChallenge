from fastapi import APIRouter, HTTPException

from app.services.impl import cars_services

import datetime

cars_router = APIRouter()

@cars_router.get("/cars/available")
async def get_available_cars(
    specified_date: datetime.date 
):
    available_cars = await cars_services.retrive_available_cars(specified_date)
    return available_cars

@cars_router.post("/cars/book_a_car")
async def post_car_booking(    
    booking_date: datetime.date,
    car_name: str
):
    if cars_services.create_car_booking(booking_date=booking_date,car_name=car_name):
        return "Cars has been booked" 
    else:
        raise HTTPException(status_code=400, detail="Car couldn't be book")