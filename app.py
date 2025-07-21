#Everything in Python is an Object 5 is made from int class and 5 is an object "Hello" is from str class so "Hello" is an object 

def greets():
  print("Hi There !")
  print ("Welcome Aboard")

greets()


#difference b/w argument and parameter parameter is input defined for function greet(x,y) 
# where argument is actual value given for argument ("Hussain","Ashraf")

def greet(first_name,last_name):
  print(f"Hello {first_name} {last_name} !")
  print ("Welcome Aboard")


first_input = input("First Name : ")
second_input = input("Last Name : ")

greet(first_input,second_input)


#two types of function
# perform a task
# return a value


def greet(name):
    print(f"Hello, {name}!")  # Just performs a task

greet("Alice")


def add(a, b):
    return a + b  # Returns a value

result = add(5, 3)        #by doing this fucntion value can be used anywhere
print("Sum is:", result)


# example of using a function that return a value

result = add(5,3)
file = open("context.txt","w")
file.write(str(result))
file.close()


# all functions by default return none (none means there is a absence of value) 
# unless we specifically return a value 

print(greet("Alice")) # what will be the output ?  here we have used no return    ==> none
print(add(5,3))       # what will be the output ?  here we have used return       ==> 8


def increment(number,by):
   return number+by

print(increment(2,1))     #python will call the function inside print and store the result in a temporary variable that we dont see and then print it 


# how to make parameter option

def increment(number,by=1):
   return number+by

print(increment(2))  # passing only one argument and other it takes by default, defualt parameters should at last in list

def increment(number,by=1):
   return number+by
                      # here we overide the default value by 5
print(increment(2,5))  



def multiply(*numbers):  # *numbers allows you to pass any number of arguments.
    print(numbers)       # you'll see all packed like list

multiply(2,3,4,5)

def multiply(*numbers):  # *numbers allows you to pass any number of arguments.
    total = 1
    for number in numbers:
       total *= number
    return total

print(multiply(2,3,4,5))