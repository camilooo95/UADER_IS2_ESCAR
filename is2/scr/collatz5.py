#collatz
# Importar el módulo pyplot con el alias plt
import matplotlib.pyplot as plt


x = int(input('Escribe un numero: '))

while x!= 1:
    if x % 2 == 0:
        x = int (x/2)
    else:
        x = 3*x+1
    
    print(x)

# Crear la figura y los ejes
fig, ax = plt.subplots()
# Dibujar puntos
ax.scatter(x = [1, 2, 3], y = [3, 2, 1])
# Guardar el gráfico en formato png
plt.savefig('diagrama-dispersion.png')
# Mostrar el gráfico
plt.show()