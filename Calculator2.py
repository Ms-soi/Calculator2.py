# A python program to help a user carryout arithmetic calculation of choice

mathematical_operations = "+, -, *, /"

num_1 = int(input("enter the first number: "))

num_2 = int(input("enter the second number: "))

math_operation = input("enter the specific operation you want to perform: ")

if math_operation == "+":

    print(num_1 + num_2)

elif math_operation == "-":

    print(num_1 - num_2)

elif math_operation =="*":

    print(num_1 * num_2)

elif math_operation == "/":

    print(num_1 / num_2)

else:

    print("enter a valid mathematical operation")


