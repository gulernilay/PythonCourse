"""
Modüller /lib klasörü altında tutulur.math modüllerini falan python bu klasör ltında arar.
MODULLER: Hazır Modüller-Kendi Modüllerimiz
Hazır Modüller: Standart Kütüphane Modülleri,3.şahıs Modülleri(pypi.org)-pip install package-name
Progamın parçalara=modüllere ayrılması , her parça =.py uzantılı dosyalardır. 
main.py olucak ve ekstra moduleA.py,moduleB.py,moduleC.py
"""
#HAZIr MODUL KULLANIMI-MATH MODULU
import math #kullanım1 
value=dir(math)
print(value) # math modül içindeki tüm fonksiyonlar gelir
print(help(math))#fonksyionların alacağı değerler vs
value=math.sqrt(49) #7
value=math.factorial(5)
value=math.floor(5.7)
value=math.ceil(5.9)
import math as işlem #kullanım2
value=işlem.ceil(5.9)
from math import *  # tüm fonksiyonlar import edilir.
value=factorial(9)

from math import factorial,sqrt #belirli fonksiyonları import edebilirsin
# şimdi bu dosya içinde de sqrt() fonksyionu tanımlasaydım eğer :
def sqrt(x):
  print(x)  # ilk math sqrt yazıldığı için o işleme alınır ama def sqrt() yukarıda tanımlansaydı o işleme alıncaktı

#HAZIr MODUL KULLANIMI-RANDOM MODULU  
import random
x=dir(random)
x=help(random)
x=random.random() #0.0-1.0 arası sayı üret
x=random.random()*100 +10
x=random.uniform(1,10) #float sayı üretir
x=random.randint(1,100) #int sayı üretir
names=[1,2,6,7,9,10]
result=names[random.randint(0,len(names)-1)] #kullanım1
result=random.choice(names) #kullanım2
print(result)
liste=list(range(10)) #0-10 arası sayı üret listeye çevir  - [0,1,2,3,4,5,6,7,8,9]
random.shuffle(liste) #elemanlar random sıralanır

liste=range(10)
result=random.sample(liste,2) # bu listeden random seçer 2 eleman

 






