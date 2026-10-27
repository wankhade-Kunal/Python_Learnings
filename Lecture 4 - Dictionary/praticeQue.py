# Q1 Store Following Word Meanings In A Python Dictionary
# List -> []
# Tuples -> ()

# dict = {
#     "table" : ["A Piece Of Furniture", "List Of Facts & Figures"],
#     "cat" : "A Small Animal"
# }

# print(dict)
# print(type(dict))

# Q2 You Are Given A List Of Subjects For Students. Assume One Classroom Is Required For 1 Subject. How Many Classrooms Are Needed By All Students.

# subjects = {"Python", "Java", "C++", "Python", "JavaScript", "Java", "Python", "Java", "C++", "C"}
# print(subjects)
# print(len(subjects))
# print(type(subjects))


# Q3 WAP To Enter Marks Of 3 Subjects From The User & Store Them In A Dictionary.
# Starts With An Empty Dictionary & Add One By One. Use Subject Name As Key & Marks As Value.

# user = {}

# student = int(input("Enter Your Physics Marks: "))
# user.update({"Physics" : student})

# student = int(input("Enter Your Chemistry Marks: "))
# user.update({"Chemistry" : student})

# student = int(input("Enter Your Math Marks: "))
# user.update({"Math" : student})

# print(user)


# Q4 Figure Out A Way To Store 9 & 9.0 As Separate Values In The Set.
# 1 Possible Solution (We can Make 9.0 to String)
# values = {9, "9.0"}
# print(values)
# print(type(values))

# 2 way for the answer
# Tuples -> ()
values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)
print(type(values))
print(len(values))