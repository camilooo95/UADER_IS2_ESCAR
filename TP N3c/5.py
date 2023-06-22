# Modifique el programa IS2_taller_memory.py para que la clase tenga la capacidad 
# de almacenar hasta 4 estados en el pasado y pueda recuperar los mismos en cualquier orden de ser necesario.
 
# El método undo deberá tener un argumento adicional indicando si se desea recuperar el inmediato anterior (0) y los anteriores a el (1,2,3).

import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------
# class Memento:
# 	def __init__(self, file, content):
		
# 		self.file = file
# 		self.content = content


# class FileWriterUtility:

# 	def __init__(self, file):

# 		self.file = file
# 		self.content = ""

# 	def write(self, string):
# 		self.content += string


# 	def save(self):
# 		return Memento(self.file, self.content)

# 	def undo(self, memento):
# 		self.file = memento.file
# 		self.content = memento.content


# class FileWriterCaretaker:


# 	def save(self, writer):
# 		self.obj = writer.save()

# 	def undo(self, writer):
# 		writer.undo(self.obj)


# if __name__ == '__main__':

# 	os.system("clear")
# 	print("Crea un objeto que gestionará la versión anterior")
# 	caretaker = FileWriterCaretaker()

# 	print("Crea el objeto cuyo estado se quiere preservar")
# 	writer = FileWriterUtility("GFG.txt")

# 	print("Se graba algo en el objeto y se salva")
# 	writer.write("Clase de IS2 en UADER\n")
# 	print(writer.content + "\n\n")
# 	caretaker.save(writer)

# 	print("Se graba información adicional")
# 	writer.write("Material adicional de la clase de patrones\n")
# 	print(writer.content + "\n\n")

# 	print("se invoca al <undo>")
# 	caretaker.undo(writer)

# 	print("Se muestra el estado actual")
# 	print(writer.content + "\n\n")

# El método undo ahora acepta un argumento adicional para indicar si se desea recuperar el estado inmediatamente anterior (0) o los estados anteriores a él (1, 2, 3).

class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        print("Preparando el", state)
        self._state = state

    def save_state(self):
        return Memento(self._state)

    def restore_state(self, memento):
        self._state = memento.get_state()
        print("Restaurando el", self._state)


class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self):
        self._states = []

    def add_memento(self, memento):
        if len(self._states) < 4:
            self._states.append(memento)
        else:
            self._states.pop(0)
            self._states.append(memento)

    def get_memento(self, index):
        return self._states[index]


# Ejemplo de uso
originator = Originator()
caretaker = Caretaker()

originator.set_state("Estado 1")
caretaker.add_memento(originator.save_state())

originator.set_state("Estado 2")
caretaker.add_memento(originator.save_state())

originator.set_state("Estado 3")
caretaker.add_memento(originator.save_state())

originator.set_state("Estado 4")
caretaker.add_memento(originator.save_state())

print()
# Recuperar el estado 0
print('Recuperar el estado 1')
originator.restore_state(caretaker.get_memento(0))

print()
# Deshacer acciones en orden específico
print('Recuperar primeros estados en orden especifico')
originator.restore_state(caretaker.get_memento(2))
originator.restore_state(caretaker.get_memento(1))
originator.restore_state(caretaker.get_memento(0))

print()
# Deshacer acciones en cualquier orden
print('Recuperar estados anteriores en cualquier orden')
originator.restore_state(caretaker.get_memento(2))
originator.restore_state(caretaker.get_memento(0))
originator.restore_state(caretaker.get_memento(3))

# class Memory:
#     def __init__(self):
#         self.states = []

#     def add_state(self, state):
#         if len(self.states) == 4:
#             self.states.pop(0)
#         self.states.append(state)

#     def undo(self, num_states):
#         if num_states < 0 or num_states > 3:
#             print("Número de estados inválido. Debe estar entre 0 y 3.")
#             return None

#         if num_states > len(self.states):
#             print("No hay suficientes estados en el pasado.")
#             return None

#         if num_states == 0:
#             return self.states[-1]

#         return self.states[-num_states:]

# # Ejemplo de uso
# memory = Memory()

# memory.add_state("Estado 1")
# memory.add_state("Estado 2")
# memory.add_state("Estado 3")
# memory.add_state("Estado 4")

# print(memory.undo(0))  # Recuperar el estado inmediatamente anterior
# print(memory.undo(2))  # Recuperar los dos estados anteriores
# print(memory.undo(4))  # Intentar recuperar cuatro estados (no hay suficientes)
# print(memory.undo(3))  # Recuperar los tres estados anteriores

# En este ejemplo, se crea un objeto Memory y se agregan 4 estados a través del método add_state. 
# Luego, se utilizan llamadas al método undo para recuperar los estados anteriores según se desee. 
# El argumento num_states indica cuántos estados se deben recuperar. Puedes ajustar los estados y los argumentos del método undo según tus necesidades.