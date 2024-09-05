from abc import abstractmethod


class Vehicle:

    @abstractmethod
    def get_fuel_efficiency(self):
        pass
    def describe(self):
        print("description of vehicle type")

    @classmethod
    def from_name(cls,choose):
        if choose.lower()=="car":
            return Car()
        elif choose.lower()=="truck":
            return Truck()
        else:
            return AttributeError("No attribute found")


class Car(Vehicle):

    def get_fuel_efficiency(self):
        return "25 miles per gallon"

    def describe(self):
        print("This is car")


class Truck(Vehicle):
    def get_fuel_efficiency(self):
        return "15 miles per gallon"

    def describe(self):
        print("This is truck")