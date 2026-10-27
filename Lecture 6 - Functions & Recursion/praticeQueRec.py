# Q1 Write A Recursive Functions To Calculate The Sum Of First n Natural Numbers.
# def sumOfN(n):
#     if(n == 0): 
#         return 0
#     return sumOfN(n-1) + n

# print(sumOfN(5))

# Q2 Write A Recursive Functions To Print All Element In A List.
# Hint: Use List & Index As Parameters.
def printList(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    printList(list, idx+1)

fruits = ["Mango","Banana","Apple"]
printList(fruits)