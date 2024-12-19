import datetime

from app.infrastructure.impl import cars_repository

async def retrive_available_cars(specified_date: datetime.datetime):
    cars_list = await cars_repository.read_json_cars_file()
    return cars_list

async def create_car_booking(booking_date: datetime.datetime):
    return None