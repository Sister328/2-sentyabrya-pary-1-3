class Car:
    def __init__(self):
        self._engine_temperature = 20

    def start_engine(self):
        self._engine_temperature = 90
        print("Двигатель прогрет")

    def drive(self):
        if self._engine_temperature >= 90:
            print("Поехали!")
        else:
            print("Двигатель не прогрет. Сначала прогрейте двигатель.")


car = Car()

# Попытка ехать без прогрева.
car.drive()

# Прогрев двигателя и движение.
car.start_engine()
car.drive()

# Атрибут с одним подчёркиванием считается внутренним
# и не предназначен для прямого использования извне.
print(f"Текущая температура двигателя: {car._engine_temperature}")
