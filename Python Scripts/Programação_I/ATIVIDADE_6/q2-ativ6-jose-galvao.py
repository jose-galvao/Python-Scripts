dados = []
continuar = "continuar"


def linha():
    print('-='* 20)


def animais(lista):
    dados.append(lista)


def peso_medio(nome):
    qtd = quantidade(nome)
    peso = 0.0
    global dados
    for i in range(len(dados)):
        if (nome == dados[i][0]):
            peso += dados[i][1]
    if (qtd == 0):
        return 0.0
    return peso / qtd


def quantidade(nome):
    global dados
    quantidade = 0
    for i in range(len(dados)):
        if (dados[i][0] == nome):
            quantidade = quantidade + 1
    return quantidade



def puan_animais(pais, animal):
    animais = []
    global dados
    for i in range(len(dados)):
        if (animal == dados[i][0]):
            animais.append(dados[i])
    return len(paises(animais, pais))


def paises(lista, pais):
    paises = []
    for i in range(len(lista)):
        if (lista[i][2] == pais):
            paises.append(lista[i])
    return paises


#programa princiapal
while (continuar == "continuar"):
    linha()
    nome = str(input('\033[1;31mNome \033[0;0mdo\033[1;34m Animal\033[0;0m:')).lower()
    peso = float(input('\033[1;36mPeso \033[0;0mdo \033[1;34mAnimal\033[0;0m:'))
    pais = str(input('\033[1;34mPais \033[0;0mdo \033[1;34mAnimal\033[0;0m:')).lower()
    animais([nome, peso, pais])
    continuar = str(input('Digite \033[;7mcontinuar\033[0;0m,para continuar... ')).lower()
    linha()

print('macacos:', quantidade("macaco"))
print("Peso médio dos tigres: %.2f" % peso_medio("tigre"))
print('Cobras da Venezuela:', puan_animais("venezuela", "cobra"))