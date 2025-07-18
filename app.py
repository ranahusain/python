#Everything in Python is an Object 5 is made from int class and 5 is an object "Hello" is from str class so "Hello" is an object 

for number in range(3):                 #starts from 0 
  print("Number")

for number in range(3):
  print("Number : " , number)           #can print the iterator like this


for number in range(3):
  print("Number : " ,f"[{number+1}]" )  #Output: Number: [1] 



for number in range(1,3):               #start from 1 go till < 3
  print("Number : " ,f"[{number}]" )    #Output: Number: [1] 


for number in range(1,10,2):            #start from 1 till <10 with a step of 2
  print(number, (number * "." ))        #ouput: 1 3 5 7 9 


# Loop and if else

success = False

for number in range(3):
    print("Attempt Number : ", number )
    if success == True:
      print("Success is true")
      break
else:
  print("Attempted " , number + 1 , " times")



for x in range(3):
  for y in range(3):
    print(f"{x} , {y}")


# Iterables in Python

# range is a iterable and many others like string lists and custom objects

# print(type(5))          you will get int class
# print(type(range(5)))   you will get range class , range class is iterable 

for x in range(5):
  print(x)
for x in "Python":
  print(x)
# p
# y
# t
# h
# o 
# n 

for x in [1,2,3]:
  print(x)  

# 1
# 2
# 3



# while loop

no = 100
while no > 0:
  print(no)
  no //= 2


# loop termination on sepeicfic condition

command = ""
while command != "quit":
  command = input(">> ")
  print("You entered : " , command)


# command = ""
while command.lower() != "quit":    #for comparison when the use entered somthing print as it is and then compare it with to condition by lowercasing it
  command = input(">> ")
  print("You entered : " , command)


# infinite loop

while True:
  command = input(">>")
  print("You Entered : " , command)
  if command.lower() == "quit":
    break

count = 0 
for number in range(1,10):
  if number % 2 == 0:
    count += 1
    print(number)
print(f"We have {count} even numbers")