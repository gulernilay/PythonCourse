"""
Lecture9: File Management
"""

"""
dosya erişim modlari: w(write- dosyaların içindekileri siler ve üstüne yazar ,dosyayı belirtilen konumda açar ) , a(append- dosyanın içindeki verileri silmeden yazar , dosya yoksa oluştururu) , x( dosya yaratır varsa hata verir) , r( read- dosya yoksa hata verir)

"""
#Dosya oluşturma 
file=open("newfile.txt","w") # yeni bir dosya oluşturur ve açar 
file2=open("C:/Users/nilay/desktop/newFile.txt","w")
print(file)
file.close() #dosyanın açık kalıp kaynakları tüketmesini istemeyiz 

file2=open("C:/Users/nilay/desktop/newFile.txt","w",encoding="utf-8")#encoding=karakter kodlaması türkçe karakterlerin de okunmasını sağlar 
file2.write("Sadikturan")
file2.close()

file=open("newfile.txt","a")  #contentin içine sona ekler 
file.write("\n Nilay Güler") # new line oluşturur
file.close()

file=open("newfile.txt","x",encoding="utf-8")  #x modu dosyaoluşturmak için kullanılır, içine ekleme yapılamaz
file.write("\n Nilay Güler") # new line oluşturur
file.close()

#Dosya Okuma  

try:
   file=open("newfile.txt","r",encoding="utf-8")  #mod bilgisi vermesen bile varsayılan reaad olarak atanır 
except FileNotFoundError:
   print("dosya okuma hatası")
finally:
   file.close()
   print("Dosya kapandı")
#read modunda dosyanın ilgili konumda olması gerekir yoksa exception atar
print(file)

#okuma işlemi for döngüsü ile yapılabilir
for i in file:
   print(i,end="")
file.close()

#okuma işlemi fread metotu ile yapılabilir
content=file.read()
print(content)
print("İçerik 1 ")
content2=file.read()
print(content)
print("İçerik 2 ")  #baştan okumaya başlar gaiba, dene !!!!
content=file.read(5) # ilk 5 karakterini alır (Sadık)
content=file.read(3) # ilk 5den sonraki ilk3 karakterini alır ( Tu)-boşluk + 2 harf

content=file.readline() # her seferinde bir satır okunur
print(content) #1 satırı okur
print(content) #2. satırı okur
print(content) #3. satırı okur
print(content) #4. satırı okur

liste=file.readlines()
print(liste) # liste elemanı şeklinde döndürürür
print(liste[0]) # liste elemanı şeklinde döndürürür

#Dosya Okuma Fonksiyonları:

file=open("newfile.txt","r",encoding="utf-8")
content=file.read()
print(content)
file.close()

with open("newfile.txt","r",encoding="utf-8") as file : # with open işlem bitince otomatik dosyayı kapatır 
    content=file.read()
    print(content)
    file.seek(0) #cursorı 0.konuma gönderir
    print(file.tell())#cursor konumunu verir.
    content2=file.read() # cursor devamını basar 
    print(content2)

#DosyaDA Güncelleme Yapma :
with open("newfile.txt","r+",encoding="utf-8") as file : # r+ hem okuma yapar hem yazma yapar 
    file.write("deneme") 
    file.seek(20)
    file.write("deneme2")
with open("newfile.txt","r+",encoding="utf-8") as file : # r+ hem okuma yapar hem yazma yapar 
    print(file.read())

with open("newfile.txt","a",encoding="utf-8") as file : # cursor dosyanın en sonuna gider append modu ile birlikte 
    file.write("\ndeneme") 

#Sayfa başında güncelleme
with open("newfile.txt","r+",encoding="utf-8") as file : # cursor dosyanın en sonuna gider append modu ile birlikte 
    content=file.read()
    content="Efe Turan\n" +content  #başına içerik eklenir 
    file.seek(0)
    file.write(content)
with open("newfile.txt","r+",encoding="utf-8") as file : # r+ hem okuma yapar hem yazma yapar 
    print(file.read())

#Sayfa Ortasında Güncelleme 
with open("newfile.txt","r+",encoding="utf-8") as file : # cursor dosyanın en sonuna gider append modu ile birlikte 
    content=file.readlines()
    list.insert(1,"Ali Korkmaz\n") #1.indexden önce ekleme işlemi yapar 
    file.seek(0)
    for i in list :
        file.write(i)
    print(list)
with open("newfile.txt","r+",encoding="utf-8") as file : # r+ hem okuma yapar hem yazma yapar 
    print(file.read())

