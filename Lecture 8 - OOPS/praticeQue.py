# # Q1 Create student class that takes name & marks of 3 subjects as a arguments in constructor.
# # Then create a method to print the average.

# class Student():
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def getAvg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "Your avg score is: ", sum/3)

# stu1 = Student("Ron", [98,23,45])
# stu1.getAvg()

# stu2 = Student("Rohit", [24,55,67])
# stu2.getAvg()

# stu3 = Student("Krish", [44,56,77])
# stu3.getAvg()


# Q2 Create account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance

class Account:
    def __init__(self, initial_balance, account_number):
        self.balance = initial_balance
        self.account_number = account_number

    def credit_debit(self, debit_amount, credit_amount,):
        self.balance -= debit_amount
        print("Rs", debit_amount, "Debit from your account")
        print("Your current balance is:", self.balance)

        self.balance += credit_amount
        print("Rs", credit_amount, "Credit in your account")
        print("Your current balance is:", self.balance)

ramesh = Account(10000, 13214)
ramesh.credit_debit(1000, 500)


