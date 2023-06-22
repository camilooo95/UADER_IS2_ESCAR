# Implemente una clase bajo el patrón iterator que almacene una cadena de
# caracteres y permita recorrerla en sentido directo y reverso.

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class Iterator_reversa:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

class Iterator_Texto:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        self.index += 1
        return self.data[self.index - 1]

class Iterator_Combinado:
    def __init__(self, data, collection: List[Any] = []) -> None:
        self.data = data
        self._collection = collection

    def __iter__(self):
        return iter(self.data)
    
    def add_item(self, item: Any):
        self._collection.append(item)

# Ejemplo de uso
cadena = "Ingenieria en Software "

# Recorriendo en sentido directo
iterator = Iterator_Texto(cadena)
for char in iterator:
    print(char)

print("---")

# Recorriendo en sentido inverso
reverse_iterator = Iterator_reversa(cadena)
for char in reverse_iterator:
    print(char)

print("---")

# Recorriendo en sentido directo y reverso combinados
combined_iterator = Iterator_Combinado([Iterator_Texto(cadena), Iterator_reversa(cadena)])
for char in combined_iterator:
    print(char)

collection = Iterator_Combinado()
collection.add_item("Primero")
collection.add_item("Segundo")
collection.add_item("Tercero")
