numero_cargos, quantas_vagas = input().split()
numero_cargos = int(numero_cargos)
quantas_vagas = int(quantas_vagas)
dicionario_cargos = {}
soma = []
lista_temp = None
lista_palavras = []
for i in range(numero_cargos):
  nome, valor = input().split()
  nome = nome.lower()
  valor = int(valor)
  dicionario_cargos[nome] = valor

for i in range(quantas_vagas):

  descr_cargo = input()
  while descr_cargo != ".":
    lista_temp = descr_cargo.lower().split()
    descr_cargo = input()
    
    for palavra in lista_temp:
      lista_palavras.append(palavra)
    for string in lista_palavras:
      if string in dicionario_cargos.keys():
        soma.append(dicionario_cargos[string])
    lista_palavras.clear()
  
  print(sum(soma))
  soma.clear()
