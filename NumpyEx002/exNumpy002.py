#utf-8
#Exercício 2 do curso de Data science com Python do prof. Walisson Silva

'''''('1)Crie arrays 1D, 2D e 3D tendo como base as dimensões dos arrays apresentados na figura abaixo. Em seguida, analise cada um dos atributos mencionados na aula.

**OBS.: Note que, nos arrays 1D e 2D da figura, há um pulo do elemento 3 para o 5. Considere que o próximo elemento é o 4.**

![Figura da primeira questão](aula2-q1.png)

Observe um exemplo de resposta no que se refere aos arrays que você deve construir. Lembre-se que você ainda precisa analisar os atributos desses arrays.')'''

import numpy as np

print()
print('=' * 39)
print('Ex.1')
print(np.arange(0, 6))                  # array de 1 dimensão
print(type(np.arange(0, 6)))
print(f'Formato => {np.arange(0, 6).shape}')
print(f'Tamanho => {np.arange(0, 6).size}')
print(f'Dimensão => {np.arange(0, 6).ndim}')
print(f'\n{2}')


b = np.random.randint(3, size=(3, 4))   # array de 2 dimensões
print(b)
print(type(b))
print(f'Formato => {b.shape}')
print(f'Tamanho => {b.size}')
print(f'Dimensão => {b.ndim}')
print(f'\n{3}')

c = np.random.randint(2, size=(3, 3, 5))
print(c)
print(type(c))
print(f'Formato => {c.shape}')
print(f'Tamanho => {c.size}')
print(f'Dimensão => {c.ndim}')

'''2) Crie uma matriz identidade com dimensões 5 X 5.'''

print('=' * 39)
print('Ex.2')
print(np.identity(5, dtype=float))

'''3) Crie uma matriz 3 X 3 com todos os elementos iguais a 1.'''

print('=' * 39)
print('Ex.3')
print(np.ones((3, 3)))

'''4) Crie uma matriz $2 \times 3$ com elementos de valores aleatórios entre 0 e 20.'''

print('=' * 39)
print('Ex.4')
print(np.random.rand(2, 3))

'''5) Crie o vetor [9, 8, 7, 6, 5, 4, 3, 2, 1] utilizando as duas funções vistas na 
aula que são capazes de criar um vetor como este, de forma automática.'''

print('=' * 39)
print('Ex.5')
print(np.arange(9, 0, -1))
print(np.linspace(9, 1, 9, dtype=int))

