# Molnár Krisztina Führinger Zsófia 10.c - Első Beadandó 
import random

adatok=[]
vege=1


while vege:
    if (len(adatok)==0): 
        print("\n========[ Válassz menüpontot! ]==========\n")
        print("[1] - tömb feltöltése billentyűzetről\n[2] - tömb feltöltése véletlen számokkal\n[3] - tömbhöz egy új elem hozzáadása\n[0] - kilépés")
    else:
        print("========[ Válassz menüpontot! ]==========\n")
        print("[1] - tömb feltöltése billentyűzetről\n[2] - tömb feltöltése véletlen számokkal\n[3] - tömbhöz egy új elem hozzáadása")
        print("[4] - a tömb egy adott sorszámú elem módosítása\n[5] - a tömb egy adott sorszámú elem törlése\n[6] - tömb ürítése\n[7] - tömb kiírása\n[8] - Feladatok\n[0] - kilépés")
   
    valasz=int(input())

    # tömb feltöltése billentyűzetről
    if (valasz==1):
        szamok=input("Add meg a számokat vesszővel elválasztva: ").replace(" ", "").split(",")
        
        adatok=[float(i) for i in szamok]
            
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
                if (adatok[i]%1==0):
                    print(int(adatok[i]), end="")
                else:
                    print(adatok[i]*100/100, end="")
            else:
                if (adatok[i]%1==0):
                    print(int(adatok[i]), end=", ")
                else:
                    print(adatok[i]*100/100, end=", ")
            
        adott_sorszam=int(input("\nadd meg hanyadik sorszámú elemet módositanád: "))
        
        adatok[adott_sorszam-1] = round(float(input("Add meg mivel helyettesítenéd: ")))

    # a tömb egy adott sorszámú elem törlése

    elif (valasz==5):
        
        print("A tömbben lévő adatok: ")
        for i in range(len(adatok)):
            
            if (i==len(adatok)-1):
                if (adatok[i]%1==0):
                    print(int(adatok[i]), end="")
                else:
                    print(adatok[i]*100/100, end="")
            else:
                if (adatok[i]%1==0):
                    print(int(adatok[i]), end=", ")
                else:
                    print(adatok[i]*100/100, end=", ")
        
        adott_sorszam=int(input("\nadd meg hanyadik sorszámú elemet törölnéd: "))
        
        adatok.pop(adott_sorszam-1)

        print(f"{adott_sorszam}. sorszámú elem sikeresen törölve!")

        kilepes=float(input("Ahhoz, hogy vissza lépj, írj be bármilyen számot! = "))

    # tömb ürítése

    elif (valasz==6):
        biztos_kerdes=int(input())

        if (biztos_kerdes==1):
            adatok.clear()
        else:
            kilepes=float(input("Ahhoz, hogy vissza lépj, írj be bármilyen számot! = "))

    # tömb kiírása 
    
    elif (valasz==7):
        print("A tömbben lévő adatok: ")
        for i in range(len(adatok)):
            
            if (i==len(adatok)-1):
                if (adatok[i]%1==0):
                    print(int(adatok[i]), end="")
                else:
                    print(adatok[i]*100/100, end="")
            else:
                if (adatok[i]%1==0):
                    print(int(adatok[i]), end=", ")
                else:
                    print(adatok[i]*100/100, end=", ")
            
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
                max_ertek=0
                maximum_ertekek_szama=0
                
                for i in range(len(adatok)):
                    if (adatok[i]>adatok[max_ertek]):
                        max_ertek=i
                

                for i in range(len(adatok)):
                    if (adatok[i]==max_ertek):
                       maximum_ertekek_szama+=1

                print(f"{max_ertek} {maximum_ertekek_szama} alkalommal.")

                kilepes=float(input("\nAhhoz, hogy vissza lépj, írj be bármilyen számot! = "))


            # 1b feladat 
            
            # 27.3, 26.8, 25.7, 26.3, 27.3, 27.2, 27, 27.3

            elif (valasz2==2):
                max_ertek=0
                min_ertek=0
                
                for i in range(len(adatok)):
                    if (adatok[i]>adatok[max_ertek]):
                        max_ertek=i
                        
                for i in range(len(adatok)):
                    if (adatok[i]<adatok[min_ertek]):
                        min_ertek=i
                    
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
                    print(f"Az átlagnál nagyobb elemekből van több.\nAz átlag: {atlag}. ")
                else:
                    print(f"Az átlagnál kisebb elemekből van több.\nAz átlag: {atlag}.")

                        
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
        