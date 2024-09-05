from electronic_device import ElectronicDevice


def validation(name):
    if name.lower() in ["smartphone","laptop"]:
        return name
    else:
        name=input(f"The provided type not found.\nEnter a valid type : ")
        return validation(name)

type_name = input("Enter the type : ")
type_name = validation(type_name)
# print(type_name)
brand = input("Enter the brand : ")
model = input("Enter the model : ")

while True:
    try:

        if type_name.lower()=="laptop":
            battery_life = int(input("Enter the battery life in hours: "))
            if battery_life<0:
                raise ValueError("Positive Integer Expected....")
            laptop = ElectronicDevice.from_type(type_name, brand, model,battery_life)
            laptop.describe()
            print(laptop.power_usage())
            break
        else:
            screen_size=float(input("Enter the screen size in inch : "))
            if screen_size<0:
                raise ValueError("Positive Number Expected....")
            smartphone = ElectronicDevice.from_type(type_name, brand, model,screen_size)
            smartphone.describe()
            print(smartphone.power_usage())
            break

    except ValueError as e:
        print(e)


    except TypeError as e:
        print(e)

    except AttributeError as e:
        print(e)











