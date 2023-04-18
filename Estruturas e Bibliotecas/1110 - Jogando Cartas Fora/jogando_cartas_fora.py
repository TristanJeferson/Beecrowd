lista = []
lista_remove = []

numero_cartas = int(input())
while numero_cartas != 0:
  for i in range(1, numero_cartas +1):
    lista.append(i)
  while len(lista) > 1:
    remove = lista.pop(0)
    lista.append(lista.pop(0))
    lista_remove.append(remove)

  print('Discarded cards:', str(lista_remove)[1:-1])
  print('Remaining card:', str(lista)[1:-1])
  lista.clear()
  lista_remove.clear()
  numero_cartas = int(input())
