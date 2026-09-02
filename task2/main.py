class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    def draw(self):
        print(f"На экране рисуется кот {self.name}, порода {self.breed}.")


cats = [
    Cat("Британская", "Барсик", 3),
    Cat("Сиамская", "Мурка", 2),
    Cat("Мейн-кун", "Лео", 4),
]

for cat in cats:
    cat.draw()
