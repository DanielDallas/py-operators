string1 = "Linux"
string2 = "Hint"
joined_string = string1 + string2
print(joined_string)

# Use of String Formatting
float1 = 563.78453
print("{:5.2f}".format(float1))

# Use of String Interpolation
float2 = 563.78453
print("%5.2f" % float2)


import math
# Assign values to x and n
x = 4
n = 3

# Method 1
power = x ** n
print("%d to the power %d is %d" % (x,n,power))

# Method 2
power = pow(x,n)
print("%d to the power %d is %d" % (x,n,power))

# Method 3
power = math.pow(2,6.5)
print("%d to the power %d is %5.2f" % (x,n,power))



# Boolean value
val1 = True
print(val1)

# Number to Boolean
number = 10
print(bool(number))

number = -5
print(bool(number))

number = 0
print(bool(number))

# Boolean from comparison operator
val1 = 6
val2 = 3
print(val1 < val2)


# Assign a numeric value
number = 70

# Check the is more than 70 or not
if (number >= 70):
    print("You have passed")
else:
    print("You have not passed")




# Switcher for implementing switch case options
def employee_details(ID):
    switcher = {
        "1004": "Employee Name: MD. Mehrab",
        "1009": "Employee Name: Mita Rahman",  
        "1010": "Employee Name: Sakib Al Hasan",
    }
    '''The first argument will be returned if the match found and
        nothing will be returned if no match found'''
    return switcher.get(ID, "nothing")

# Take the employee ID
ID = input("Enter the employee ID: ")
# Print the output
print(employee_details(ID))