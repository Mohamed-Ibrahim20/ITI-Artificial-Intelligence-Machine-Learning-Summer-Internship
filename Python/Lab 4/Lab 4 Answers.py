class Person:
    def __init__(self, name, age, GPA):
        self.name = name
        self._age = age
        self.__GPA = GPA
    
    def show(self):
        print(f"Name: {self.name}, His age is: {self._age}, And his GPA is: {self.__GPA}")


class Student(Person):
    def __init__(self, name, age, GPA, university, email):
        super().__init__(name, age, GPA)
        self.university = university
        self._email = email
    
    def print_info(self):
        print(f"Name: {self.name}, His age is: {self._age}, his GPA is: {self._Person__GPA}, His email is: {self._email}, And his university is: {self.university}")


pub_person = Person("Mohamed", 21, 3.91)
print(f"Name: {pub_person.name}, Age: {pub_person._age}, GPA: {pub_person._Person__GPA}")
Student1 = Student("Ahmed", 22, 4.0, "Mansoura University", "Ahmed@gmail.com")
Student1.print_info()
