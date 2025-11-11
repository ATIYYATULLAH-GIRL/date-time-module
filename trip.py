def hotel_cost(nights):
    return 10*nights
def plane_ride_cost(city):
    if "Abuja"==city:
        return 200
    elif "Jos"==city:
        return 180
    elif "Rivers"==city:
        return 150
    elif "Delta"==city:
        return 100
def rental_car(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days
def trip_cost(city,days,spending_money):
    return hotel_cost(days)+plane_ride_cost(city)+rental_car(days)+spending_money
print("Cost of car rental",rental_car(5))
print("Cost of hotel room",hotel_cost(7))
print("Cost of plane ride",plane_ride_cost("Jos"))
print("Total trip cost",trip_cost("Abuja",5,600))