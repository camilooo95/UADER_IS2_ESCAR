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
