n =int(input('escolha um numero de 1 a 10: '))
ckyara=0
cvin=0
for i in range(n):
    kyara = str(input("Vez de Kyara: "))
    Vinicius = str(input("Vez de Vinicius: "))
    info=[]
    info.append(kyara)
    info.append(Vinicius)
    if info[0] == "pedra":
        if info[1] == "pedra":
            ckyara=ckyara+1
            cvin= cvin+1
        elif info[1] == "papel":
            cvin= cvin+1
        elif info[1] == "tesoura":
            ckyara=ckyara+1
    elif info[0] == "papel":
        if info[1] == "papel":
            ckyara=ckyara+1
            cvin= cvin+1
        elif info[1] == "tesoura":
            cvin= cvin+1
        elif info[1] == "pedra":
            ckyara=ckyara+1

    if info[0] == "tesoura":
        if info[1] == "tesoura":
            ckyara=ckyara+1
            cvin= cvin+1
        elif info[1] == "pedra":
            cavin= cvin+1
        elif info[1] == "papel":
            ckyara=ckyara+1
            
if(ckyara>cvin):
    print("Vinicius vai lavar a louça!")
elif(ckyara<cvin):
    print("Kyara vai lavar a louça!")
else:
    print("Os dois vão lavar a louça juntos!")