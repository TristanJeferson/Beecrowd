traducao = {}
quantidade_idiomas = int(input())
for i in range(quantidade_idiomas):
  nome_idioma = input()
  traducao_idioma = input()
  traducao[nome_idioma] = traducao_idioma
    
quantidade = int(input())
for j in range(quantidade):
  nome_crianca = input()
  idioma_falado = input()
  print(nome_crianca)
  print(traducao.get(idioma_falado))
  print()
