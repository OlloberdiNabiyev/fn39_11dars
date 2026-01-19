from abc import abstractmethod,ABC

class Person(ABC):
    def __init__(self,name,lastname,age,address):
        self.name = name
        self.lastname = lastname
        self.__age = age
        self.__address = address


    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,value):
        self.__age = value
    
    @age.deleter
    def age(self):
        del self.__age

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self,value):
        self.__address = value
    
    @address.deleter
    def address(self):
        del self.__address

    @abstractmethod
    def get_info(self):
        pass

class Employee(Person):
    def __init__(self, name, lastname, age, address,salary):
        super().__init__(name, lastname, age, address)
        self.__salary =salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,value):
        self.__salary = value
    @salary.deleter
    def salary(self):
        del self.__salary
    def get_info(self):
        pass

e1 = Employee('Nodir','Valiyev',21,'fergana',700)
e2 = Employee('Vali','Toxirov',18,'tashkent',550)
print(hasattr(e1,'address'))
print(getattr(e1,'address'))
setattr(e1,'age',20)
delattr(e1,'address')
print(e1.__dict__)
print(hasattr(e2,'name'))
print(getattr(e2,'name'))
setattr(e2,'age',19)
delattr(e2,'name')
print(e2.__dict__)