clientesCadastrados = 0
clientes = []
while True:
    nome = input('Nome: ').title()
    if nome.upper() == 'SAIR' or clientesCadastrados == 100:
        break
    else:
        senha = int(input('Senha: '))
        mensalidade = input('situacao: ').upper()
        clientes.append([nome, senha, mensalidade])
        clientesCadastrados += 1
while True:
    recebeSenha = int(input(''))
    if recebeSenha == -1:
        break
    encontrei = False
    nome = ''
    situacao = ''
    for usuario in clientes:
        if usuario[1] == recebeSenha:
            encontrei = True
            nome = ''.join(usuario[0])
            situacao = ''.join(usuario[2])
            continue
    if encontrei:
        if situacao == 'P':
            print(f'{nome}, seja bem-vindo(a)!')
        else:
            print(f'Não está esquecendo de algo, {nome}? Procure a recepção')
    else:
        print('Seja bem-vindo(a)! Procure a recepção!')