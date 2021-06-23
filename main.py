##############################################################################
# ---------- > EXERCISE 01

A = int(input('Digite o 1º lado do triangulo:'))
B = int(input('Digite o 2º lado do triangulo:'))
C = int(input('Digite o 3º lado do triangulo:'))

if (A > 0) and (B > 0) and (C > 0):

    if(A + B > C) and (A + C > B) and (B + C > A):
        if A != B and A != C and B != C:
            print('triangulo escaleno !')
        else:
            if A == B and A == C and B == C:
                 print('Ao menos um dos valores indicados nao servem para formar um triangulo')
            else:
                print('Triangulo isosceles!')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triangulo ')

else:
    print('Ao menos um dos valores indicados não servem para formar um triangulo')

##############################################################################
# ---------- > EXERCISE 02

op = input(input('Qual operação deseja fazer: '))
if op == '+' or op == '-' or op == '*' or op == '/':
    x = input(input('Digite o primeiro valor: '))
    y = input(input('Digite o segundo valor:'))

if (op == '+'):
    res = x + y++
    print('Resultado: {} + {} = '.format(x, y, res))
elif(op == '-'):
    res = x - y
    print('Resultado: {} - {} = '.format(x, y, res))
elif (op == '*'):
    res = x * y
    print('Resultado: {} * {} = '.format(x, y, res))
elif (op == '/'):
    res = x / y
    print('Resultado: {} / {} = '.format(x, y, res))
else:
    print('Operação invalida.')

print('Encerrando o programa')

##############################################################################
# ---------- > EXERCISE 03
kwh = float(input('Quantos KWh?'))
tipo = input('Qual o tipo de instalção (R, C ou I) ?')

if(tipo == 'R'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65

elif(tipo == 'C'):
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.6

elif(tipo == 'I'):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.6
else:
    print('Instalação ivalida')

