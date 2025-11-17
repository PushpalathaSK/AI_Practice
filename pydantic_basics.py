from pydantic import BaseModel,EmailStr
'''
class Person(BaseModel):
    name:str
    age:int
    email:str

person1=Person(name="Sk",age=11,email="sk")
print(person1)

person2=Person(name="Sk",age="11",email="sk@gmail.com")
print(person2) #age changes as int

person3=Person(name=123,age="11",email="sk@gmail.com")
print(person3)# raises error
'''

class Person(BaseModel):
    name:str
    age:int
    email:EmailStr



person2=Person(name="Sk",age="11",email="sk@gmail.com")
print(person2) 

person1=Person(name="Sk",age=11,email="sk")
print(person1)



