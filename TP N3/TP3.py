# 1. Provea una clase que dado un número entero cualquiera retorne el factorial del mismo, 
# debe asegurarse que todas las clases que lo invoquen utilicen la misma instancia de clase

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonFact(metaclass = SingletonMeta):
    def getfact(self,n):
        if n == 0:
            return 1
        else:
            return n * self.getfact(n-1)

class Factorial:
    __instance = None
    
    def __init__(self):
        if Factorial.__instance is not None:
            raise Exception("Esta clase es un Singleton. ¡Utilice Factorial.get_instance() para obtener la instancia!")
        Factorial.__instance = self
    
    @staticmethod
    def get_instance():
        if Factorial.__instance is None:
            Factorial()
        return Factorial.__instance
    
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)
#Esta función toma un número entero n y devuelve el factorial de n. Si n es igual a 0, la función devuelve 1. 
# De lo contrario, la función utiliza la fórmula n! = n * (n-1) * (n-2) * ... * 1 para calcular el factorial de n utilizando la recursión.        


"Esta clase Factorial tiene un método factorial que toma un número entero n y devuelve el factorial de n."
"La clase utiliza un enfoque basado en Singleton, que asegura que todas las instancias de Factorial que se crean son la misma instancia."
"Esto se logra mediante la definición de una variable de clase privada __instance que mantiene una referencia a la única instancia de la clase."

"El constructor de la clase Factorial es privado y solo se llama una vez para crear la única instancia de la clase."
"Si alguien intenta crear una instancia adicional,"
"se lanzará una excepción. En su lugar, las clases deben llamar al método estático get_instance() para obtener la instancia existente."


"Aquí hay un ejemplo de cómo se puede utilizar la clase Factorial:"
f = Factorial.get_instance()
print(f.factorial(0)) # Output: 1
print(f.factorial(1)) # Output: 1
print(f.factorial(5)) # Output: 120
print(f.factorial(10)) # Output: 3628800

# En otra parte del código, se obtiene la misma instancia de la clase
g = Factorial.get_instance()
print(g.factorial(3)) # Output: 6

"En este ejemplo, se crea una instancia única de la clase Factorial llamando al método estático get_instance(). "
"Luego se llama al método factorial en la misma instancia de la clase para calcular el factorial de varios números enteros. "
"Finalmente, se muestra que las distintas variables que guardan la instancia de la clase devuelven la misma instancia."


# 2. Elabore una clase para el cálculo del valor de impuestos a ser utilizado por todas las clases que necesiten realizarlo. 
# El cálculo de impuestos simplificado deberá recibir un valor de importe base imponible y deberá retornar la suma
# del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre esa base imponible.

class CalculadoraImpuestos:
    def calcular_impuestos(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones = base_imponible * 0.012
        return iva + iibb + contribuciones

'Esta clase CalculadoraImpuestos tiene un método calcular_impuestos que toma un valor de base imponible' 
'y devuelve la suma de los impuestos calculados sobre esa base imponible. El método calcula el IVA (21%),' 
'el Impuesto sobre los Ingresos Brutos (5%) y las Contribuciones Municipales (1,2%) sobre la base imponible '
'y los suma para obtener el total de impuestos.'

ci = CalculadoraImpuestos()
impuestos = ci.calcular_impuestos(1000)
print(impuestos)

'En este ejemplo, se crea una instancia de la clase CalculadoraImpuestos y '
'se llama al método calcular_impuestos con un valor de base imponible de 1000. '
'El método devuelve el total de impuestos sobre la base imponible, que en este caso es 238.2.'

#3. Genere una clase donde se instancie una comida rápida “hamburguesa” que pueda ser entregada en mostrador, 
# retirada por el cliente o enviada por delivery. A los efectos prácticos bastará que la clase imprima el método de entrega.

class Hamburguesa:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def entrega_en_mostrador(self):
        print("La hamburguesa {} está lista para ser retirada en mostrador.".format(self.tipo))
    
    def entrega_al_cliente(self):
        print("La hamburguesa {} está lista para ser retirada por el cliente.".format(self.tipo))
    
    def entrega_a_domicilio(self):
        print("La hamburguesa {} será entregada por delivery en breve.".format(self.tipo))

'En este ejemplo, la clase Hamburguesa tiene un método constructor que toma un parámetro tipo, '
'que puede ser utilizado para identificar el tipo de hamburguesa (por ejemplo, "con queso" o "doble carne").'
'Luego, se definen tres métodos diferentes para las opciones de entrega: entrega_en_mostrador(), entrega_al_cliente() y entrega_a_domicilio().'
'Cada método imprime un mensaje indicando la opción de entrega elegida y el tipo de hamburguesa que se está entregando.'
'Para utilizar esta clase, puedes instanciar un objeto de la siguiente manera:'

mi_hamburguesa = Hamburguesa("doble carne")

'Y luego llamar a los métodos de entrega según sea necesario:'

mi_hamburguesa.entrega_en_mostrador() # Imprime "La hamburguesa doble carne está lista para ser retirada en mostrador."
mi_hamburguesa.entrega_al_cliente() # Imprime "La hamburguesa doble carne está lista para ser retirada por el cliente."
mi_hamburguesa.entrega_a_domicilio() # Imprime "La hamburguesa doble carne será entregada por delivery en breve."


# 4. Implemente una clase “factura” que tenga un importe correspondiente al total de la factura pero de acuerdo 
# a la condición impositiva del cliente (IVA Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal condición. 

class Factura:
    def __init__(self, importe, condicion_impositiva):
        self.importe = importe
        self.condicion_impositiva = condicion_impositiva
    
    def calcular_iva(self):
        if self.condicion_impositiva == "Responsable Inscripto":
            return self.importe * 0.21
        elif self.condicion_impositiva == "No Inscripto":
            return 0
        elif self.condicion_impositiva == "Exento":
            return 0
        else:
            raise ValueError("La condición impositiva ingresada no es válida.")
    
    def imprimir_factura(self):
        iva = self.calcular_iva()
        total = self.importe + iva
        print("Factura")
        print("Importe: ${:.2f}".format(self.importe))
        print("Condición impositiva: {}".format(self.condicion_impositiva))
        print("IVA: ${:.2f}".format(iva))
        print("Total: ${:.2f}".format(total))

'En este ejemplo, la clase Factura tiene un método constructor que toma dos parámetros: importe, que representa el monto total de la factura, '
'y condicion_impositiva, que indica la condición impositiva del cliente.'
'Luego, se define un método calcular_iva() que utiliza la condición impositiva para determinar el monto del IVA correspondiente.' 
'En este caso, se asume una tasa de IVA del 21% para los clientes Responsables Inscriptos, '
'mientras que los clientes No Inscriptos y Exentos no pagan IVA.'
'Finalmente, se define un método imprimir_factura() que utiliza el monto del IVA calculado para imprimir la factura con el detalle correspondiente.'

mi_factura = Factura(1000, "Responsable Inscripto")
mi_factura.imprimir_factura()

# 5. Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar para construir aviones en lugar de vehículos. 
# Para simplificar suponga que un avión tiene un “body”, 2 turbinas, 2 alas y un tren de aterrizaje.


class Body:
    def __init__(self):
        print("Se construyó el body del avión.")


class Turbina:
    def __init__(self):
        print("Se construyó una turbina del avión.")


class Alas:
    def __init__(self):
        print("Se construyó un ala del avión.")


class TrenAterrizaje:
    def __init__(self):
        print("Se construyó el tren de aterrizaje del avión.")


class Airplane:
    def __init__(self):
        self.body = Body()
        self.Turbina_1 = Turbina()
        self.Turbina_2 = Turbina()
        self.Alas_1 = Alas()
        self.Alas_2 = Alas()
        self.landing_gear = TrenAterrizaje()
        print("Se construyó un avión completo.")

'En este ejemplo, se definen las mismas clases utilizadas para construir vehículos en el taller de clase,'
'pero se agregan dos clases adicionales para representar las turbinas y las alas de un avión.'
'Luego, se define una clase Airplane que utiliza estas clases para construir un avión completo.'
'En este caso, se asume que un avión tiene un body, dos turbinas, dos alas y un tren de aterrizaje.'
'Para utilizar esta clase, puedes instanciar un objeto de la siguiente manera:'

mi_avion = Airplane()

# 6. Extienda el ejemplo del taller para prototipos de forma que genere 20
# anidamientos y que la carga simulada de procesamiento dure 2 segundos.

import time

class Prototipo:
    def __init__(self, id):
        self.id = id
        print(f"Se creó el prototipo {self.id}.")
    
    def process(self):
        print(f"El prototipo {self.id} está procesando...")
        time.sleep(2)
        print(f"El prototipo {self.id} ha terminado de procesar.")

def crear_Prototipo(num_Prototipo):
    for i in range(num_Prototipo):
        p = Prototipo(i)
        p.process()
        print()

if __name__ == "__main__":
    crear_Prototipo(20)

'En este ejemplo, se agregó un bucle for para crear 20 prototipos anidados. '
'Cada vez que se crea un prototipo, se llama al método process para cargarlo durante 2 segundos.'
'Luego, se llama a la función crear_Prototipo para crear los 20 prototipos anidados.'

