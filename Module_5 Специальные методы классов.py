class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        new_floor = int(number_of_floors)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")
        return self.name

h1 = House('ЖК Гнездо кукушки', 18)

h2 = House('Домик бобра', 2)

print(h1)
print(h2)
print(len(h1))
print(len(h2))
