from Vehicle import Vehicle

while True:
    try:
        choose = input("Enter vehicle type: ")
        chosen_vehicle=Vehicle.from_name(choose)
        #print(type(chosen_vehicle))
        print(f"The fuel efficiency of {choose} is {chosen_vehicle.get_fuel_efficiency()}")
        chosen_vehicle.describe()
        break
    except AttributeError:
        print("No vehicle type found")


























"""while choose.lower() != "car" and choose.lower()!= "truck":
    print("No vehicle type found")
    choose = input("Enter the vehicle: ")
"""

"""chosen_vehicle=Vehicle.from_name(choose)
#print(type(chosen_vehicle))
print(chosen_vehicle.get_fuel_efficiency())
chosen_vehicle.describe()"""