class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{gd.name}: {gd.price}" for gd in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()

cart.add(TV("Samsung Smart TV", 55000))
cart.add(TV("LG OLED", 90000))
cart.add(Table("Компьютерный стол", 15000))
cart.add(Notebook("Lenovo IdeaPad", 65000))
cart.add(Notebook("ASUS VivoBook", 70000))
cart.add(Cup("Кружка", 500))
