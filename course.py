from abc import ABC,abstractmethod
class Course(ABC):
    def __init__(self,course_name,duration,students:list,teacher):
        self.__course_name = course_name
        self.__duration = duration
        self.students = students
        self.teacher = teacher
    @property
    def student(self):
        return self.students
    
    @student.setter
    def student(self,value):
        self.students.append(value)

    @property
    def course_name(self):
        return self.__course_name
    
    @course_name.setter
    def course_name(self,value):
        self.__course_name = value

    @course_name.deleter
    def course_name(self):
        del self.__course_name
    
    @property
    def duration(self):
        return self.__duration
    
    @duration.setter
    def duration(self,value):
        self.__duration = value

    @duration.deleter
    def duration(self):
        del self.__duration

    @abstractmethod 
    def get_info(self):
        pass

class OnlineCourse(Course):
    def __init__(self, course_name, duration, students, teacher,platform):
        super().__init__(course_name, duration, students, teacher)
        self.__platform = platform

    @property
    def platform(self):
        return self.__platform
    
    @platform.setter
    def platform(self,value):
        self.__platform = value

    @platform.deleter
    def platform(self):
        del self.__platform
        
    def get_info(self):
        pass
c1 = OnlineCourse(
    "Python Backend",
    3,
    ["Ali", "Vali"],
    "Aziz",
    "Udemy"
)

c2 = OnlineCourse(
    "Web Frontend",
    4,
    ["Sardor", "Jasmin"],
    "Kamola",
    "Coursera"
)
setattr(c1,'grade',5)
print(getattr(c1,'students'))
print(c1.platform)
c1.student = 'Toxir'
c1.platform = 'w3schools'
delattr(c1,'grade')
del c1.duration
print(hasattr(c1,'duration'))
print(c1.__dict__)