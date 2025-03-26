class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def get_info(self):
        return f"{self.position}: {self.name}"
    @staticmethod
    def valid_position(pos):
        valid_pos = ["Manager", "Cook", "Cashier"]
        return f"{pos} is valid position" if pos in valid_pos else f"{pos} is not a valid position"

employee1 = Employee(name="Oggy", position="Delivery Boy")
employee2 = Employee(name="Jack", position="Manager")

print(employee1.get_info())
print(employee2.get_info())

print(Employee.valid_position("Cook"))