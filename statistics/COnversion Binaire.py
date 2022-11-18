i=0
resultat=[]
reste=0

def convertir():
    nombre = int(input("entrez le nombre à convertir "))
    resultat.clear()
    while nombre >= 2:
        reste = nombre % 2
        nombre = nombre / 2
        resultat.insert(0,int(reste))
    if nombre!= 0:
        resultat.insert(0, 1)
        return resultat
    else:
        print("alors comme ca on ne sait pas convertir 0 en binaire ?")
        



print(convertir())
print(convertir())