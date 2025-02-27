class Human :
    def __init__(self,ID,Name,Age,Gender):
        self.__ID=ID
        self._Age=Age
        self.Name=Name
        self.Gender=Gender
    @property
    def id(self):
        return self.__ID
    def __str__(self):
        return (f"Human(ID:{self.__ID}, Name:{self.Name}, Age:{self._Age}, Gender:{self.Gender}")
    def Sleep(self):
        print (f"zzzzzzz Iam sleeping")
    def Eat(self):
        print(f"humhumhumhum Iam Eating")
    def Buy(self):
        print (f"Iam Eating")
    def get_ID(self):
        return self.__ID
    def set_ID(self,new_ID):
        if len(new_ID) == 14:
            self.__ID=new_ID
        else:
            print ("invalid ID")
    def get_age(self):
        return self._Age
    def set_age(self,new_Age):
        if new_Age>0:
            self._Age=new_Age
        else:
            print("Invalid age")