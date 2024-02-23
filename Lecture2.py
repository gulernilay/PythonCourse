"""
Lecture 2: OPERATORS
"""
x,y,z=4,5,6
print(x,y,z)

x,y=y,x # exchange x and y 
x+=5  #x=x+5 
x*=5   # x=x*5
x%=2
x//=2
x/=2
x**2

values=1,2,3 # tuple
a,b,c =values
print(a,b,c)
values2=1,2,3,4,5 # tuple
a2,b2,c2 =values2
print(a2,b2,*c2)  # a2=1,b2=2,c=[3,4,5] list


#-----------------------------------------Comparison Operators---------------------------------------------------------------------------
# !=, ==, >= ,<= < ,> 
a,b,c,d=5,5,6,7
if a==b :
  print("equal")
else:
  print("not equal")
#-----------------------------------------Logical Operators-------------------------------------------------------------------------------
x=6
if (x<15) and (x>5):
    x+=7
    print(x)
elif (x<16) or(x>30):
   print("or")
else:
   print("nothing")
result=not(x<0)

#----------------------------------------- is/in OPERATORS -------------------------------------------------------------------------------------
x=y=[1,2,3,4,5,6]
z=[1,2,3,4,5,6]
t=[2,4,6]
print(x==y)#true
print(x is y)#true döndürür çünkü ikiside aynı adrese sahip 
print(x is z)#false
meyve=["ananas","banana"]
print( "banana" in meyve) #True
print( "banana" not in meyve)#False




