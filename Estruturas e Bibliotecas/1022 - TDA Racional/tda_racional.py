from math import gcd

quant_testes = int(input())
for i in range(quant_testes):
    n1, b1, d1, operacao, n2, b2, d2 = input().split()
    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)

    if operacao == '+':
        soma = (n1 * d2) + (n2 * d1)
        d = d1 * d2
        mdc = gcd(soma, d)
        print(f'{soma}/{d} = {soma//mdc}/{d//mdc}')

    elif operacao == '-':
        subtracao = n1*d2 - n2*d1
        d = d1 * d2
        mdc = gcd(subtracao, d)
        print(f'{subtracao}/{d} = {subtracao//mdc}/{d//mdc}')
    
    elif operacao == '*':
        multiplicacao = n1 * n2
        d = d1 * d2
        mdc = gcd(multiplicacao, d)
        print(f'{multiplicacao}/{d} = {multiplicacao//mdc}/{d//mdc}')
    
    elif operacao == '/':
        divisao = n1 * d2
        d = n2 * d1
        mdc = gcd(divisao, d)
        print(f'{divisao}/{d} = {divisao//mdc}/{d//mdc}')
