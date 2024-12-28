from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int


mohammed = Person("Mohammed", 25)
print(mohammed)



@dataclass
class employee(Person):
   department: str
   salary: float