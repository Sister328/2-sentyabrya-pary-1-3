class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    total_mem_slots = 4

    def __init__(self, name, cpu, *memories):
        self.name = name
        self.cpu = cpu
        self.mem_slots = list(memories[:self.total_mem_slots])

    def get_config(self):
        memory = "; ".join(
            f"{mem.name} - {mem.volume}" for mem in self.mem_slots
        )
        return [
            f"Материнская плата: {self.name}",
            f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
            f"Слотов памяти: {self.total_mem_slots}",
            f"Память: {memory}"
        ]


cpu = CPU("Intel Core i5", 3.5)
mem1 = Memory("Kingston", 16)
mem2 = Memory("Samsung", 8)

mb = MotherBoard("ASUS Prime", cpu, mem1, mem2)
