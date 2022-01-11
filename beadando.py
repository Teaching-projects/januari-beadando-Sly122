# Szám kitaláló játék, 1 és 50 között kell tippelni egy számra. 
import random

szam = random.randint(1,50)
tipp = 0
elet = 11

print("A helyes megoldás: ",szam) # Csak az ellenőrzés végett! 
while tipp != szam:
        
        print("\n""Maradt eletek szama: ",elet)
        
        tipp = int(input("Tippelj egy szamra 1 es 50 kozott: "))
        if tipp > szam:
            print("Tul nagy szamra tippeltel, tippelj kisebbre.")
            elet-=1
        elif tipp < szam: 
            print ("Tul kicsi szamra tippeltel, tippelj nagyobbra.")
            elet-=1
        if elet == 0:
            print("Elfogyott az eleted,vege a jateknak!") 
            break
else:
        print("Gratulalok,eltalaltad a szamot!")


        
