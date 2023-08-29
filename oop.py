class Employee:
    # class attribute
    company = "copyassignment.com"
    # constructor
    def __init__(self, name, age, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.salary = salary
    # class method
    def myMethod1(self):
        print(f"Hi {self.name}!")
    def myMethod2(self, city):
        print(f"{self.name}, do you lives in {city}?")

# creating objects
emp1 = Employee("John", 34, 50000)
emp2 = Employee("Harry", 30, 60000)

# calling methods
emp1.myMethod1()
emp1.myMethod2("London")
