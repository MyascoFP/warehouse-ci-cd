
class Warehouse:
    def __init__(self):
        self.materials = {}

    def add_material(self, name, quantity):
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")

        self.materials[name] = self.materials.get(name, 0) + quantity

    def get_balance(self, name):
        return self.materials.get(name, 0)

    def write_off(self, name, quantity):
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")

        if self.get_balance(name) < quantity:
            raise ValueError("Недостаточно материала на складе")

        self.materials[name] -= quantity

    def get_total_quantity(self):
        return sum(self.materials.values())

