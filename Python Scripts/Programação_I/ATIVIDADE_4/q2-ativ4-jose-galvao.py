q = int(input('Total de doces comprados: '))
c=0
for c in range (1,q+1):
    print('')
    print('Doce:%.d'%(c))
    p = int(input('peso (g):'))
    preco = float(input('Valor (R$): '))

    preço_u = 1000*preco / p
    print('Preço unitário = %.2f/R$'%(preço_u))
