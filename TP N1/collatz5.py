#collatz
# Importar el módulo pyplot con el alias plt
import matplotlib.pyplot as plt
import numpy as np


num = int(input('Escribe un numero: '))

while num!= 1:
    if num % 2 == 0:
        num = int (num/2)
    else:
        num = 3*num+1
    
    print(num)

# # Crear la figura y los ejes
# fig, ax = plt.subplots()
# # Dibujar puntos
# ax.scatter(x = [num], y = [num])
# # Guardar el gráfico en formato png
# plt.savefig('diagrama-dispersion.png')
# # Mostrar el gráfico
# plt.show()

x = np.arange(0,10,0.1)
y = x*np.cos(x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lab DLS')
plt.show()