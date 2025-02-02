class Employee:
    companyName = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Alex", 20000)
e2 = Employee("Bob", 30000)

print(e1.companyName)
print(e2.companyName)

Employee.companyName = "HighTechCorp"

print(e1.companyName)
print(e2.companyName)