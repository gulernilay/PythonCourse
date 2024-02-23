"""
Lecture5: Functions, Lambda Expressions, GlobalLocal Variables
"""

def say_Hello():
  print("Hello")

#say_Hello()

def say2_Hello(name="user"): # name girilmediğinde default user bastırılır
  print(f"Hello {name}")

#say2_Hello("Nilay")


def say3_Hello(name="user"): # name girilmediğinde default user bastırılır
  return "Hello"+name

msg=say3_Hello("Nilay")
print(msg)


def total(valu1,value2):
  return valu1+value2
result=total(12,45)
print(result)
print(help(total)) #fonksiyon help dökümanı açıklanır


def chanegName(name):
  name="ADA"
name="Erinhan"
chanegName(name)
print(name)  #Erinhan

def change(n):
  n[0]="İstanbul"

sehirler=["ankara","izmir"]
change(sehirler) # istanbul ,izmir 
print(sehirler)

def add(a,b,c=0):  
  return sum(a,b)
print(add(10,20))   # 3 parametreli olmasına rağmen 2 parametreli çağrılardada çalışır c=0 ladığımız için

def addd(*params):
  return sum(params)
print(addd(10,20,60,90)) # bu yolla istenilen kadar değer toplanılır

def displayUser(**params): # dictionary geleceğini bildirmek için ** 
  for key,value in params.items():
    print("{} is {}".format(key,value))
  displayUser(name="Nilay",age=2,city="İzmir")


def myFunc(a,b,*args,**args2):
  print(a) #2
  print(b) #3
  print(*args) #4,5,6,7,8,9,0
  print(**args2) #key1="value 1"

myFunc(2,3,4,5,6,7,8,9,0 ,key1="value 1")


#exercise: gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın
def function1(name,time):
  print(name*time)
function1("Nilay",10)
#exercise: kendine gönderilen sınırsız sayıdaki parametreyi listeye çeviren fonksyion yaz
def function2(*args):
  liste=[]
  for i in args:
    liste.append(i)
  return liste
result=function2(10,56,78,98,0,90,89,45,"Merhaba")
print(result)

#gönderilen 2 sayı arasındaki tüm asal sayıları bulun
def function3(number1, number2):
    prime_numbers = []  # List to hold prime numbers
    for i in range(number1, number2 + 1):  # Include number2 in the range
        if i > 1:  # Check only numbers greater than 1
            isAsal = True  # Assume i is prime until proven otherwise
            for x in range(2, i):  # Check for factors of i
                if (i % x == 0):
                    isAsal = False  # i is not prime
                    break
            if isAsal:
                prime_numbers.append(i)  # Append prime number to the list
    return prime_numbers
# Example usage
print(function3(2, 5))

#kendisine gönderilen bir sayının tam bölenlerini liste şeklinde döndürün

number=input("Sayı giriniz:")
x=int(number)
list=[]
def function(x):
   for i in range(1,x):
      print(i)
      if(x%i==0):
         list.append(i)
         print(f"{i} bölünür sayıdır")
         i+=1
      else:
         print(f"{i} bölünemez sayıdır.")
         i+=1
function(x)


#Lambda expressions
def square(num): 
  return num**2
result=square(2)
print(result)
#dizi içindeki elemanları fonksiyona gönderme :
numbers=[1,2,3,4]
result=list[map(square,numbers)] # liste şeklinde döndürmek için lis() kullanılır ya da for döngüsü ile yazdırılır.
print(result)
#ismi olmayan fonksyion tanımlanabilir=lambda expression denir
numbers=[1,2,3,4]
result=list(map(lambda num:num**2,numbers)) # dizinin elemanlarını fonksiyona gönderir.
#####
square=lambda num:num**2
numbers=[1,2,3,4]
result=list(map(square,numbers))
# filter()fonksiyonuile belli değerler döndürülebilir
def check_even(num):
  return num%2==0
result=list(filter(check_even,numbers))
result=list(filter(lambda num:num%2==0),numbers)
result=check_even(numbers[2])   # false bilgisi gönderilir.

#GLOBAL -LOCAL VARIABLES:
#Fonksiyon local x varsa onu kullanır, yoksa global x i kullanır.
#fonksiyon içinde global x olarak tanımlanabilir. 



