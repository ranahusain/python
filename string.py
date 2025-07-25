# Simple Strings
name = "Hussain"
print(len(name))  # print the length
print(name[0:3])  # print a substring
print(name[-1])   # -1 goes to the end
print(name[-7])   # Will Print H
print(name[0:])   # no end index so go till end
print(name[:3])   # no start index go till 3 start from 0


# EscapSequence in Python
course = "Python \"Programming\""  # Will Print Python "Programming"
print(course)

# types of escape sequences
# \ "
# \ '
# \\
# \n
# \t

# Formatted Strings
first = "Hussain"
last = "Ashraf"

# full = first + " " + last
# print(full)

full = f"{first} {last}"
print(full)

# print(f"{first} {last}")  can also be printed like this

# while working with this we can put any valid expression b/w them
# full = f"{len(first)} {2+2}"
# print(full)

#String Methods

course = "   Python Programming   "
print(course.upper())
print(course.lower())
print(course.strip()) #remove the white spaces we have rstrip and lstrip
print(course.find("Pro")) #finds the index of P
print(course.replace("P","J")) #replaces p with j
print("Pro" in course)  #find "pro" in our string boolean true or false
print("Pro" not in course)  #find "pro" in our string boolean true or false

print(course)
