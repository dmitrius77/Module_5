class House:
    houses_history = [] # В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0]) # Дополните метод __new__ так, чтобы Название объекта добавлялось в список cls.houses_history.
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

#    def __len__(self):
#        return self.number_of_floors
#
#    def __str__(self):
#        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")
#
#    def __eq__(self, other):
#        return self.number_of_floors == other.number_of_floors
#
#    def __lt__(self, other):
#        return self.number_of_floors < other.number_of_floors
#
#    def __le__(self, other):
#        return self.number_of_floors <= other.number_of_floors
#
#    def __gt__(self, other):
#        return self.number_of_floors > other.number_of_floors
#
#    def __ge__(self, other):
#        return self.number_of_floors >= other.number_of_floors
#
#    def __ge__(self, other):
#        return self.number_of_floors >= other.number_of_floors
#
#    def __ne__(self, other):
#        return self.number_of_floors != other.number_of_floors
#
#    def __add__(self,value):  # __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
#        self.number_of_floors += value
#        return self
#
#    def __radd__(self, value):
#        return self.__add__(value)
#
#    def __iadd__(self, value):
#        return self.__add__(value)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)


# Удаление объектов
del h2
del h3

print(House.houses_history)