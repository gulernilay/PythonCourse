"""
Lecture 4: Loops, Break&Continue , Loop Methods

"""
import random
#FOR Loops
numbers=[0,1,2,3,4,5]
names=["Ali","Veli"]

for i in numbers: #Option1
  print(i)

for a in numbers:#Option2
  print("Hello") # eleman sayısı kadar harf basılır

for x in numbers:#Option3
   print(f"My name is{x}")



tuple=(1,2,3,4,5)
for t in tuple:
    print(t)


d={"Key1":5,"key2":7}
for x in d.items():
   print(x) # key leri basar
for key,value in d.items():
   print(key,value)


#exercise:
sayilar=[1,3,5,7,9,12,19,21]
   #sayilar listesindeki hangi sayılar 3 ün katıdır?
thress=[]
sum=0
for i in sayilar:
      if(i%3==0):
         thress.append(i) 
         sum+=i      
      else:
         sum+=i  
ürünler=[
    {"name":"samsung-s6","price":"3000"},
    {"name":"samsung-s7","price":"8000"},
    {"name":"samsung-s8","price":"4000"},
    {"name":"samsung-s9","price":"5000"},
]
sum2=0
#ürün fiyat toplamı
for i in ürünler:
    print(i["price"])
    sum2+=int(i["price"])
    print(sum2)

#WHILE DONGUSU
#1-100 ARASI BASTIR 
i=0
while i in range(6):
    print(i)
    if(i==3):
        break
    else:
        continue
x=0
while x<100:
    print(x)
    x+=1
print("bitti")

name=""
while not name:
    name=input("İsminizi giriniz:")

print(f"Merhaba ,{name}")

sayilar=[1,3,5,7,9]
# while ile tüm elemanları ekrana yazdır
x=0
while x< len(sayilar):
  print(sayilar[x])
  x+=1

#başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
first=input("Başlangıç değerini giriniz:")  #1
last=input("Son değerini giriniz:") #5
a=int(first)
b=int(last)
while a<= b:
    if(int(a)%2!=0):
      print(a)
      a+=1
    else:
      a+=1

#1-100 arası azalan sırada yazdır
x=100
while x>=1:
   print(x)
   x-=1

# kullanııdan aldığın 5 sayıyı ekranda sıralı bir şekilde yazdır
x = 0
numbers_list = []  # Renamed for clarity
while x < 5:
    a = input("Enter a number: ")  # Prompt changed to English
    numbers_list.insert(x, a)  # 'list' is a built-in name, so it's better to use a different variable name
    x += 1

print(f"The numbers given by user: {numbers_list}")  # Using f-string for interpolation

numbers_list.reverse()  # Reversing the list
print("Reversed list:", numbers_list)  # Printing the reversed list

#BREAK &CONTINUE YAPISI 
name="Nilay Güler"
for letter in name:
  if(letter=="ü"):
   break
  print(letter)
  if(letter=="a"):
   continue
  print(letter)

#DÖNGÜ METOTLARI :
#1.metot(range)
for item in range(9):
  print(item)
print(list(range(5,15,2))) # gelen verileri listeye çevirir
print("bitti")
x=0
while x in range(5,10,2): # 2 şer 2 şer artsın
  print(x)

#2.metot enumarate()
greeting="Hello"
for index in enumerate(greeting):
    print(index) # index,element şeklinde açıklar 

#3. zip metotu: listeler arası eşleşme
list1=[0,1,2,3]
list2=["a","b","c","d"]
print(list(zip(list1,list2)))
for item in zip(list1,list2):
  print(item)

#List Comprehensive:
numbers=[]
for x in range(10):
  numbers.append(x)
numbers=[x for x in range(10)]
print(numbers)

for x in range(10):
    print(x**2)
numbers=[x**2 for x in range(10)]   
print(numbers)   

years=[1983,1999,2008,1956]
ages=[2019-year for year in years]
print(ages)

result=[]
for x in range(3):
   for y in range(5):
      result.append(x,y)
      print(result)

#Exercise: SAYI TAHMİN ÜRETME OYUNU- 1-100 arasında rastgele ürettir.

hak_sayisi=int(input())
tahmin_edilen_Değer=59

for i in hak_sayisi:
  print(i)
  i+=1
  x=random.randint(1,100)
  print(x)
  if(x==tahmin_edilen_Değer):
    print("Bildiniz!")
  elif(x<tahmin_edilen_Değer):
    print("Aşağı")
  elif(x>tahmin_edilen_Değer):
    print("Yukarı")
      
# sayının asal olup olmaığını kontrol et.
  print("Bir sayı giriniz.")
  x=random.randint(1,100)
  asalmi=True
  # sayımız 5 olsun , sadece 1 ve 5 e bölünebilir ama 2,3,4 bölünemez
  for i in range(2,x):
    if(x%i==0):
      asalmi=False 
      break
  if asalmi:
    print("Sayı asaldır")
  else:
    print("Sayı asal değildir")
