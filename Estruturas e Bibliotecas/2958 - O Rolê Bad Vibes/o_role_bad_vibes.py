while True:
	try:
		linha, coluna = input().split()
		linha = int(linha)
		coluna = int(coluna)
		
		lista_vida = []
		lista_disciplina = []
		
		for i in range(linha):
			num_letra = input().split()
			for item in num_letra:
				if item[1] == 'V':
					lista_vida.append(item)
				else:
					lista_disciplina.append(item)
		
		lista_vida.sort(reverse=True)
		lista_disciplina.sort(reverse=True)
		
		for item in lista_vida:
			print(item)
		for item in lista_disciplina:
			print(item)
	
	except EOFError:
		break
