import datetime
from typing import List

from app.infrastructure.impl import cars_repository
from app.domain.cars_model import car_model
from app.services.contracts import cars_dtos
async def retrive_available_cars(specified_available_date: datetime.date):
    cars_list = await cars_repository.read_json_cars_file()

    available_cars_list = list()

    for car in cars_list:
        domain_car = car_model(id=car["id"], name= car["Name"], booked_dates= car["BookedDates"])
        if await domain_car.check_car_boking(specified_available_date) == False:
            available_car = cars_dtos.car_dto_response(
                name = domain_car.name,
                booked_dates = domain_car.booked_dates)

            available_cars_list.append(available_car)


    return available_cars_list

async def create_car_booking(booking_date: datetime.datetime, car_name: str):
    cars_list = await cars_repository.read_json_cars_file()

    i = 0
    for car in cars_list:
        if car["Name"] == car_name:
            domain_car = car_model(id=car["id"], name=car["Name"], booked_dates= car["BookedDates"])
            if await domain_car.book_car(booking_date) == False:
                return False
            cars_list[i]["BookedDates"].append(str(booking_date))
            await cars_repository.write_json_cars_file(cars_list)
            return True
        i += 1
    return True