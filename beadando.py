# Szám kitaláló játék, 1 és 50 között kell tippelni egy számra. 
import random
szam = random.randint(1,50)
tipp = 0
elet_nehez = 5
nehezseg = input("K/N: ")
elet_konnyu = []


def langyos(szam,tipp,elet_konnyu,):
    if szam -tipp <=10 and szam -tipp>=5:
        print("Langyos")
        elet_konnyu.append(1)
        elet = print("Eletek szama:",10-sum(elet_konnyu))
          
def hideg(szam,tipp,elet_konnyu,):
    if szam -tipp >=10:
        print("Hideg")
        elet_konnyu.append(1)
        elet = print("Eletek szama:",10-sum(elet_konnyu))
       
def meleg(szam,tipp,elet_konnyu,):
    if szam -tipp <=4:
        print("Meleg")
        elet_konnyu.append(1)
        elet = print("Eletek szama:",10-sum(elet_konnyu))
        
def forro(szam,tipp,elet_konnyu,):
    if szam -tipp <=1:
        print("Forro")
        elet_konnyu.append(1)
        elet = print("Eletek szama:",10-sum(elet_konnyu))
        

print("A helyes megoldás: ",szam) # Csak az ellenőrzés végett! 
if nehezseg == "K":
    print("10 Eleted van!")   
    while tipp != szam:
        
            tipp = int(input("Tippelj egy szamra 1 es 50 kozott: "))
            

            if tipp != szam:
                langyos(szam,tipp,elet_konnyu,)
                

            if tipp != szam:
                hideg(szam,tipp,elet_konnyu,) 
                

            if tipp != szam: 
                meleg(szam,tipp,elet_konnyu,)
                

            if tipp !=szam: 
                forro(szam,tipp,elet_konnyu,)
                

            if sum(elet_konnyu) == 10:
                
                print("Elfogyott az eleted, vege a jateknak!") 
                break
    else:
            print("Gratulalok,eltalaltad a szamot!")
            
elif nehezseg =="N":
    while tipp != szam:
                
                print("\n""Maradt eletek szama: ",elet_nehez)
                
                tipp = int(input("Tippelj egy szamra 1 es 50 kozott: "))
                if tipp > szam:
                    print("Tul nagy szamra tippeltel, tippelj kisebbre.")
                    elet_nehez-=1
                elif tipp < szam: 
                    print ("Tul kicsi szamra tippeltel, tippelj nagyobbra.")
                    elet_nehez-=1
                if elet_nehez == 0:
                    print("Elfogyott az eleted,vege a jateknak!") 
                    break
    else:
                print("Gratulalok eltalaltad a szamot!")

