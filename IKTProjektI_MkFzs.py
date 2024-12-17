# Molnár Krisztina Führinger Zsófia 10.c - Első Beadandó 
import random

adatok=[]
vege=1


while vege:
    if (len(adatok)==0):    
        print("========[ Válassz menüpontot! ]==========\n")
        print("[1] - tömb feltöltése billentyűzetről\n[2] - tömb feltöltése véletlen számokkal\n[3] - tömbhöz egy új elem hozzáadása\n[0] - kilépés")
    else:
        print("========[ Válassz menüpontot! ]==========\n")
        print("[1] - tömb feltöltése billentyűzetről\n[2] - tömb feltöltése véletlen számokkal\n[3] - tömbhöz egy új elem hozzáadása")
        print("[4] - a tömb egy adott sorszámú elem módosítása\n[5] - a tömb egy adott sorszámú elem törlése\n[6] - tömb ürítése\n[7] - tömb kiírása\n[8] - Feladatok\n[0] - kilépés")
   
    valasz=int(input())

    # tömb feltöltése billentyűzetről
    if (valasz==1):
        feltoltes_szama=int(input("Add meg hány számmal szeretnéd feltölteni: "))
        
        for i in range(feltoltes_szama):
            feltoltott_szamok=float(input())
            adatok.append(round(feltoltott_szamok, 2))
            
        kilepes=float(input("Ahhoz, hogy vissza lépj, írj be bármilyen számot! = "))
        
        

    # tömb feltöltése véletlen számokkal

    elif (valasz==2):
        
        veletlen_szamok=int(input("Add meg hány véletlen számmal szeretnéd feltölteni a tömböt: "))
        
        while veletlen_szamok<1:
        
            print("Helytelen válasz, próbáld újra!")
            veletlen_szamok=int(input("Add meg hány véletlen számmal szeretnéd feltölteni a tömböt: "))
            
        also_hatar=int(input("Add meg az alsó határt: "))
        felso_hatar=int(input("Add meg a felső határt: "))
        
        while also_hatar>felso_hatar:
            print("Helytelen válasz, próbáld újra!")
            also_hatar=int(input("Add meg az alsó határt: "))
            felso_hatar=int(input("Add meg a felső határt: "))
            
        for i in range(veletlen_szamok):
            
            adatok.append(random.randint(also_hatar, felso_hatar))
        
        kilepes=float(input("Ahhoz, hogy vissza lépj, írj be bármilyen számot! = "))

    # tömbhöz egy új elem hozzáadása

    elif (valasz==3):
        uj_elem=float(input("Add meg az új elemet: "))

        adatok.append(round(uj_elem))
        
        kilepes=float(input("Ahhoz, hogy vissza lépj, írj be bármilyen számot! = "))

    # a tömb egy adott sorszámú elem módosítása 

    elif (valasz==4):
        print("A tömbben lévő adatok: ")
        for i in range(len(adatok)):
            
            if (i==len(adatok)-1):
                print(adatok[i], end="")
            else:
                print(adatok[i], end=", ")
            
        adott_sorszam=int(input("\nadd meg hanyadik sorszámú elemet módositanád: "))
        
        adatok[adott_sorszam-1] = round(float(input()))

    # a tömb egy adott sorszámú elem törlése

    elif (valasz==5):
        
        print("A tömbben lévő adatok: ")
        for i in range(len(adatok)):
            
            if (i==len(adatok)-1):
                print(adatok[i], end="")
            else:
                print(adatok[i], end=", ")
        
        adott_sorszam=int(input("\nadd meg hanyadik sorszámú elemet törölnéd: "))
        
        adatok.pop(adott_sorszam-1)

    # tömb ürítése

    elif (valasz==6):
        adatok.clear()

    # tömb kiírása 
    
    elif (valasz==7):
        print("A tömbben lévő adatok: ")
        for i in range(len(adatok)):
            
            if (i==len(adatok)-1):
                print(adatok[i], end="")
            else:
                print(adatok[i], end=", ")
            
        kilepes=float(input("\nAhhoz, hogy vissza lépj, írj be bármilyen számot! = "))

    #Feadatok
    elif (valasz==8):
            if (len(adatok)==0):
                print("Először adj meg adatokat!")
                
                kilepes=float(input("\nAhhoz, hogy vissza lépj, írj be bármilyen számot! = "))
    
            else:
                print("A maximum érték hányszor fordul elő? = 1\nMekkora az adathalmaz terjedelme? = 2\nAz átlagnál kisebb, vagy az átlagnál nagyobb értékből van-e több? = 3\nTéli hónapban vagy? Van-e benne negatív hőmérséklet? = 4")
            
            valasz2=int(input())
            # 1a feladat 

            if (valasz2==1):
                max_ertek=max(adatok)
                maximum_ertekek_szama=0
                

                for i in range(len(adatok)):
                    if (adatok[i]==max_ertek):
                       maximum_ertekek_szama+=1

                print(f"{max_ertek} {maximum_ertekek_szama} alkalommal.")

                kilepes=float(input("\nAhhoz, hogy vissza lépj, írj be bármilyen számot! = "))


            # 1b feladat 

            elif (valasz2==2):
                max_ertek=max(adatok)
                min_ertek=min(adatok)
                    
                adathalmaz=max_ertek-min_ertek

                print(round(adathalmaz, 2))

                kilepes=float(input("\nAhhoz, hogy vissza lépj, írj be bármilyen számot! = "))

            # 1c feladat 

            elif (valasz2==3):
                adatok_szama=len(adatok)
                adatok_osszege=0

                for i in range(len(adatok)):
                   adatok_osszege+=adatok[i]

                atlag=adatok_osszege/adatok_szama
                        
                nagyobb_szamok=0
                kisebb_szamok=0
                        
                for i in range(len(adatok)):
                    if  (adatok[i]>atlag):
                       nagyobb_szamok+=1
                    else:
                        kisebb_szamok+=1

                if (nagyobb_szamok>kisebb_szamok):
                    print("Az átlagnál nagyobb elemekből van több.")
                else:
                    print("Az átlagnál kisebb elemekből van több.")

                        
                kilepes=float(input("\nAhhoz, hogy vissza lépj, írj be bármilyen számot! = "))

            # 1d feladat

            elif (valasz2==4):
                negatív_ertek=0
                for i in range(len(adatok)):
                    if (adatok[i]<0):
                        negatív_ertek+=1
                    
                if (negatív_ertek>0):
                    print("téli hónap.")
                else:
                    print("nem téli hónap")
                    
                kilepes=float(input("\nAhhoz, hogy vissza lépj, írj be bármilyen számot! = "))

    # kilépés

    elif (valasz==0):
        vege-=1
        