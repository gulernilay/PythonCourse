#Iterators: listeler iterator objelerdir ve for döngüsü ile tek tek elemanları dolaşılabilir.
"""
__iter__ metotuna sahip bir obje iterable objedir. dir(liste) fonksiyonu ile lbir objenin fonksiyonlarına bakılabilir. 
Iterator lar Java da arraylist,LinkedList,HashSet,hASHmAP için kullanılır. 
Java Iteratorlwr koleksiyonlar üzerinde döngü sağlamak için kullanılan bir araçtır.Kole

"""
liste=[1,2,3,4,5]
iterator=iter(liste)
print(next(iterator)) # her çağrılışta listenin bir elemanı karşımıza gelir.
print(next(iterator)) # 2
print(next(iterator)) # 3
print(next(iterator)) # 4
print(next(iterator)) # 5
print(next(iterator)) # Stop Iteration Hatası 

while True:
  try:
    print(next(iterator))
  except StopIteration:
    break

class MyNumbers:
  def __iter__(self):
    return self
  def __init__(self,start,stop):
    self.start=start
    self.stop=stop  
  def __next__(self):
    if self.start<=self.stop:
      x=self.start
      self.start +=1
      return x 
    else:
      raise StopIteration
list=MyNumbers(20,50)
myiter=iter(list)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

