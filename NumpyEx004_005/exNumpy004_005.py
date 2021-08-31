# utf-8
'''**1) Crie dois arrays 1D de forma automática: o primeiro com números pares entre 0 e 8; o segundo com números ı
́mpares entre 1 e 9. Experimente realizar as operações aritméticas de soma,
subtração, multiplicação e divisão sobre eles (primeiro o array par e depois o array ímpar, nessa ordem).**'''

import numpy as np
print()
print('=' * 39)
print('Ex.1')

a = np.arange(0, 10, 2)
print(a)

b = np.arange(1, 10, 2)
print(b)

print(a + b)
print(a - b)
print(a / b)
print(a * b)

'''**2) Construa a matriz ilustrada pela figura abaixo (Dica: pesquise sobre o método `reshape`). 
Em seguida, obtenha cada um dos "pedaços" (ou cortes) do array 2D destacados na figura (em cores) e, 
para cada um deles, calcule a soma, a média, a variância e o desvio padrão dos valores.**

![Questão 2](aula3-q2.png)'''
print()
print('=' * 39)
print('Ex.2')

p = np.arange(6)
s = np.arange(10, 16)
t = np.arange(20, 26)
qa = np.arange(30, 36)
qi = np.arange(40, 46)
se = np.arange(50, 56)
fig = np.concatenate((p, s, t, qa, qi, se))
fig = fig.reshape(6, 6)
print(fig)

r = fig[2, :]
ro = r[r % 2 == 0]
x = fig[4, :]
xo = x[x % 2 == 0]

roxo = np.concatenate((ro, xo), axis=0, out=None, dtype=int, casting='same_kind')
print(f'\nslice roxo {roxo}')
print(f'média slice roxo {roxo.mean()}')
print(f'variância slice roxo {roxo.var()}')
print(f'desvio padrão slice roxo {roxo.std()}')

azul = fig[:, 2]
print(f'\nslice azul {azul}')
print(f'média slice azul {azul.mean()}')
print(f'variância slice azul {azul.var()}')
print(f'desvio padrão slice azul {azul.std()}')

vermelho = fig[0, 3:5]
print(f'\nslice vermelho {vermelho}')
print(f'média slice vermelho {vermelho.mean()}')
print(f'variância slice vermelho {vermelho.var()}')
print(f'desvio padrão slice vermelho {vermelho.std()}')

verde = (fig[4:, 4:]).reshape(1, 4)
print(f'\nslice verde {verde}')
print(f'média slice verde {verde.mean()}')
print(f'variância slice verde {verde.var()}')
print(f'desvio padrão slice verde {verde.std()}')

'''**3) Com base na matriz abaixo, obtenha:**
  (a) Um vetor cotendo o seno dos elementos da segunda linha;  
  (b) A sua inversa, sua transposta e um vetor com os elementos da sua diagonal principal;  
  (c) A soma e a média dos seus elementos.'''
print()
print('=' * 39)
print('Ex.3')
ma = [[2, 45, 22, 12], [44, 34, 68, 3], [5, 7, 78, 2], [12, 34, 5, 9]]
ma_arr = np.array(ma)
print(f'\n{ma_arr}')

print('\n(a)')
sen_arr = np.sin(ma_arr[1, :])
print(sen_arr)

print('\n(b.1)')
print(f'{ma_arr[::-1]}')

print('\n(b.2)')
print(ma_arr.T)

print('\n(b.3)')
print(ma_arr.diagonal())

print('\n(b.3)')
print(f'A soma do array é {ma_arr.sum()} e a média {ma_arr.mean()}')
