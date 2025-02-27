from lab3 import Person


class Employee(Human):
    def __init__(self,ID,Name,Age,Gender,Employee_ID,Department ,Salary):
        super().__init__(ID,Name,Age,Gender)
        self.__Employee_ID = Employee_ID
        self.__Salary=Salary
        self.Department = Department
    def __str__(self):
        return (f"Employee(ID:{self._ID},Name:{self.Name},Age:{self._Age},Gender:{self.Gender}"
                f"Employee ID:{self.__Employee_ID},Salary:{self.__Salary},Department:{self.Department}")
    def Work(self):
        print (f"{self.Name}is working in the {self.Department} department")
    def get_Employee_ID(self):
        return self.__Employee_ID
    def set_Employee_ID(self,new_Employee_ID):
        if len(new_Employee_ID)==4:
            self.__Employee_ID=new_Employee_ID
        else:
            print("Invalid Employee ID ")
    def get_Salary(self):
        return self.__Salary
    def set_Salary(self,newSalary):
        if newSalary>0:
            self.__Salary =newSalary
        else:
            print("Invalid Salary ,Must be positive ")
class Email:
    def __init__(self,To,Subject,Message,Reciver_Name):
        self.to             =To
        self.subject        =Subject
        self.MSG            =Message
        self.Reciver_Name   =Reciver_Name
    def Send_Mail(self):
        Email_Content =(f"""To:{self.to}
                        Subject:{self.subject}
                        Dear {self.Reciver_Name},
                        {self.MSG}
                        Best regards,
                         Your Name""")
        with open("Email.txt","w")as file:
            file.write(Email_Content)
            print(f"Email Sent to{self.Reciver_Name}({self.to})")


