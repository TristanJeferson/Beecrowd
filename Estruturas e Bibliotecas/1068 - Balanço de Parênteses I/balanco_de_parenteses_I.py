while True:
    try:
        lista = []
        expressao = input()
        for x in expressao:
            if x != '(' and x != ')':
                expressao = expressao.replace(x,'')
    
    
        for expressao in expressao:
            if len(lista) > 0:
                if lista[-1] == '(' and expressao == ')':
                    lista.pop()
                else:
                    lista.append(expressao)
            else:
                lista.append(expressao)
    
        if len(lista) == 0:
            print('correct')
        else:
            print('incorrect')
        lista.clear()
        
    except EOFError or 1 <= len(expressao) <= 10000:
        break
