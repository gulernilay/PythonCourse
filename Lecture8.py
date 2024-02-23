#ERROR HANDLING:  

#tanımlanmamış değişkeni ekrana yazdırma
print(a)#Name Error 
#string ifadeyi integer a çevirirken:
int("1a2") #Value Error
print(10/0) #Zero Division Error 
print("denem"e) #SyntaX Error

while True:
  try:
    x=int(input("x:"))
    y=int(input("y:"))
    print(x/y)
  except ZeroDivisionError:
    print("y için 0 girilemez")
  except ValueError:
    print("x ve y için sayısal değer girilmeliir")
  except: # except çalışmazsa else çalışır 
    print("Yanlış bilgi girdiniz")
  except Exception as ex:
    print("Yanlış bilgi girdiniz,ex")
  else:
    print("Her şey yolunda")
    break
  finally: # except veya try çalışsa dahi çalışır.F
    print("try except sonlandı")

x=10
if x>5: 
      raise Exception("x 5 den büyük olamaz ")
    
def check_password(ps):
      if len(ps)<8 :
        raise Exception("Parola en az 7 karakter olmalı")
      elif not re.search("[a-z]",ps):
         raise Exception("Parola küçük haf içermelidir")
      elif not re.search("[A-Z]",ps):
         raise Exception("Parola büyük haf içermelidir")
      elif not re.search("[0-9]",ps):
         raise Exception("Parola rakam içermelidir")
      elif not re.search("\s",ps):
         raise Exception("Parola boşluk içermemelidir")
      
password="1234_89"  
try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Geçerli parola")
finally:
    print("Validation tamamlandı")

class Person:
  def __init__(self,name,year):
    if len(name)>10 :
      raise Exception("Name alanı fazla karakter içeriyor")
    else:
      self.name=name
p=Person("ALİİİİİİİİİİİİİ",1989)

# EXAMPLE: liste=["1","2","5a","10b","abc","10","50"]
#liste elemanları içindeki sayısal değerli bulunuz. 
import regex
liste=["1","2","5a","10b","abc","10","50"]
for x in liste:
     try:
          result=int(x)
          print(result)
     except ValueError:
          continue

def chekc_numbers(liste):
  if not regex.search("[0-9]",liste):
         raise Exception("Parola rakam içermelidir")
#türkçe karaker hatası ver
characters="şçüğöİ"
parola=input("Parola:")
for i in parola:
     if i in characters:
          raise TypeError("Parola türkçe karakter içermez.")
     else:
          pass
print("Geçerli parola")