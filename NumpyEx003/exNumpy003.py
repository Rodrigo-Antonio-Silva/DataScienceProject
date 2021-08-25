#utf-8

'''1) Obtenha as "fatias" do array que são destacadas na figura abaixo. Observe que cada corte (ou fatia) é destacado em uma cor distinta.
    Em outras palavras, você deve se perguntar como obter a região destacada na cor laranja, por exemplo;
e o mesmo para cada uma das outras cores.![Cortes em um array bidimensional](aula3-q1.png)'''

import numpy as np

print()
print('=' * 39)
print('Ex.1')
p = np.arange(6)
s = np.arange(10, 16)
t = np.arange(20, 26)
qa = np.arange(30, 36)
qi = np.arange(40, 46)
se = np.arange(50, 56)

a = np.concatenate((p, s, t, qa, qi, se))

a = a.reshape(6, 6)
print(a)

print(f'\nValores em verde: {a[2][0]}, {a[2][2]}, {a[2][4]}, {a[4][0]}, {a[4][2]}, {a[4][4]}')
print(f'\nValores em vermelho:{a[:,2]}')
print(f'\nValores em laranja: {a[0, 3:5]}')
print(f'\nValores em azul: {a[4:6, 4:6]}')

'''2) Realize o mesmo procedimento que foi solicitado na questão anterior para a figura abaixo.

![Questão 2](aula3-q2.png)'''

print()
print('=' * 39)
print('Ex.2')

print(f'\nValores em roxo {a[2][0]}, {a[2][2]}, {a[2][4]}, {a[4][0]}, {a[4][2]}, {a[4][4]}')
print(f'\nValores em azul {a[:, 2]}')
print(f'\nValores em vermelho {a[0][3:5]}')
print(f'\nValores em verde {a[4:, 4:]}')

'''3) Faça uma download de uma imagem na internet. Em seguida, pratique a técnica de cortes em arrays na sua imagem,
 de modo semelhante àquele apresentado na Aula 03'''

print()
print('=' * 39)
print('Ex.3')

from skimage import io
import matplotlib.pyplot as plt

img = io.imread('img.png')
print(img.shape)

print(plt.imshow(img))
plt.show()
