"""
#encapsulation
def outer(num1):
  print("outer")
  print(num1)
  def inner(num1):
    print("inner")
    num1+=5
    return num1
  num2=inner(num1)
  print(num2)
outer(6)

#recursive function:
def factorial(number):
  if not isinstance(number,int):
    raise TypeError("number must be integer")
  if not number>=0:
    raise ValueError("number must be positive or bigger zero")
  def inner_factorial(number):
    if number<=1:
      return 1
    return number*inner_factorial(number-1)
  return inner_factorial(number)
try:
  print(factorial(6))
except Exception as e:
  print(e)

#Fonksiyondan Fonksiyon Döndürme:
def usalma(number):
    def inner(power):
      return number**power
    return inner
  
two=usalma(2)  # 2 üzeri 3 oldu
print(two(3))

def yetki_sorgula(page):
  def inner(role):
    if role=="Admin":
      return "{0} rolü{1} sayfasına ulaşabilir.".format(role,page)
    else:
      return "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)
  return inner
user1= yetki_sorgula("Product Edit")
print(user1("Admin"))
print(user1("User"))

def islem(islem_Adi):
  def toplama(*args):
    toplam=0
    for i in args:
      toplam+=i
    return toplam
  def carpim(*args):
    carpim=1
    for i in args:
      carpim*=i
    return carpim
  if islem_Adi=="toplama":
    return toplama
  else:
    return carpim
  
toplama=islem("toplama")
print(toplama(1,3,5,7,9))
carpim=islem("carpim")
print(toplama(1,3,5,7,9))


#Functions as parameters:
def toplama(a,b):
  return a+b
def cikarma(a,b):
  return a-b
def carpma(a,b):
  return a*b

def islem(f1,f2,f3,islem_adi):
  if islem_adi=="toplama":
    print(f1(2,3))
  elif islem_adi=="cikarma":
    print(f1(5,3))
  elif islem_adi=="carpma":
    print(f1(3,4))
  else:
    print("geçersiz işlem...")
islem(toplama,cikarma,carpma,"toplama") #toplama çalıştırılır


#DECORATOR FUNCTIONS: bir başka fonksyionu alarak işlevini değiştiren, ekstra işlevsellik katan , bir işlevi veya fonksiyonu sarar .Kod tekrarının önüne geçildi.Bir çok farklı fonksiyon içinde yapılan aynı işlemler tek bir decorator fonksiyonu içinde toplanarak kod tekrarı engellenir. 

def my_Decorator(func):
  def wrapper():
    print("fonksiyondan önceki işlemler")
    func()
    print("fonksiyondan sonraki işlemler" )
  return wrapper

@my_Decorator
def sayHello():
  print("Hello")
def sayGreeting():
  print("greeting")

sayHello=my_Decorator(sayHello)   #yerine sayHello üstüne @my_Decorator yazdığında göndermiş oluyor 
sayHello() 

"""
import math
import time

def calculate_Time(func):
  def wrapper(*args,**kwargs):
    start=time.time()
    time.sleep(1)
    func(*args,**kwargs)
    finish=time.time()
    print(str(finish-start) +"saniye sürdü")
  return wrapper
@calculate_Time
def usalma(a,b):
  #start=time.time()
  #time.sleep(1)
  print(math.pow(a,b))
  #finish=time.time()
  #print(str(finish-start) +"saniye sürdü")
@calculate_Time
def faktoriyel(num):
  #start=time.time()
  #time.sleep(1)
  print(math.factorial(num))
  #finish=time.time()
  #print(str(finish-start) +"saniye sürdü")

usalma(2,3)
faktoriyel(5)


