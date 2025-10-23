sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

print("-"*30)
print("1- Toplama\n2- Çıkarma\n3- Çarpma\n4- Bölme")
print("-"*30)

secim = input("Yapmak istediğiniz işlemi seçin: ")
print("-"*30)
# türüdü bey buraya fonksiyonları tanımlayacak
def topla(sayi1,sayi2):
    return sayi1+sayi2
def çıkarma(sayi1,sayi2):
     return sayi1-sayi2
def bölme(sayi1,sayi2):
      return sayi1/sayi2
def çarpma(sayi1,sayi2):
       return sayi1*sayi2
# toplama çıkarma çarpma bölme fonksiyonlarını tamamladim 
# halit bey de aşağıdaki if else lerin içini türüdü beyin fonksiyonlarına göre düzenleyecek.
if secim == "1":
    sonuc = topla(sayi1,sayi2)
    #print(f"{sayi1} + {sayi2} = {sayi1+sayi2}")
    print(f"{sayi1} + {sayi2} = {sonuc}")
elif secim == "2":
    sonuc = çıkarma(sayi1,sayi2)
    print(f"{sayi1} - {sayi2} = {sayi1-sayi2}")
elif secim == "3":
     sonuc = çarpma(sayi1, sayi2)
    print(f"{sayi1} * {sayi2} = {sayi1*sayi2}")
elif secim == "4":
    sonuc = bölme(sayi1,sayi2)
    if (sayi2 == 0):
        print("!!! Payda sıfır olamaz !!!")
    else:
        print(f"{sayi1} / {sayi2} = {(sayi1/sayi2):.2f}")
else:
    print("!!! Hatalı seçim yaptınız !!!")
print("-"*30)
