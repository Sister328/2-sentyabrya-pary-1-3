class Translator:
    def add(self, eng, rus):
        if "tr" not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        if "tr" in self.__dict__:
            self.tr.pop(eng, None)

    def translate(self, eng):
        if "tr" not in self.__dict__:
            return False
        return self.tr.get(eng, False)


tr = Translator()

pairs = [
    ("tree", "дерево"),
    ("car", "машина"),
    ("car", "автомобиль"),
    ("leaf", "лист"),
    ("river", "река"),
    ("go", "идти"),
    ("go", "ехать"),
    ("go", "ходить"),
    ("milk", "молоко"),
]

for eng, rus in pairs:
    tr.add(eng, rus)

tr.remove("car")
print(*tr.translate("go"))
