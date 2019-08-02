employees = []
class Employee:
    def __init__(salf, name, department, position, rate):
       self.name = name
       self.department = department
       self.position = position
       self.rate = rate

    def getSalary(self, hourly):
        return self.rate * hourly


employee.append(Employee("Charles Darwin", "Engineering", "Maintenance", 200))
employee.append(Employee("Anne Sullivane", "IT", "Analyst", 200))
employee.append(Employee("Marie Christine", "IT", "Developer", 200))

for e in employees:
    print("***********************")
    print(employee.index(e))
