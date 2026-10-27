# Q1 Print The Element Of The Following List Using A Loop:
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for val in nums:
#     print(val)


# Q2 Search For A Number X In This Tuple Using Loop:
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the value X: "))
idx = 0
for val in nums:
    if(val == x):
        print("Found at Idx", idx)
    idx += 1