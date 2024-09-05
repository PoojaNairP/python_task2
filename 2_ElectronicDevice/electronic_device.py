from abc import abstractmethod


class ElectronicDevice:

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    @abstractmethod
    def power_usage(self):
        pass

    def describe(self):
        print(f"The device is of brand {self.brand} and model {self.model}.")

    @classmethod
    def from_type(cls,type_name,brand,name,number):
        if type_name=="laptop":
            return Laptop(brand,name,number)
        else:
            return Smartphone(brand,name,number)


class Laptop(ElectronicDevice):

    def __init__(self, brand, model,battery_life):
        super().__init__(brand, model)
        self.battery_life=battery_life

    def power_usage(self):
        return "The power usage of laptop is 50 watts per hour"


class Smartphone(ElectronicDevice):

    def __init__(self, brand, model,screen_size):
        super().__init__(brand, model)
        self.screen_size=screen_size

    def power_usage(self):
        return "The power usage of smartphone is 10 watts per hour"



