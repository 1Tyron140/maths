
print("pre_bintodec()")

def bintodec(s,nombre): #s pour separateur soit la virgule ou le point
    #nombre est la saisie en binaire
    result, result2 = 0, ""
    p, i = 0, 0 #pivot pour les calculs et i pour la boucle


    #separer partie entiere de la partie fractionnaire avec divmod()
    #faire la conversion et retirer le "1" a chaque foisqu'on multiplie par 2 et qu'il survient
    #demander le nombre de chiffre apres la virgule pour pas callculer a l'infini

    av, ap = nombre.split(s)[0], nombre.split(s)[1] #av avant la virgu et ap: apres
    result = int(av,2) #conversion av en dec
    k= int(input("limite nombres? "))

    while i < len(ap):#boucle tant que ap > 0 ou que la limite de nb est pas atteinte
        
        result += int(ap[i]) * 2**-(i+1)

        if i >=k:
            return result

        i+=1

    return result




def pre_bintodec(): #cette fonction sert a tester si le nb a conv est int ou pas et le traiter
    
    nombre = str(input("nombre a convertir ? "))    
    try:
        int(nombre,2)
        result = int(nombre,2) #convertit le nombre de base "2" en decimal
        print(result) 
        return result
    except:
        try: #sinon extraire la partie av et ap le point 
            nombre.split(".")[1] #et convertir
            print(bintodec('.',nombre))
        except:
            try:
                #pareil mais avec une virgule
                nombre.split(",")[1]
                print(bintodec(',',nombre))
            except:
                print("Saisir un binaire, peut etre fractionnaire")

    return None

pre_bintodec()