from fastapi import APIRouter, HTTPException # type: ignore

from app.services.impl import cars_services

import datetime
import logging

cars_router = APIRouter()

@cars_router.get("/cars/available")
async def get_available_cars(
    specified_date: datetime.date 
):
    logging.info("GET /cars/available called")
    available_cars = await cars_services.retrive_available_cars(specified_date)
    logging.info("GET /cars/available returning data")
    return available_cars

@cars_router.post("/cars/book_a_car")
async def post_car_booking(    
    booking_date: datetime.date,
    car_name: str
):
    logging.info("POST /cars/book_a_car called")
    if await cars_services.create_car_booking(booking_date=booking_date,car_name=car_name):
        logging.info("POST /cars/book_a_car returning data")
        return "Cars has been booked" 
    else:
        logging.info("POST /cars/book_a_car returned 400")
        raise HTTPException(status_code=400, detail="Car couldn't be booked")