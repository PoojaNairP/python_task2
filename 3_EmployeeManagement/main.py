from Employee import FullTimeEmployee,PartTimeEmployee

def validation_float():
    while True:
        try:
            number=float(input("Enter the value: "))
            if number<0:
                raise ValueError
            return number
        except ValueError:
            print("Positive integer expected")

def validation_name():
    while True:
        try:
            employee_name=input("Enter the name : ")
            if employee_name=='':
                raise ValueError("Name can't be null")
            return employee_name
        except ValueError as ex:
            print(ex)


def validation_employee_type():
    while True:
        try:
            emp_type = input("Enter employment type : ")
            emp_type=emp_type.replace(" ","")
            emp_type = emp_type.replace("-", "")
            #print(emp_type)
            if emp_type.lower() not in ["fulltime", "parttime"]:
                raise ValueError("Employment type should be fulltime or parttime")
            return emp_type
        except ValueError as ex:
            print(ex)



name=validation_name()
employee_type=validation_employee_type()
try:
    if employee_type.lower()=="fulltime":
        employee=FullTimeEmployee(name)
        employee.describe()
        print(f"The salary of {employee.name} is ${employee.calculate_salary()}")

    else:
        print("Hours Worked")
        hours_worked=validation_float()
        print("Hourly Rate")
        hourly_rate=validation_float()
        employee = PartTimeEmployee(name,hours_worked,hourly_rate)
        employee.describe()
        print(f"The salary of {employee.name} is ${employee.calculate_salary()}")

except TypeError as e:
    print(e)



