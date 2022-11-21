def premier():
    nombre = int(input("Quel nombre à tester ?"))
    i = 2
    while i < nombre:
        print(nombre%i)
        if nombre == 1: print('evidemment que 1 est premier')
        if nombre%i == 0 : #reste de nombre/i
            print(f"{nombre} n\'est pas premier !")
            return True
        i+=1
    print(f'{nombre} est premier ! ')
    return False

premier()