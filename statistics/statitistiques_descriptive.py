from math import sqrt

value = [float(x) for x in str(input("valeurs (a,b,...): ")).split(",")] #peuple la liste des valeurs en extrayant les valeurs separees par une virgule et convertit les strings en nombre
effectif = [float(x) for x in str(input("effectifs(a,b,...): ")).split(",")] #convertit la liste en int 
list = [1, 2, 3]
n = sum(effectif) #effectif total
etendue = max(value) - min(value) #difference des valeurs extremes
mode = value[effectif.index(max(effectif))] # recupere l'index de l'effectif max et retourne la valeur avecc le meme index


def esperance(): #le numerateur dans le calcul pour la moyenne
    i,esperance = 0, 0
    while i < len(value) and len(effectif):
        esperance += (value[i]*effectif[i]) #on additionne le produit des valeurs avec leurs effectifs 
        i+=1   
    return esperance

def moyenne():

    moyenne = e/n #esperance divise par effectif total
    return moyenne


def variance():#plus la variance est elevee plus les effectifs sont disperses (exemple l'eleve n'a jamais la meme note), moins c'est eleve plus les resultats sont reguliers 
    #(par exemple l'eleve a souvent 10 sur 20)
    #produit de l'effectif par le carre de l'ecart de la valeur à la moyenne 
    v,i = 0, 0
    while i < len(value) and len(effectif):
        v+= effectif[i] * ((value[i] - m )**2)
        i+=1
    v2 = v
    v = v/n
    return v, v2

def ecart_type(): #ecart type grand = valeurs autour de la moyenne et ecart-type faible = valeur eloignee de la moyenne
    
    ecart = sqrt(v[0])
    return ecart

def mediane(): 
    # classer les valeurs dans l'ordre croissant asc=ascendant=croissant
    asc_value, i, j = [], 0, 0

    for val in value: #cette boucle clsse les valeurs das l'ordre croissant
        i = 0
        while i < effectif[j]:
            asc_value.append(val)
            i+=1
        j+=1

    if n%2 != 0: # si l'effectif total est impair...
        med = asc_value[int(n/2)] #on retourne la au milieu des valeurs classees 
        return med, asc_value
    else: # si l'eff total est pair
        med = (asc_value[int(n/2)] + asc_value[int(n/2)-1])/2 #on retourne la moyenne des deux valeurs du milieu
        return med, asc_value
    

e = esperance()
m = moyenne()
v = variance()
ec = ecart_type()
med = mediane()
asc = med[1] #valeurs dans l'ordre croissant

#print(f"valeurs: {value}\neffectifs: {effectif}\neffectif total: {n}\netendue: {etendue}\nvaleur modale: {mode}\nesperance: {e}\nmoyenne: {m} ou {e}/{n}\nvariance: {v[0]} ou {v[1]}/{n}\necart-type: {ec}")

print("valeurs: {}\neffectifs: {}\neffectif total: {}\netendue: {}\nvaleur modale: {}\nmediane: {}\nvaleurs classees: {}".format(value, effectif, n, etendue, mode, med[0], asc))
print("esperance: {}\nmoyenne: {} ou {}/{}\nvariance: {} ou {}/{}\necart-type: {}".format(e, m, e, n, v[0], v[1], n, ec))
