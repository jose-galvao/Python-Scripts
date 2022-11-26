import os

saldo = float(input('digite o seu salario atual e press enter para continuar... '))
os.system('clear')

while True:
    print("===BANCO P1====")
    print('1- DEPOSITAR')
    print('2- SACAR')
    print('3- TRANSFERIR')
    print('4- SALDO')
    print('5- SAIR')

    opçao = int(input('DIGITE A OPÇÃO QUE DESEJA: '))

    if opçao < 1 or opçao > 5:
        print('essa opçao nao existe...')
        pause = str(input("aperte enter para continuar..."))
    os.system('clear')
        # opçao 1
    if opçao == 1:
        os.system('clear')
        print('=====Você esta na opçao de deposito=====')
        deposito = float(input(' valor do deposito:'))
        print(f'você depositou R${deposito:.2f}')
        saldo+=deposito
        pause=input('press enter para continuar')
        os.system('clear')
    
    #opçao 2
    if opçao == 2:
        os.system('clear')
        print('===você esta na opçao de saque===')
        saque = float(input('valor do saque: '))
        if saque > saldo:
            print('você nao tem dinheiro suficiente para saque')
            pause=input('press enter para continuar')
            os.system('clear')
        if saque <= saldo:
            print(f'você sacou R${saque:.2f}')
            saldo-=saque
        pause=input('press enter para continuar')
        os.system('clear')
    #opçao 3
    if opçao == 3:
        r = 'S'
        while r == 'S':
            os.system('clear')
            print('===Você esta na opçao de transferir===')
            print(f'seu saldo atual é de R${saldo:.2f}')
            conta = int(input(' qual o numero da conta? '))
            trans = float(input('quanto deseja transferir: '))
            os.system('clear')

            if trans > saldo:
                print('você nao tem dinheiro suficiente')
                pause=input('press enter para continuar')
                os.system('clear')
                r = str(input('deseja fazer outra transferencia? [S/N]')).upper()
            if trans <= saldo:
                print('transferencia concluida...')
                r = str(input('deseja fazer outra transferencia? [S/N]')).upper()
                os.system('clear')
                saldo -= trans
            continue
    #opçao 4
    if opçao == 4:
        os.system('clear')
        print('=====Você esta na opçao de saldo=====')
        print(f'Seu saldo é de R${saldo:.2f}')
        pause = str(input("aperte enter para continuar..."))
        os.system('clear')
#opçao 5
    if opçao == 5:
        print = input('sua sessão está sendo encerrada, aperte enter para finalizar...')
        os.system('clear')
