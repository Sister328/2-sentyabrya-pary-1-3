class DataBase:
    lst_data = []
    FIELDS = ("id", "name", "old", "salary")

    def insert(self, data):
        for line in data:
            values = line.split()
            item = dict(zip(self.FIELDS, values))
            self.lst_data.append(item)

    def select(self, a, b):
        return self.lst_data[a:b + 1]


# Методы выше добавлены в существующий класс DataBase.
# При необходимости проверки:
# db = DataBase()
# db.insert(["1 Сергей 35 120000", "2 Федор 23 12000", "3 Иван 13 1200"])
# print(db.select(0, 2))
