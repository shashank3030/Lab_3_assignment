class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.employee_id}\tName: {self.name}\tAge: {self.age}\tSalary: {self.salary}"


def main():
    employee_list = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    print("Sort by:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        employee_list.sort(key=lambda x: x.age)
    elif choice == 2:
        employee_list.sort(key=lambda x: x.name)
    elif choice == 3:
        employee_list.sort(key=lambda x: x.salary)
    else:
        print("Invalid choice.")
        return

    print("Sorted Employee Data:")
    for employee in employee_list:
        print(employee)


if __name__ == "__main__":
    main()
