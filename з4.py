import time


class Wizard:
    amount = 0

    @classmethod
    def increaseamount(cls):
        cls.amount += 1

    @classmethod
    def decreaseamount(cls):
        cls.amount -= 1

    def __init__(self, maxmana=10, maxhp=8, mana=5, hp=4, staff_id=1):
        self.__maxm = maxmana
        self.__mana = mana
        self.__maxhp = maxhp
        self.__staff_id = staff_id
        self.__hp = hp
        Wizard.increaseamount()

    def changestaff(self, staffid):
        self.__staff_id = staffid

    def __del__(self):
        Wizard.decreaseamount()

    def showinfo(self):
        print(f"Максимальная мана = {self.__maxm}")
        print(f"Мана = {self.__mana}")
        print(f"Максимальное здоровье = {self.__maxhp}")
        print(f"Здоровье = {self.__hp}")

    @staticmethod
    def play(wiz):
        print("1 - выстрелить")
        print("2 - восстановиться")
        print("3 - посмотреть характеристики")
        print("4 - завершить игру")
        while True:
            try:
                choice = int(input())
            except ValueError as e:
                print(e)
                continue
            if choice == 1:
                wiz.shoot(2)
            elif choice == 2:
                wiz.regen()
            elif choice == 3:
                wiz.showinfo()
            if choice == 4:
                return

    def shoot(self, manacost):
        if manacost < self.__mana:
            self.__mana -= manacost
            print("Выстрел!")
        else:
            print("Недостаточно маны для выстрела")

    def regen(self):
        print("Восстановление начнется через 5 секунд")
        time.sleep(5)
        while self.__mana != self.__maxm:
            self.__mana += 1
            print("Мана +1")
            time.sleep(1)
        else:
            print("Мана заполнена")
        while self.__hp != self.__maxhp:
            self.__hp += 1
            print("HP +1")
            time.sleep(1)
        else:
            print("Здоровье восстановлено")


def menu():
    while True:
        print("Введите\n1-создать нового мага\n2-вывести всех магов\n3-выбрать мага для игры\n4-выход\nВаш выбор?")
        try:
            choice = int(input())
        except ValueError as e:
            print(e)
        else:
            return choice


wizards = []
while True:
    ch = menu()
    if ch == 1:
        w = Wizard()
        wizards.append(w)
        print("Новый маг создан")
    if ch == 2:
        a = 1
        for i in wizards:
            print(f"Информация о маге {a}:\n")
            i.showinfo()
            a += 1
            print()
    if ch == 3:
        num = 0
        print("Введите номер мага для игры")
        while True:
            try:
                num = int(input())
            except ValueError as e:
                print(e)
            else:
                break
        Wizard.play(wizards[num - 1])
    if ch == 4:
        break
