import re
lista = []
contador_diamantes = 0
numero_testes = int(input())
for i in range(numero_testes):
    diamantes = input()
    diamantes = diamantes.replace('.','')
    diamantes = re.split("(\S{1})", diamantes)
    diamantes = list(filter(None, diamantes))

    for diamante in diamantes:
        if len(lista) > 0:
            if lista[-1] == '<' and diamante == '>':
                contador_diamantes += 1
                lista.pop()
            else:
                lista.append(diamante)
        else:
            lista.append(diamante)
    print(contador_diamantes)
    contador_diamantes = 0
    lista.clear()
