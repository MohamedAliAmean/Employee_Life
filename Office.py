from shelve import Shelf


class Office :
    def __init__(self,Name):
        self.Name = Name
        self.Employees =[]
    def get_All_Employees(self):
        return self.Employees
    def get_Employee(self,Employee_ID):
        for Employee in self.Employees:
            if Employee.get_Employee_ID()==Employee_ID:
                return Employee
            else:
                return None
    def Hire(self,Employee):
        self.Employees.append(Employee)
        print(f"{Employee.Name} has been hired")
    def Fire(self,Employee_ID):
        Employee= self.get_Employee(Employee_ID)
        if Employee:
            self.Employees.remove(Employee)
            print(f"{Employee.Name} has been Fired")
        else:
            print("Employee Not Found ")
    def Calc_Lateness(self,Employee_ID ,Arrival_Time):
        Employee=self.get_Employee(Employee_ID)
        if Employee:
            if Arrival_Time>9:
                latenss=Arrival_Time -9
                print(f"{Employee.Name} is {latenss} Hours late")
                return latenss
            else:
                print("Employee Not Found")
                return None
    def deduct(self,Employee_ID,Amount):
        Employee =self.get_Employee(Employee_ID)
        if Employee:
            new_Salary = Employee.get_Salary() -Amount
            Employee.set_Salary(new_Salary)
            print(f"${Amount}deducted from {Employee.Name}'s salary. New salary: ${Employee.get_salary()}")
        else:
            print("Employee Not Found ")

    def reward(self, Employee_ID, reward):
        Employee = self.get_Employee(Employee_ID)
        if Employee:
            Employee.salary += reward
            print(f"${reward} added to {Employee.Name}'s salary. New salary: ${Employee.salary}")
        else:
            print("Employee not found.")

