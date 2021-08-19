#utf-8
#Exercício 2 do curso de Data science com Python do prof. Walisson Silva

'''''('1)Crie arrays 1D, 2D e 3D tendo como base as dimensões dos arrays apresentados na figura abaixo. Em seguida, analise cada um dos atributos mencionados na aula.

**OBS.: Note que, nos arrays 1D e 2D da figura, há um pulo do elemento 3 para o 5. Considere que o próximo elemento é o 4.**

![Figura da primeira questão](aula2-q1.png)

Observe um exemplo de resposta no que se refere aos arrays que você deve construir. Lembre-se que você ainda precisa analisar os atributos desses arrays.')'''

import numpy as np

print(f'\n{1}')
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

