# Pythonla Sanal Market
patates_toplam_fiyat = 0
patlican_toplam_fiyat = 0
elma_toplam_fiyat = 0
armut_toplam_fiyat = 0
domates_toplam_fiyat = 0
while True:
    print("************************")
    print("Marketimize Hoş Geldiniz")
    print("************************")

    print("Ne almak isterdiniz")
    print("--------------------")
    print("1- Patates")
    print("2- Domates")
    print("3- Elma")
    print("4- Armut")
    print("5- Patlıcan")
    print("6- Tutarı Sorğulamak")
    print("7- Çıkış\n")

    i = int(input("Almak için seçin: "))

    # Patatesin Kodları

    if i == 1:
        print("--------------------")
        print("Fiyat = 18TL")
        patates = int(input("Kaç kilo patates istersin: "))
        print("--------------------")
        patates_toplam_fiyat = patates * 18
        print("Tutar: " + str(patates_toplam_fiyat) + "TL")
        input("Geri dönmek için entere basınız...")

    # Domatesin Kodları

    if i == 2:
        print("--------------------")
        print("Fiyat = 25TL")
        domates = int(input("Kaç kilo domates istersin: "))
        print("--------------------")
        domates_toplam_fiyat = domates * 25
        print("Tutar: " + str(domates_toplam_fiyat) + "TL")
        input("Geri dönmek için entere basınız...")

    # Elma Kodları

    if i == 3:
        print("--------------------")
        print("Fiyat = 30TL")
        elma = int(input("Kaç kilo elma istersin: "))
        print("--------------------")
        elma_toplam_fiyat = elma * 30
        print("Tutar: " + str(elma_toplam_fiyat) + "TL")
        input("Geri dönmek için entere basınız...")

    # Armut Kodları

    if i == 4:
        print("--------------------")
        print("Fiyat = 25TL")
        armut = int(input("Kaç kilo armut istersin: "))
        print("--------------------")
        armut_toplam_fiyat = armut * 25
        print("Tutar: " + str(armut_toplam_fiyat) + "TL")
        input("Geri dönmek için entere basınız...")

    # Patlıcan Kodları

    if i == 5:
        print("--------------------")
        print("Fiyat = 25TL")
        patlican = int(input("Kaç kilo patlıcan istersin: "))
        print("--------------------")
        patlican_toplam_fiyat = patlican * 25
        print("Tutar: " + str(patlican_toplam_fiyat) + "TL")
        input("Geri dönmek için entere basınız...")

    # Tutar Sorğulama

    if i == 6:
        toplam = patates_toplam_fiyat + domates_toplam_fiyat + elma_toplam_fiyat + armut_toplam_fiyat + patlican_toplam_fiyat
        print("Toplam Tutar: " + str(toplam))
        input("Geri dönmek için entere basınız...")
    
    if i == 7:
        exit()

