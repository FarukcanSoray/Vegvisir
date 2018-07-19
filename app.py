from database import *

print("""
İşlemler:

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil

5. Baskı Yükselt

Çıkmak için 'q'ya basın.
""")

kutuphane = Database()
kutuphane.find_last_offer()
while True:
    islem = input("Yapacağınız İşlem:")

    if islem == 'q':
        print("Program sonlandırılıyor")
        break

    elif (islem == '1'):
        kutuphane.kitaplari_goster()
        print(kutuphane.isim_otomatik_tamamla_liste_olustur())

    elif (islem == '2'):
        print("""
Sorgulama
---------
1. İsim Sorgusu

2. Yazar Sorgusu

3. Yayınevi Sorgusu

4. Tür Sorgusu
        """)
        sorgu = input("Sorgu tipini seçiniz: ")

        if(sorgu == '1'):
            isim = input("Aramak istediğiniz kitap ismini girin: ")
            kutuphane.kitap_sorgula(isim, "isim")

        elif(sorgu == '2'):
            yazar = input("Aramak istediğiniz yazar ismini girin: ")
            kutuphane.kitap_sorgula(yazar, "yazar")

        elif(sorgu == '3'):
            yayinevi = input("Aramak istediğiniz yayınevi ismini girin: ")
            kutuphane.kitap_sorgula(yayinevi, "yayinevi")

        elif(sorgu == '4'):
            tur = input("Aramak istediğiniz türü girin: ")
            kutuphane.kitap_sorgula(tur, "tur")

        else:
            print("Geçersiz giriş.")

    elif (islem == '3'):
        date = input("Tarih: ")
        company = input("Firma: ")
        contact = input("Yetkili: ")
        telephone = input("Telefon: ")
        mail = input("Mail: ")
        address = input("Adres: ")
        remindTime = int(input("Hatirlatma Suresi: "))
        new_offer = Offer(date, company, contact, telephone, mail, address, remindTime)
        kutuphane.add_offer(new_offer)

    elif (islem == '4'):
        isbn = input("Silmek istediğiniz kitabın ISBN numarasını girin: ")
        kutuphane.kitap_sil(isbn)


    elif (islem == '5'):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz: ")
        kutuphane.baski_yukselt(isim)

    else:
        print("Geçersiz İşlem.")
