
print("pre_dectobin()")




def dectobin(s,nombre): #s pour separateur soit la virgule ou le point

    result, result2 = 0, ""
    p, i = 0, 0 #pivot pour les calculs et i pour la boucle


    #séparer partie entiere de la partie fractionnaire avec divmod()
    #faire la conversion et retirer le "1" à chaque foisqu'on multiplie par 2 et qu'il survient
    #demander le nombre de chiffre apres la virgule pour pas callculer a l'infini

    if s in nombre:
        av, ap = nombre.split(s)[0], nombre.split(s)[1] #av avant la virgu et ap: apres
        av = int(av)
        ap = float("0." + ap)
        result = bin(int(av)) #conversion av en binaire
        k= int(input("limite nombres? "))

        while ap:#boucle tant que ap > 0 ou que la limite de nb est pas atteinte
            
            
            ap = ap*2
            
            if 1 > ap > 0: #si apres le double a est inf a 0 exemple a*2 = 0.5
                result2+="0" #result2=['0']

            if ap > 1: #si ap est sup a 2 exemple ap =1.5
                ap -= 1 #retire le 1 exemple a = 0.5
                result2+="1" #ajoute 1  en fin du res binaire totale resultat2=["1"]
            
            if  i == k:
                result = result + "." + result2 
                return result

            if ap+1 >= 2:

                result = result + "." + result2 + "1"
                return result

            i+=1

        result = result + "." + result2
        return result


def pre_dectobin(): #cette fonction sert a tester si le nb a conv est int ou pas et le traiter
    
    nombre = str(input("nombre a convertir ? "))    
    try:
        int(nombre) #s'il est int, le conv en binaire
        print(bin(int(nombre)))
        return bin(int(nombre))
    except:
        try: #sinon extraire la partie av et ap le point 
            nombre.split(".")[1] #et convertir
            print(dectobin('.',nombre))
        except:
            try:
                print(nombre) #pareil mais avec une virgule
                nombre.split(",")[1]
                print(dectobin(',',nombre))
            except:
                pass
        
  
pre_dectobin()