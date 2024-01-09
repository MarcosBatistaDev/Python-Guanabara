# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

entrada = str(input('Expressão: '))
parênteses = list()

for c in entrada:
    if c == '(':
        parênteses.append(c)
    elif c == ')':
        if len(parênteses) > 0:
            parênteses.pop()
        else:
            parênteses.append(')')
            break
if len(parênteses) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')