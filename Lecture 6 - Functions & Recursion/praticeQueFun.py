# # Q1 WAF To Print The Length Of A List. [list is the parameter]
# cities = ["Pune", "Delhi", "Bengluru", "Noida"]
# heroes = ["Thor", "Ironman", "Wakanda", "Spider-Man", "Lohaman"]
# def calLen(items):
#     print(len(items))

# calLen(cities)
# calLen(heroes)

# # Q2 WAF To Print The Elements Of A List In A Single Line. [List is the parameter]
# def calLis(list):
#     for item in list:
#         print(item, end=" ")

# calLis(heroes)

# Q3 WAF To Find The Factorial Of n. (n is the parameter)
# def calFact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# calFact(5)

# Q4 WAF To Convert USD To INR
# def currConvertor(usdVal):
#     inrVal = usdVal * 94.79
#     print(usdVal, "USD =", inrVal, "INR")

# currConvertor(100)


# HOME QUESTION
n = int(input("Enter the number: "))
def checkNum(num):
    if(num % 2 == 0):
        print("Even")
    else:
        print("Odd")

checkNum(n)