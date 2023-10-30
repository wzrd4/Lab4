class Worker:
    def __init__(self, name, surname, position, wage=0, bonus=0):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage=0, bonus=0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self._name + ' ' + self._surname

    def get_total_income(self):
        try:
            return self._income["wage"] + self._income["bonus"]
        except TypeError as e:
            print(e)
            print("При создании объкта были указаны неккорректные значения")


a = Position("Николай", "Апретов", "Менеджер", 120, 30)
print(a.get_full_name())
print(a.get_total_income())
