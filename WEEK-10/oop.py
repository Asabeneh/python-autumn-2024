
class Person:
    def __init__(self, first_name, last_name, age, gender):
        self.fist_name = first_name
        self.last_name = last_name
        self.age = age 
        self.gender = gender
        self.skills = []
    def person_info(self):
        pronoun = 'He' if self.gender == 'male' else 'She'
        return f'{pronoun} is {self.fist_name} {self.last_name}. {pronoun} is {self.age} years.'
    def add_skill(self, skill):
        self.skills.append(skill)
        
        
        
        
p1 = Person('Asab','Yeta', 250, 'Male')
p2 = Person('John', 'Doe', 21, 'Male')

p1.add_skill('Machine Learning')
p1.add_skill('Cloud')
p1.add_skill('DevOps')
p1.add_skill('Data Mining')

print(p1.fist_name, p1.last_name, p1.age, p1.gender)
print(p2.fist_name)
print(p1.person_info())
print(p1.skills)


class Student (Person):
    def __init__(self, first_name, last_name, age, gender):
         super().__init__(first_name, last_name, age, gender)
         self.points = 0
         
    def add_point(self, point):
        self.points = self.points + point
        

s = Student('Elena', 'Elena', 25, 'Female')
s.add_skill('Python')
s.add_skill('Wed Development with Flask')
s.add_point(25)
print(s.person_info())
print(s.points)