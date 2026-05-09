import random
import time
import numpy
import math
import sys

print("hesap makinesine hoş geldiniz")

yapilan_islemler = []
sayilar = []

while True:
    yapilacak_islem = int(input("""Hesap makinesine hoş geldiniz. Lütfen aşşağıdan yapmak istediğiniz işlemi seçiniz
1- Toplama
2- Çıkarma
3- Çarpma
4- Bölme
5- Üslü sayı alma
6- bir sayının faktoriyelini alma
7- Yüzde hesaplama işlemleri
8- Kuralları gör
9- Çıkış
10- Yapılan işlemleri görüntüle
Seçiminiz: """))
    if yapilacak_islem == 1:
        yapilan_islemler.append("Toplama işlemi")
        print("toplama aracına hoş geldiniz.")
        while True:
            toplama_girdisi = input("bir sayı girin veya çıkmak için 'q' yazın")
            if toplama_girdisi.lower() == "q":
                print("programdan çıkılıyor...")
                break
            try:
                sayi = float(toplama_girdisi)
                sayilar.append(sayi)
            except ValueError:
                print("sayı giriniz (lütfen)")
            toplam = sum(sayilar)
        print(f"girdiğiniz sayılar: {sayilar}")
        print(f"cevabınız: {toplam}")
        yapilacak_islem = input("programdan çıkmak için 'q' yazınız. devam etmek isterseniz boş bırakabilirsiniz")
        yapilacak_islem = yapilacak_islem.lower()
        if yapilacak_islem == "q":
            print("programdan çıkılıyor. Programı kullandığınız için teşekkür ederim.")
            break
    elif yapilacak_islem == 2:
        yapilan_islemler.append("Çıkarma işlemi")
        print("""Çıkarma aracına hoş geldiniz.
(toplama programı gibi istediğiniz kadar sayı girememektedisiniz. Bu eksikliğimizden dolayı özür dileriz. En kısa zamanda düzelteceğiz)""")
        birinci_sayi = input("lütfen ilk sayıyı giriniz (çıkmak için 'q')")
        if birinci_sayi == "q":
            print("""programdan çıkııyor. İyi günler dileriz.""")
            break
        birinci_sayi = float(birinci_sayi)
        ikinci_sayi = float(input("Lütfen ikinci sayıyı giriniz: "))
        ucuncu_sayi = float(input("var ise üçüncü sayıyı giriniz yok ise 0 yazınız: "))
        dorduncu_sayi = float(input("var ise dördüncü sayıyı giriniz yok ise 0 yazınız: "))
        sayi = birinci_sayi - ikinci_sayi - ucuncu_sayi - dorduncu_sayi
        print(f"girdiğiniz sayılar: {birinci_sayi, ikinci_sayi, ucuncu_sayi, dorduncu_sayi}")
        print(f"cevabınız: {sayi}")
        yapilacak_islem = str(input("Programdan çıkmak için 'q' yazınız. Devam etmek isterseniz enter tuşuna basın"))
        yapilacak_islem = yapilacak_islem.lower()
        if yapilacak_islem == "q":
            break
    elif yapilacak_islem == 3:
        yapilan_islemler.append("çarpma işlemi")
        print("çarpma operatörüne hoş geldiniz.")
        carpma = 1
        while True:
            yapilacak_islem = input("Lütfen sayı giriniz. Çıkmak isterseniz 'q' yazınız: ")
            if yapilacak_islem.lower() == "q":
                print("programdan çıkılıyor. Kullandığınız için teşekkür ederim.")
                break
            sayi = float(yapilacak_islem)
            sayilar.append(sayi)
        print(f"girdiğin sayılar: {sayilar}")
        cevap = numpy.prod(sayilar)
        print(f"cevabınız: {cevap}")
        yapilacak_islem = input("devam etmek isterseniz Enter tuşuna basmanız yeterli olacaktır. Çıkmak için ie 'q' yazınız ")
        if yapilacak_islem == "q":
            print("programdan çıkılıyor. Programı kullandığınız için teşekkür ederiz.")
            break
    elif yapilacak_islem == 4:
        yapilan_islemler.append("Bölme işlemi")
        print("bölme operatörüne hoş geldiniz.")
        print("bölme işlemlerinde birden fazla sayıyı bölmezsiniz. Lütfen 0 kullanmayınız hata ile sonuçlanacaktır.")
        try:
            birinci_sayi = float(input("Lütfen birinci sayıyı giriniz (bir sayı 0'ı bölemez ve 0'a bölünemez): "))
            ikinci_sayi = float(input("lütfen ikinci sayıyı giriniz: "))
            cevap = birinci_sayi / ikinci_sayi
            print(f"cevabınız: {cevap}")
            yapilacak_islem = input("programdan çıkmak isterseniz 'q' yazınız. Devam etmek isterseniz Enter tuşuna basınız")
        except (ValueError, ZeroDivisionError):
            print("bir hata oluştu")
    elif yapilacak_islem == 5:
        yapilan_islemler.append("Üslü sayı alma")
        print("üslü sayı alma operatörüne hoş geldiniz.")
        try:
            birinci_sayi = float(input("Lütfen taban olan sayıyı giriniz (çıkmak için'q'):"))
            if birinci_sayi == "q":
                print("programdan çıkılıyor. Kullandığınız için teşekkür ederiz.")
                break
            ikinci_sayi = float(input("Lütfen kuvvet olan sayyı giriniz: "))
            cevap = birinci_sayi**ikinci_sayi
            print(f"sorunuzun cevabı: {cevap}")
            yapilacak_islem = input("çıkmak isterseniz 'q' yazmanız yeterli olacaktır. Devam etmek isterseniz Enter tuşuna basınız: ")
            if yapilacak_islem == "q":
                print("programdan çıkılıyor. Programı kullandığınız için teşekkür ederim.")
                break
        except ValueError:
            print("lütfen sayı giriniz. Harf değil.")
    elif yapilacak_islem == 6:
        yapilan_islemler.append("Faktoriyel alma")
        print("faktoriyel alma operatörüne hoş geldiniz.")
        sayi = int(input("lütfen sayıyı giriniz: "))
        faktoriyel = math.factorial(sayi)
        print(f"girdiğiniz sayı: {sayi}! cevabınız: {faktoriyel}")
        yapilacak_islem = input("Programdan çıkmak isterseniz 'q' yazmanız yeterli olacaktır. devam etmek isterseniz Enter tuşuna basınız: ")
        if yapilacak_islem == "q":
            print("programdan çıkılıyor. Programı kullandığınız için teşekkür ederiz")
            break
    elif yapilacak_islem == 7:
        yapilan_islemler.append("yüzde hesaplama")
        print("yüzde hesaplama operatörüne hoş geldiniz")
        birinci_sayi = float(input("Lütfen yüzdesi alınacak sayıyı giriniz: "))
        ikinci_sayi = float(input("Lütfen bu sayının yüzde kaçını almak istediğinizi yazınız: "))
        x= birinci_sayi * ikinci_sayi
        y = x / 100
        print(f"{birinci_sayi} sayısının yüzde {ikinci_sayi}'si kaç ediyor. sorusunun cevabı: {y}")
        yapilacak_islem = input("çıkmak isterseniz 'q' yazmanız yeterli olacaktır. devam etmek isterseniz Enter tuşuna basınız: ")
        if yapilacak_islem == "q":
            print("programı kullandığınız için teşekkür ederiz. İyi günler dileriz.")
            break
    elif yapilacak_islem == 8:
        yapilan_islemler.append("kuralları görüntüle")
        print("""Kurallara hoş geldiniz 
Matematiksel işlemlerde işlemlerin soldan sağa doğru yapıldığını unutmayın. Programda sizden istenilen veri harici bir veri girmeyin program hata verecektir.
Programda Faktoriyel alma işlemlerinde negatif sayılar girmeyiniz program hata verecektir. Bölme işlemlerinde 0 girmeyiniz aynı şekilde program yine hata verecektir.
Tekrardan programı kullandığınız için teşekkür ederim. İyi günler""")
    elif yapilacak_islem == 9:
        print("programdan çıkılıyor. Programı kullandığınız için teşekkür ederiz.")
        for cikis in range(1,4):
            time.sleep(1)
            print(cikis)
        break
    elif yapilacak_islem == 10:
        print(f"yaptığınız işlemler {yapilan_islemler}")