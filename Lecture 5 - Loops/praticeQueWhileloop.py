# Q1 Print Number From 1 To 100
# val = 1
# while val <= 100:
#     print("I'm CEO")
#     # print("I'm CEO",val)
#     val += 1


# Q2 Print Numbers From 100 To 1
# val = 100
# while val >= 1:
#     print("I Made It", val)
#     val = val - 1


# Q3 Print The Multiplication Table Of A Number n.
# n = int(input("Enter The Number: "))
# val = 1
# while val <= 10:
#     print(n * val)
#     val = val + 1


# Q4 Print The Elements Of The Following List Using A Loop.
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx],idx)
#     idx += 1


# Q5 Search For A Number X In This Tuple Using Loop
val = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter The Value X: "))
idx = 0
while idx < len(val):
    if(val[idx] == x):
        print("Found At Index:",idx)
        break
    idx += 1  
else:
        print("Not Found")
