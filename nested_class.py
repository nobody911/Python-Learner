class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.position}: {self.name}"

    def add_employees(self, name, position):
        new_employee = self.Employee(name=name, position=position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [emp.get_details() for emp in self.employees]

company1 = Company("Jack's Pizza")        
company2 = Company("Krusty Place")

company1.add_employees(name="Oggy", position="delivery boy")
company1.add_employees(name="Jack", position="Manager")

company2.add_employees(name="Squidward", position="Cashier")
company2.add_employees(name="Spongbob", position="Cook")

print(company1.name)
for employee in company1.list_employees():
    print(employee)

print()

print(company2.name)
for employee in company2.list_employees():
    print(employee)