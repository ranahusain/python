x = input("Enter the Number to check +ve, -ve or zero : ")
x= int(x)
if x > 0:
    print("Number is +Ve")
    print("Another statement is added like this")
elif x < 0:
    print("Number is -ve")
    print("can have multiple")
    print("statements")
else:
    print("Number is Zero")
print("this will be executed always")

print("\n")
message = "Postive" if x > 0 else ("Negative" if x < 0  else ("Zero" if x == 0 else "Invalid") )
print(message)

# logical operators
# and
# or
# not

high_income=True
good_credit=True
student=False

if (high_income or good_credit) and not student:   #(True or True) and True === True
  print("Eligible")
else:
  print("Not Eligible")