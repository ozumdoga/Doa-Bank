print("""************** 

 Doa Bank ATM'sine Hoş geldiniz...

 İşlemler

 1.İşlem:Bakiye Sorgulama   
 2.İşlem:Para yatırma
 3.İşlem:Para çekme

 Programdan çıkmak için "q" ya basınız.
 
 ************** """)

bakiye = 1000

while True:
    islem = input("İşlem giriniz: ")

    if (islem == "q"):
        print("Yine bekleriz...")
    elif (islem == "1"):
        print("Hesabınızdaki bakiye:{}".format(bakiye))
    elif (islem == "2"):
        artan_bakiye = int(input("Eklemek istediğiniz bakiyeyi giriniz: "))
        bakiye += artan_bakiye
        print("Yeni bakiyeniz : {}".format(bakiye))
    elif (islem == "3"):
        azalan_bakiye = int(
            input("Nakit çekmek istediğiniz bakiyeyi giriniz:  "))
        if azalan_bakiye < bakiye:
            bakiye -= azalan_bakiye
            print("Yeni bakiyeniz : {}".format(bakiye))
        elif bakiye == 0:
            print("Yetersiz bakiye...")
        else:
            parayetersiz = input(
                "Bakiyeniz yetersiz olduğu için hesabınızdan {} çekebileceksiniz.Onaylıyor musunuz?\nOnaylıyorsanız E'ye basınız.\nOnaylamıyorsanız H'ye basınız.".format(bakiye))
            while True:
                if parayetersiz == "h":
                    print("İşlem iptali...")
                    break
                elif parayetersiz == "e":
                    bakiye -= azalan_bakiye
                    print("Paranızı çıkıştan alabilirsiniz.\nBakiyeniz= 0 TL")
                    break
                else:
                    print("Geçersiz işlem girdiniz...")
    else:
        print("Geçersiz İşlem...")
