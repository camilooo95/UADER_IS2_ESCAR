lass Numero():
#     def __init__(self, valor) -> str:
#         self.valor = valor

#     def imprimir(self)-> str:
#         print(f"Valor actual: {self.valor}")


# class OperacionDecorator:
#     def __init__(self, numero):
#         self.numero = numero

#     def imprimir(self)-> str:
#         self.numero.imprimir()


# class SumaDecorator(OperacionDecorator):
#     def imprimir(self)-> str:
#         self.numero.imprimir()
#         print(f"Después de sumar 2: {self.numero.valor + 2}")


# class MultiplicacionDecorator(OperacionDecorator):
#     def imprimir(self)-> str:
#         self.numero.imprimir()
#         print(f"Después de multiplicar por 2: {self.numero.valor * 2}")


# class DivisionDecorator(OperacionDecorator):
#     def imprimir(self)-> str:
#         self.numero.imprimir()
#         print(f"Después de dividir por 3: {self.numero.valor / 3}")


# if __name__ == "__main__":

#     #Uso del patrón Decorator
#     numero = Numero(5)
#     numero.imprimir()  # Imprime el valor inicial

#     print("\nDecorators aplicados:")

#     numero_suma = SumaDecorator(numero)
#     numero_suma.imprimir()  # Imprime el valor sumado por 2

#     numero_multiplicacion = MultiplicacionDecorator(numero_suma)
#     numero_multiplicacion.imprimir()  # Imprime el valor multiplicado por 2

#     numero_division = DivisionDecorator(numero_multiplicacion)
#     numero_division.imprimir()  # Imprime el valor dividido por 3

# # En esta implementación, la clase Numero representa un número y tiene un método imprimir que simplemente muestra su valor actual. 
# # La clase OperacionDecorator es la clase base abstracta que actúa como el Decorator. 

# # Toma una instancia de Numero en su constructor y redefine el método imprimir, llamando al método imprimir de la instancia interna.
# # Las clases SumaDecorator, MultiplicacionDecorator y DivisionDecorator son subclases concretas de OperacionDecorator que añaden comportamiento 
# # adicional al método imprimir al mostrar el valor del número después de realizar una operación específica.

# # En el ejemplo proporcionado, se crea una instancia de Numero con el valor inicial de 5. 
# # Luego se crean instancias sucesivas de los decoradores, pasándose mutuamente la instancia previa en sus constructores.

# # Al invocar el método imprimir de la última instancia de decorador, se mostrará el valor inicial del número y, a continuación, 
# # se mostrarán los resultados de las operaciones aplicadas en orden: suma, multiplicación y división.

# # La implementación del patrón Decorator permite añadir comportamiento adicional de forma dinámica y flexible a la clase base Numero 
# # sin modificar su código original.