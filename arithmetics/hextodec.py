#print("print(HexToInt())")

def HexToInt():
    hex_str = str(input("valeur en hexadécimal: "))
    result=0
    i = 0
    
    if "," in hex_str:
        hex_str = hex_str.split(",") #sépare la partie avant et apres la virgule
        result+=int(hex_str[0],16)
        coma = hex_str[1] #partie apres la virgule
        while i<len(coma): #s'il reste des chiffres à convertir apr virgule
            result+=int(coma[i],16) * 16**-(i+1) 
            i+=1
        return(result)


    if "." in hex_str:
        hex_str = hex_str.split(".") #pareil mais avec un point
        result+=int(hex_str[0],16) #convertit base 16 en dec
        coma = hex_str[1] #partie apres la virgule
        while i<len(coma): #s'il reste des chiffres à convertir apr virgule
            result+=int(coma[i],16) * 16**-(i+1) 
            i+=1
        return result

    else:
        result = int(hex_str,16)
        return result



print(HexToInt())