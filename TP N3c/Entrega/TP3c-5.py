# Modifique el programa IS2_taller_memory.py para que la clase tenga la capacidad 
# de almacenar hasta 4 estados en el pasado y pueda recuperar los mismos en cualquier orden de ser necesario.
 
# El método undo deberá tener un argumento adicional indicando si se desea recuperar el inmediato anterior (0) y los anteriores a el (1,2,3).

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
