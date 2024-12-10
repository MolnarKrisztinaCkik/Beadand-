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
    if (valasz==1):
        feltoltes_szama=int(input("Add meg hány számmal szeretnéd feltölteni: "))
        
        for i in range(feltoltes_szama):
            feltoltott_szamok=float(input())
            adatok.append(round(feltoltott_szamok, 2))
            
        kilepes=float(input("Ahhoz, hogy vissza lépj, írj be bármilyen számot! = "))
        
        

    # tömb feltöltése véletlen számokkal   
    # tömbhöz egy új elem hozzáadása
    # a tömb egy adott sorszámú elem módosítása 
    # a tömb egy adott sorszámú elem törlése
    # tömb ürítése
    # tömb kiírása 
    #Feadatok
            # 1a feladat 
            # 1b feladat 
            # 1c feladat 
            # 1d feladat
    # kilépés