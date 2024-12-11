from symtable import Class
# Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
class House:  # Создайте класс House.
    def __init__(self, name, number_of_floors):  # Внутри класса House определите метод __init__,
        self.name = name  # в который передадите название
        self.number_of_floors = number_of_floors  # и кол-во этажей.
        new_floor = int(number_of_floors)

    def go_to(self,
              new_floor):  # Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
            return
        for i in range(1, new_floor + 1):
            print(i)


h1 = House('ЖК Высокий', 18)  # Создайте объект класса House с произвольным названием и количеством этажей.
h2 = House('Домик бобра', 2)  # Создайте объект класса House с произвольным названием и количеством этажей.

h1.go_to(5)  # Вызовите метод go_to у этого объекта с произвольным числом.
h2.go_to(5)  # Вызовите метод go_to у этого объекта с произвольным числом.
