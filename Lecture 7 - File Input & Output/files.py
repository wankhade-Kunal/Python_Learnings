# Types Of All Files
# 1. Text Files: .txt, .docx, .log etc.
# 2. Binary Files : .mp4, .mov, .png, .jpeg etc.

# Q1 Create A New File "praticeQue.txt" using Python. Add The Following Data in it:
# with open("praticeQue.txt", "w")as f:
# f.write("Hi everyone\nwe are learning File I/O\nusing java.\nI like programming in java.")
# f.close()


# Q2 WAF That Replace All Occurrences Of "java" With "python" In Above File.
# with open("praticeQue.txt", "r") as f:
#     data = f.read()

# newData = data.replace("java","python")
# print(newData)

# with open("praticeQue.txt","w") as f:
#     f.write(newData)


# Q3 Search If The Word "learning" Exists In The File Or Not.
# def findWord():
#     word  = "learning"
#     with open("praticeQue.txt","r") as f:
#         data = f.read()

#         if(word in data):
#             print("Found It")
#         else:
#             print("Not Found")

# findWord()


# Q4 WAF To Find In Which Line OF The File Does The Word "learning" Occur First.
# Print -1 If Word Not Found.
# def checkLine():
#     word = "python"
#     data = True
#     lineNum = 1
#     with open("praticeQue.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(lineNum)
#                 return
#             lineNum += 1

#     return -1
# print(checkLine())



# Q5 From a file containing numbers separated by comma, print the count of even number
def cntEven():
    cnt = 0
    with open("praticeQue.txt", "r") as f:
        data = f.read()

        nums = data.split(",")
        for val in nums:
            if(int(val) %2 == 0):
                cnt += 1
        return cnt
print(cntEven())