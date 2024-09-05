from abc import abstractmethod


class Employee:

    def __init__(self,name):
        self.name=name

    @abstractmethod
    def calculate_salary(self):
        pass

    def describe(self):
        print("Employee name and type")

class FullTimeEmployee(Employee):

    def __init__(self,name):
        super().__init__(name)

    def calculate_salary(self):
        return 3000

    def describe(self):
        print(self.name," is a full-time employee")


class PartTimeEmployee(Employee):

    def __init__(self,name,hours_worked,hourly_rate):
        super().__init__(name)
        self.hours_worked=hours_worked
        self.hourly_rate=hourly_rate

    def calculate_salary(self):
        return self.hours_worked*self.hourly_rate

    def describe(self):
        print(self.name," is a part-time employee")








