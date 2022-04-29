import time
import random

tahminHakki=5
sayi=random.randint(1,100)

print("sayi tahmin oyununa hosgeldiniz.. 1 ve 100 arasında bir sayi tuttum. 5 adet tahmin etme hakkınız var.")
time.sleep(2)

while True:
    girilenSayi=int(input("tahmininiz nedir:  "))

    if sayi==girilenSayi:
        print("sayi kontrol ediliyor..")
        time.sleep(1)
        print("tebrikler! dogru sayi")
        break
    
    elif sayi < girilenSayi:
        print("sayi kontrol ediliyor..")
        time.sleep(1)
        print("daha kucuk bir sayi tahmin etmistim aslinda..")
        tahminHakki-=1
        print("kalan tahmin hakki: ", tahminHakki)
    
    elif sayi > girilenSayi:
        print("sayi kontrol ediliyor..")
        time.sleep(1)
        print("yuksek bir sayi girsen daha iyi olur :)")
        tahminHakki-=1
        print("kalan tahmin hakki: ", tahminHakki)

    if tahminHakki==0:
        print("maalesef bulamadın ve oyun bitti.")
        print("dogru cevap: ", sayi)
        break
