""""
Lecture 1 : Data Types ,String Methods, Lists, Dictionaries , Sets, Tuples 
"""
#Numbers : Float and Integer
print(2+2) # 4
print(2*10) # 20 
print(2*"Nilay") #NilayNilay
print(type(10.5)) # Float
isStudent=True#bool
# + , - , * , /(division with remainder) , // (division without remainder) ,%(mod)
print(11//2)#5
print(11/2)#5.5

#Variable Declaration Rules : 
_a=5#(acceptable)
iğ=6# No turkish character usage + Uppercase/Lowercase letter sensitivity
a= "10" #string
b= 5#integer 
print(a+str(b))#Concetanation of string variables
x,y,z=(4,10,"Nilay")#declaration of more than 1 variables in 1 sentence


#Take input from user (Scanner in Java)
x=input("Sayı giriniz") #for ex:45
print(x)
print(int(x))#convert into int - > 45
print(str(x))#convert into string->"45"
print(float(x))#convert into float -> 45.0
print(bool(a))#True if it is string , 1 if it is integer 

# String : 
name ="Nilay"
surname="Lale"
print("Name:" +name +" " +"Surname:" +surname+" "+"\n I am 23 years old.")# \n is used for new line 
sentence="Ali Babanın Çiftliği"
print("My name is {} {}".format(name,surname))
print(f"My name is {name} {surname}") #Nilay Lale
print("My name is {1}{0}".format(name,surname))#Lale Nilay
print("My name is {s} {n}".format(s=name,n=surname))

print(len(sentence))
print(len(sentence[:5])) # the first 5 character in sentence 
print(len(sentence[1])) # the first character in sentence
print(len(sentence[1:10:2])) # from first character until 10.character by passing 2 character

website="http://www.google.com"
print(len(website))
print(website[::-1]) # tersten yazdır 

#exercise: exchange "W" with "x" in "Hello World" 
string="Hello World" # string[7]="x" is not applicable 
string = string[0:6] + "x" + string[-5:]
print(string)

#STRING Methods
string2="Hello there. My name is Yalin."
print(string2.upper())#
print(string2.lower())
print(string2.title())# make uppercase letter of each word - "Hello There. My Name Is Yalin."
print(string2.capitalize)#Hello there. my name is nilay güler

print(string2.find("Hello"))#0
isFound=string2.startswith("I")#False
isFound=string2.endswith("I")#False
isFound=string2.replace("Hello","Jamble")# "Jamble there. My name is Yalin."

sentence="Hello World"
sentence2=sentence.strip("Hello ")
print(sentence2)

#SETS :(Kümeler) -sıralama önemli değildir, tekrarlayan elemanlar 1 kez yazılır. 
fruits={"ali","veli","nilay"}  #sıralama önemli değil,tekrarlayan elemanlar 1 kez yazılır 
print(fruits) 
# fruits[0]=6  #çalışmaz 
# fruits[4]="Ali"
for i in fruits:
  print(i)
fruits.add(9)
fruits.update(["nilay","tarık","erinhan"]) #liste içinde gönderilebilir
fruits.remove("nilay")
fruits.discard("erinhan")
fruits.clear() # kkomple temizler 
print(fruits)
my_List=[1,2,3,4,5,1,2,3,4,5]
print(set(my_List)) # convert list to set  ,her eleman sadece 1 kere yazılacak 




#Dictionary - key,value
sehirler=["kocaeli" ,"istanbul"]
plakalar=[41,34]
plakalar[sehirler.index("kocaeli")] # dictionar olmadan listelerle nasıl sonuca ulaşırız

dict={" Kocaeli":4,"İstanbul":5}
print(dict[" Kocaeli"]) # 4 
dict["İZMİR"]=3
dict={"Nilay Güler":{"AGE" :36,"heiht":"168"},"Ümmü Güler":{"AGE" :50,"heiht":"162"}}
print(dict["Nilay Güler"]["AGE"])

#EXAMPLE:DICTIONARY
name_list=[]
surname_list=[]
tel_list=[]
student_no_list=[]
#Kullanıcıdan isim ,soyisim,tel al
for i in range(3):
  name=input("Name: ")
  surname=input("Surname: ")
  tel=input("tel:")
  student_no=input("Student No:") # keys
  print(name,surname,tel,student_no)
  name_list.append(name)
  surname_list.append(surname)
  tel_list.append(tel)
  student_no_list.append(student_no)

# Sözlük oluştur
student_dict = {
    student_no_list[0]: {"Name": name_list[0], "Surname": surname_list[0], "Telephone": tel_list[0]},
    student_no_list[1]: {"Name": name_list[1], "Surname": surname_list[1], "Telephone": tel_list[1]},
    student_no_list[2]: {"Name": name_list[2], "Surname": surname_list[2], "Telephone": tel_list[2]}
}
print(student_dict)

student_dict={'67': {'Name': 'Nilay', 'Surname': 'Güler', 'Telephone': '20180612003'}, '123': {'Name': 'Irmak', 'Surname': 'Atıcı', 'Telephone': '6789062'}, '90': {'Name': 'Osman', 'Surname': 'Doluca', 'Telephone': '789453628'}}
#öğrenci numarasını kullanıcıdan al ve ilgili öğreni bilgisini göster
number=input("Student Number: ")

# İlgili öğrenci bilgisini göster
if number in student_dict:
    student_info = student_dict[number]
    print(f"Name: {student_info['Name']}, Surname: {student_info['Surname']}, Telephone: {student_info['Telephone']}")
else:
    print("Bu numaraya sahip bir öğrenci bulunamadı.")


#TUPLES:
list=[1,2,3]
tuple=(1,"İKİ",3)
type(tuple)
#tuple da tuple[0]="Ayşe" gibi eleman ataması yapılamaz
tuple.index(1)
tuple.count("ahmet")
tuple2=2*tuple
print(tuple2)



#LISTS IN PHYTON -   sentence=sentence.strip()  sonucunda list açığa çıkar 
my_List=[1,2,True,"Ali",5.6]
my_List2=[3,88,False]
print(my_List +my_List2)
len(my_List2)
#liste içinde liste saklama 
user1=["Nilay", 24]
user2=["Veli" , 45]
total=[user1] +[user2]
print(total)
print(total[0]) # ['Nilay', 24]    
print(total[0][1])#24
print(total[1][0])# "Çınar "


#example :
list=["BMW" ,"MERCEDES","MAZDA"]
list[2]="TOYOTA"
x = list[:3] # ilk 3 elemanını alın 
list[-2]="Toyota"#son 2 elemanını değiştirme
list[-1]="opel"
result="Mercedes" in list   # mercedes bu listede var mı?
list[-2:]=["Toyota","Renault"] # son 2 elemanını değiştirme 
list+["Toyota" ,"Nissan"] # değer ekleme
del list[-1] # son elemanı silme 


numbers=[0,1,2,3,4,5]
letter=["a","j","l"]
x=min(numbers)
y=max(numbers)
z=max(letter) # alfabetik en sonki sırada olandır.
numbers[3:6] # 3-5.indexe kadar
numbers[4]=40
numbers.append(6)
numbers.insert(3,78) # 3.indexe 78 rakamı ekler 
numbers.pop(3) # 3.index silinir
numbers.remove(2) # listeden 2 yi siler
numbers.sort()
numbers.reverse()
numbers.count(0) # 0 dan kaç tane var
numbers.clear() # listeyi temizler 

names=["Ali" ,"Yağmur", "Hakan","Deniz"]
years=[1998,2000,1998,1987]
#Cenk ismini ekle 
names.append("Cenk")
names[0]="Sena"
names.remove("Deniz")
result="Ali" in names
print(result)
years.reverse()
years.sort()
# kullanıcıdan alacağın 3 tane marka bilgisini listede sakla
list=[]
brand1=input("marka1: ")
list.append(brand1)
brand2=input("marka2: ")
list.append(brand2)
# str= Chevrolet, Dacia liste çevir.
str="Chevrolet, Dacia"
result=str.split(",")






























