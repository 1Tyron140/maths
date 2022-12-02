table = {

    '0':'0', '0000':'0', '1':'1', '0001':'1', '10':'2', '0010':'2', '11':'3',
    '0011':'3','100':'4', '0100':'4', '101':'5', '0101':'5','110':'6', 
    '0110':'6', '111':'7', '0111':'7', '1000':'8', '1001':'9', '1010':'A',
    '1011':'B', '1100':'C', '1101':'D', '1110':'E' ,'1111':'F'
}



def pre_bintohex(): #test si le nb est int ou pas
    
    nombre = str(input("bin a convertir ? "))    
    try:
        result = ""
        int(nombre,2)
        i = len(nombre)%4 #commence par la partie du nombre sur 4 bits ou moins
        if i==0:
            #result += table[nombre[0:4]]
            pass
        else:
            result += table[nombre[:i]]

        while i < len(nombre):
            result += table[nombre[i:i+4]]
            i+=4
        print(result)
        return result
    except:
        pass

    return None

pre_bintohex()