# Molnár Krisztina Führinger Zsófia 10.c - Első Beadandó 
import random

adatok=[]
vege=1


while vege:
    if (len(adatok)==0): 
        print("\n========[ FŐMENÜ ]==========\n")
        print("[1] - tömb feltöltése billentyűzetről\n\n[2] - tömb feltöltése véletlen számokkal\n\n[3] - tömbhöz egy új elem hozzáadása\n\n[0] - kilépés\n")
    else:
        print("\n========[ FŐMENÜ ]==========\n")
        print("[1] - tömb feltöltése billentyűzetről\n\n[2] - tömb feltöltése véletlen számokkal\n\n[3] - tömbhöz egy új elem hozzáadása\n")
        print("[4] - a tömb egy adott sorszámú elem módosítása\n\n[5] - a tömb egy adott sorszámú elem törlése\n\n[6] - tömb ürítése\n\n[7] - tömb kiírása\n\n[8] - Feladatok\n\n[0] - kilépés\n")
   
    valasz=int(input())

    # tömb feltöltése billentyűzetről
    if (valasz==1):
        szamok=input("\nAdd meg a számokat vesszővel elválasztva: \n").replace(" ", "").split(",")
        
        adatok=[float(i) for i in szamok]
            
        kilepes=float(input("Ahhoz, hogy vissza lépj, írj be bármilyen számot! = "))
        
        

    # tömb feltöltése véletlen számokkal

    elif (valasz==2):
        
        veletlen_szamok=int(input("\nAdd meg hány véletlen számmal szeretnéd feltölteni a tömböt: "))
        
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

    elif (valasz==4 and len(adatok)!=0):
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

    elif (valasz==5 and len(adatok)!=0):
        
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

    elif (valasz==6 and len(adatok)!=0):
        biztos_kerdes=int(input("Biztosan űriteni akarod? ha igen, írd be hogy 1\n"))

        if (biztos_kerdes==1):
            adatok.clear()
            print("A törlés sikeres!")
            
            kilepes=float(input("Ahhoz, hogy vissza lépj, írj be bármilyen számot! = "))

            
    # tömb kiírása 
    
    elif (valasz==7 and len(adatok)!=0):
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
    elif (valasz==8 and len(adatok)!=0):
        valasz2=""
        while (valasz2!=0):
            if (len(adatok)==0):
                print("Először adj meg adatokat!")
                
                kilepes=float(input("\nAhhoz, hogy vissza lépj, írj be bármilyen számot! = "))
    
            else:
                print("\n========[ FELADATOK ]==========\n")
                print("[1] - A maximum érték hányszor fordul elő?\n\n[2] - Mekkora az adathalmaz terjedelme?\n\n[3] - Az átlagnál kisebb, vagy az átlagnál nagyobb értékből van-e több?\n\n[4] - Téli hónapban vagy? Van-e benne negatív hőmérséklet?\n\n[0] - vissza a főmenüne.\n")
            
            valasz2=int(input())
            # 1a feladat 

            if (valasz2==1):
                max_ertek=0
                maximum_ertekek_szama=0
                
                for i in range(len(adatok)):
                    if (adatok[i]>adatok[max_ertek]):
                        max_ertek=i
                

                for i in range(len(adatok)):
                    if (adatok[i]==adatok[max_ertek]):
                       maximum_ertekek_szama+=1

                print(f"\nA maximum érték a következő volt: {adatok[max_ertek]}")
                print(f"\nEnnyi alkalommal fordult elő: {maximum_ertekek_szama}")

                kilepes=float(input("\nAhhoz, hogy vissza lépj, írj be bármilyen számot! = "))


            # 1b feladat 
            
            # 27.3, 26.8, 25.7, 26.3, 27.3, 27.2, 27, 27.3

            elif (valasz2==2):
                max_ertek=0
                
                for i in range(len(adatok)):
                    if (adatok[i]>adatok[max_ertek]):
                        max_ertek=i
                        
                min_ertek=0
                
                for i in range(len(adatok)):
                    if (adatok[i]<adatok[min_ertek]):
                        min_ertek=i
                    
                adathalmaz=adatok[max_ertek]-adatok[min_ertek]

                if (adathalmaz%1==0):
                    print(f"\nAz adathalmaz terjedelme:{int(adathalmaz)}")
                else:
                    print(f"\nAz adathalmaz terjededlme: {round(adathalmaz, 2)}")

                kilepes=float(input("\nAhhoz, hogy vissza lépj, írj be bármilyen számot! = "))

            # 1c feladat 

            # 27.3, 30.2, 19.2, 26.3, 27.3, 27.2, 27, 10.2
            
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
                    print(f"\nAz átlagnál nagyobb elemekből van több.\nAz átlag: {round(atlag, 2)}")
                else:
                    print(f"\nAz átlagnál kisebb elemekből van több.\nAz átlag: {round(atlag, 2)}")

                        
                kilepes=float(input("\nAhhoz, hogy vissza lépj, írj be bármilyen számot! = "))

            # 1d feladat

            elif (valasz2==4):
                negatív_ertek=0
                for i in range(len(adatok)):
                    if (adatok[i]<0):
                        negatív_ertek+=1
                    
                if (negatív_ertek>0):
                    print("\nTéli hónap.")
                else:
                    print("\nNem téli hónap")
                    
                kilepes=float(input("\nAhhoz, hogy vissza lépj, írj be bármilyen számot! = "))
                
            # Helytelen válasz esetén
    
            elif (valasz2!=0):
                print("Helytelen válasz. Probáld meg újra!")
                
                kilepes=float(input("\nAhhoz, hogy vissza lépj, írj be bármilyen számot! = "))   

    # kilépés

    elif (valasz==0):
        vege-=1
        
        
    # Helytelen válasz esetén
    
    else:
        print("Helytelen válasz. Probáld meg újra!")
        
        kilepes=float(input("\nAhhoz, hogy vissza lépj, írj be bármilyen számot! = "))