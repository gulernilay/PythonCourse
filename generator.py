"""
Generator bellekte yer işgal etmeyen iteratör üretir.
Python'da bir generator (üreteç), büyük veri setleri ile çalışırken hafıza kullanımını optimize etmek için kullanılan bir araçtır. 
Generator'ler, yield ifadesi kullanılarak tanımlanır ve çağrıldıklarında veriyi adım adım üretirler. 
Bu, sadece ihtiyaç duyduğunuz veriyi anında üretebilir ve bellek üzerindeki yükü azaltabilir. İşte basit bir Python generator örneği:



"""
# Bir sayı dizisinin karelerini üreten bir generator fonksiyonu
def kareleri_uret(n):
    for i in range(n):
        yield i ** 2

# Generator fonksiyonunu kullanma
for kare in kareleri_uret(10):
    print(kare)
#başka bir kullanım
def cube():
    for i in range(5):
        yield i**2
generator=cube()
iterator=iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))