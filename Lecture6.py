"""
Lecture6: OOP(Object Oriented Programming)
"""
#List Class Object
list1=[1,2,3,4] #object=instance of List Class
print(list1)
list2=[2,3,4,5,7]

# List Class Method
list1.append(10) # add 10 to list
list2.clear()
print(f"The second element of list1 is  {list1.index(2)}")
print(f"The number of 2 in list1 is  {list1.count(2)}")

#class implementation: 
class Person:

  address="no info" #attributes 
  def __init__(self,name,birthday): #constructor
    self.name=name
    self.birthday=birthday
  def intro(self):
    print("Hello")
    print(f"I am {self.name}")
  def calculateAge(self):
    return 2022-self.birthday

#Object declaration
p1=Person("ali",1920)
print(f"p1 name: {p1.name} , p1 address :{p1.address}")
print(f"p1 name: {p1.name} , p1 age :{p1.calculateAge}")
print(type(p1)) #Person
p1.intro()


class Circle:
  pi=3.14
  def __init__(self,yariçap=1):    #defaul yarıçap =1
    self.yariçap=yariçap
  
  def çevre_hesapla(self):
    return 2*self.pi*self.yariçap
  
C1=Circle() #yarıçap=1
c2=Circle(5) #yariçap=5
C1.çevre_hesapla




