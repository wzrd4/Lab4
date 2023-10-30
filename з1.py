class Calculator:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def fillvalues(self):
        while(True):
            try:
                self.__num1 = int(input("Введите первое значение     "))
                self.__num2 = int(input("Введите второе значение     "))
            except ValueError as e:
                print(e)
            else:
                break

    def sum(self):
        print(f"Суммируем {self.__num1} и {self.__num2}")
        return self.__num1 + self.__num2

    def dif(self, order=1):
        if order == 1:
            print(f"Отнимаем {self.__num2} от {self.__num1}")
            return self.__num1 - self.__num2
        elif order == 2:
            print(f"Отнимаем {self.__num1} от {self.__num2}")
            return self.__num2 - self.__num1
        else:
            return "Неправильное значение порядка"

    def mult(self):
        print(f"Умножаем {self.__num1} на {self.__num2}")
        return self.__num1 * self.__num2

    def div(self, order=1):
        if order == 1:
            print(f"Делим {self.__num1} на {self.__num2}")
            return self.__num1 / self.__num2
        elif order == 2:
            print(f"Делим {self.__num2} на {self.__num1}")
            return self.__num2 / self.__num1
        else:
            return "Неправильное значение порядка"


a = Calculator(12, 4)
a.fillvalues()
print(a.sum())
print(a.dif(1))
print(a.dif(2))
print(a.dif(3))
print(a.mult())
print(a.div())
print(a.div(2))
