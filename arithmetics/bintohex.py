print("pre_bintohex()")

#ici la strat c'est de conv la partie ap la virg en dec puis en hexa
table = { #deprecated table

    '0':'0', '0000':'0', '1':'1', '0001':'1', '10':'2', '0010':'2', '11':'3',
    '0011':'3','100':'4', '0100':'4', '101':'5', '0101':'5','110':'6', 
    '0110':'6', '111':'7', '0111':'7', '1000':'8', '1001':'9', '1010':'A',
    '1011':'B', '1100':'C', '1101':'D', '1110':'E' ,'1111':'F'
}

table_2 = {

    '10':'a', '11':'b', '12':'c', '13':'d', '14':'e', '15':'f'
}

def bintohex(s,nombre): #s pour separateur soit la virgule ou le point
    #nombre est la saisie en binaire
    result = 0
    i = 0# index i pour a boucle


    #faire la conversion et retirer le "16" a chaque foisqu'on multiplie par 16 et qu'il survient
    #demander le nombre de chiffre apres la virgule pour pas calculer a l'infini

    av, ap = nombre.split(s)[0], nombre.split(s)[1] #av avant la virgu et ap: apres
    result = hex(int(av,2))[2:] #conversion av en hex
    k= int(input("limite nombres? "))
    result_2 = 0 #partie apres la virgule qu'on convertit en hexa

    while i < len(ap):#boucle tant que ap > 0 ou que la limite de nb est pas atteinte
        result_2 += int(ap[i]) * 2**-(i+1)

        if i >= k:
            return result_2
        i+=1
    ap = result_2 #ap = partie apres la virgule en dec
    result_2 = ""

    while ap:#boucle tant que ap > 0 ou que la limite de nb est pas atteinte
            
            
            ap = ap*16
            j = int(divmod(ap,1)[0])
            if 1 > ap > 0: #si apres le double a est inf a 1 exemple a*2 = 0.5
                result_2+="0" #result2=['0']

            if ap >= 1: #si ap est sup a 2 exemple ap =1.5
                ap -= j #retire le 1 exemple a = 0.5
                try:
                    result_2+=table_2[str(j)] #ajoute la val >0 en fin du res hex tot resultat2=["e"]
                except:
                    result_2+=str(j)
                    
            if  i == k:
                result = result + "." + result_2 
                return result

            if ap+1 >= 16:

                result = result + "." + result_2 + "F"
                return result
            print(result)
            i+=1

    result = result + "." + result_2
    return result




def pre_bintohex(): #test si le nb est int ou pas
    
    nombre = str(input("bin a convertir ? "))    
    try:
        result = hex(int(nombre, 2)) #teste si le nb est bin et le conv en hex
        print(result[2:])
        return result
    except:
        try: #sinon extraire la partie av et ap le point 
            nombre.split(".")[1] #et convertir
            print(bintohex('.',nombre))
        except:
            try: #sinon extraire la partie av et ap le point 
                nombre.split(",")[1] #et convertir
                print(bintohex(',',nombre))
            except:
                print('entree incorrecte')

    return None

pre_bintohex()
