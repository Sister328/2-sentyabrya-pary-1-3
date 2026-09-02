class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age


cats = [
    Cat("Британская", "Барсик", 3),
    Cat("Сиамская", "Мурка", 2),
    Cat("Мейн-кун", "Лео", 4),
]

for cat in cats:
    print(f"Имя: {cat.name}, порода: {cat.breed}, возраст: {cat.age}")
