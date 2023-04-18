num_casos = int(input())
lista_vivos = []

for i in range(num_casos):
    quant_pessoas, numero_saltos = input().split()
    quant_pessoas = int(quant_pessoas)
    numero_saltos = int(numero_saltos)
    for j in range(1, quant_pessoas+1):
        lista_vivos.append(j)
    cont = len(lista_vivos)
    numero_saltos -= 1
    a = numero_saltos % cont
    while cont != 1:
        if len(lista_vivos) > 1:
            cont-=1
            lista_vivos.pop(a)
            a = (a + numero_saltos) % cont

    
    print('Case {}: {}'.format(i+1, *lista_vivos, sep=''))
    lista_vivos.clear()
