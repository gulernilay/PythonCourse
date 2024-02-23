"""
Lecture3:   Conditional Blocks
"""
password=input()
if True:
  print("Hoş Geldiniz")
  if (password=="1234"):
      print("Parola doğru")
  else:
     print("Parola Yanlış")
else:
   print("Username ya da parola yanlış")    
  #example:
   #trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız:

import datetime
x=input("aracnız hangi trihte trafğe çıktı:(gün /ay /yıl)")
x=x.split("/")
print(x[0]) #yıl
print(x[1])#ay
#şuandakizamanı çekmek için 
now=datetime.datetime.now
