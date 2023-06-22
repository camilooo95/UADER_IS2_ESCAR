class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        print("Setting state to:", state)
        self._state = state

    def save_state(self):
        return Memento(self._state)

    def restore_state(self, memento):
        self._state = memento.get_state()
        print("Restored state:", self._state)


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

# Deshacer acciones en cualquier orden
originator.restore_state(caretaker.get_memento(2))
originator.restore_state(caretaker.get_memento(0))
originator.restore_state(caretaker.get_memento(3))

# Deshacer acciones en orden específico
originator.restore_state(caretaker.get_memento(1))
originator.restore_state(caretaker.get_memento(0))