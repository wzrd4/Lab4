class Stationery:
    def __init__(self, title="NT"):
        self.title = title

    def draw(self):
        print("Запуск отрисовки:")


class Pen(Stationery):
    def __init__(self, title="NT"):
        super().__init__(title)

    def draw(self):
        super().draw()
        print("Ручка рисует")


class Pencil(Stationery):
    def __init__(self, title="NT"):
        super().__init__(title)

    def draw(self):
        super().draw()
        print("Карандаш рисует")


class Handle(Stationery):
    def __init__(self, title="NT"):
        super().__init__(title)

    def draw(self):
        super().draw()
        print("Маркер рисует")


a = Pen()
b = Pencil()
c = Handle()
a.draw()
b.draw()
c.draw()
