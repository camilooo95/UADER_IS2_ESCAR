#imports
import numpy as np
from collections import deque
import matplotlib.pyplot as plt



#La clase define in objeto del tipo par ordenado, que se inicializa
#con sus componentes a y b, de la forma binómica de un número complejo:
#(a+ib)
class ParOrdenado:
    def __init__(self,a,b):
        self.real = int(a)
        self.imaginario = int(b)

num = int(input('Escribe un numero: '))

while num!= 1:
    if num % 2 == 0:
        num = int (num/2)
    else:
        num = 3*num+1
    
    print(num)

#La funcion graficar se supone debe tomar esos valores y usarlos para 
#crear un vector que vaya de 0 a el componente respectivo de X y Y
def graficarComp(num):
    limx = int(num.real)
    limy = int(num.imaginario)
    x = int(np.arange(0,limx,0.1))
    y = int(np.arange(0,limy,0.1))

    #Una vez hecho eso debe realizar el gráfico del vector
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("(",num.real,",",num.imaginario,")")
    plt.show()

#Estoy trabajando con una cola para ingresar los elementos,
#en este caso es solo uno, para realizar la prueba
# cola = deque([])
# x = ParOrdenado(1,2)
# print(x.real,",",x.imaginario)
# cola.append(x)
# for i in range(len(cola)):
#     f = cola[i]
#     graficarComp(f)

# print("Fin del programa...")
# input()