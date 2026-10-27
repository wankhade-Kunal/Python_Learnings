# Q1 Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

# class Circle:
#     def __init__(self, radius): 
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2

#     def perimeter(self):
#         return 2 * (22/7) * self.radius

# c1  = Circle(21)
# print(c1.area())
# print(c1.perimeter())


# Q2 Define a Employee class with attributes role, department & salary. This class also has a showDetails() method.
# Create an Engineer class that inherita properties from employee & has additional attributes: name & age


# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role = ", self.role)
#         print("dept = ", self.dept)
#         print("salary = ", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "75,000")

# engi1 = Engineer("Kunal", "24")
# engi1.showDetails()


# Q3 Create a class called order which stores item & its price
# use Dunder function __gt__() to convey that:
# order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order("chips", 30)
ord2 = Order("Copi", 20)

print("It's", ord1 > ord2)
