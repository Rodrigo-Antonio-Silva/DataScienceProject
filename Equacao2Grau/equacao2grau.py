#utf-8

from math import sqrt


def equacao(a, b, c):
    x = b ** 2 - (4 * a * c)
    z = x ** 0.5
    if x > 0:
        z1 = (-b + z) / (2 * a)
        z2 = (-b - z) / (2 * a)
        print(f'Como o delta é positivo temos duas raízes reais: {z1:.2f} e {z2:.2f}')
    elif x == 0:
        z3 = -b / (2 * a)
        print(f'Como o delta é igual a zero temos apenas a raiz {z3:.2f}')
    else:
        z1 = complex(-b / (2 * a), + sqrt(abs(x)) / (2 * a))
        z2 = complex(-b / (2 * a), - sqrt(abs(x)) / (2 * a))
        print(f'Como o delta é negativo temos duas raízes complexas: {z1} e {z2}')


while True:
    equacao(a = float(input('Informe o parametro a: ')),
            b = float(input('Informe o parametro b: ')),
            c = float(input('Informe o parametro c: '))
             )
    resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    while resp not in 'SN':
        print('Valor inválido!')
        resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    if resp == 'N':
        print()
        print('\033[1;31mExecução interrompida. Obrigado!')
        break