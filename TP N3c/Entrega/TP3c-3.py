# Implemente una clase bajo el patrón observer donde una serie de clases están
# subscriptas, cada clase espera que su propio ID (una secuencia arbitraria de 4
# caracteres) sea expuesta y emitirá un mensaje cuando el ID emitido y el propio
# coinciden. Implemente 4 clases de tal manera que cada una tenga un ID
# especifico. Emita 8 ID asegurándose que al menos cuatro de ellos coincidan con
# ID para el que tenga una clase implementada.

class Observer:
    def __init__(self, id):
        self.id = id

    def update(self, emitted_id):
        if emitted_id == self.id:
            print(f"ID coincidente detectado: {emitted_id}")

class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def emit_id(self, emitted_id):
        print(f"ID emitido: {emitted_id}")
        for observer in self.observers:
            observer.update(emitted_id)

# Crear instancias de las clases observadoras
class1 = Observer("ABCD")
class2 = Observer("WXYZ")
class3 = Observer("1234")
class4 = Observer("5678")

# Crear la instancia del sujeto
subject = Subject()

# Suscribir las clases observadoras
subject.subscribe(class1)
subject.subscribe(class2)
subject.subscribe(class3)
subject.subscribe(class4)

# Emitir 8 IDs y verificar las coincidencias
emitted_ids = ["ABCD", "EFGH", "WXYZ", "IJKL", "1234", "5678", "MNOP", "QRST"]

for emitted_id in emitted_ids:
    subject.emit_id(emitted_id)
