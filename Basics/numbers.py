''' Number DataType has further 3 classification 
    integer  :  Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
    float    :  Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
    complex  :  Complex numbers are written with a "j" as the imaginary part: '''

''' We will see Memory aspects also so that we can get clear Idea about how they are stored in memory'''


int_num = 5             # Integer Type
float_num = 10.2375       # Float Type
float_num2 = 35e3       # Float can also be scientific numbers with an "e" to indicate the power of 10.
float_num3 = 12E4
float_num4 = -87.7e100

complex_num = 2+3j      # Complex Type

print(f'{int_num} {type(int_num)}')
print(f'{float_num} {type(float_num)}')
print(f'{float_num:.2f} {type(float_num)}')     # to get round and how much value want after decimal
print(f'{float_num2} {type(float_num2)}')
print(f'{float_num3} {type(float_num3)}')
print(f'{float_num4} {type(float_num4)}')
print(f'{complex_num} {type(complex_num)}')


''' Lets see how these are get store in memory '''

test_variable = 10
test_variable2 = 20

print(id(test_variable))    # id() is used to get the memory location of the variable


if(id(test_variable) == id(test_variable2)):
    print("YES THE LOCATION IS SAME")

else:
    print("NO THE LOCATION IS NOT SAME")

'''we will see if else condition later but for now just think, 
   if both variable have same location then if condition will execute otherwise else statement will execute'''

# Ofcourse the else statement got executes

# now we will do one thing
test_variable2 = 10 

# all the three test variables now have same value '10'

if(id(test_variable) == id(test_variable2)):
    print("NOW THE LOCATION IS SAME",id(test_variable), id(test_variable2))       # this time the if condition will execute

else:
    print("NO THE LOCATION IS NOT SAME")


'''Now lets change the Value of test_variable and test_variable2 and initialize values greater than 256'''

test_variable = 257
test_variable2 = 257

# Now think will they point to the same memory location?
# test this in terminal not in the VsCode IDE

if(id(test_variable) == id(test_variable2)):
    print("NOW THE LOCATION IS SAME",id(test_variable), id(test_variable2))

else:
    print("NO THE LOCATION IS NOT SAME")

'''This behavior is due to how Python handles object interning for small integers.'''

'''Small Integer Caching (Interning): Python pre-allocates and caches integer objects for values in the range -5 to 256. 
   When you assign a variable to any integer in this range, 
   Python will point both variables to the same memory location to optimize memory usage and improve performance.'''

'''Outside the Cached Range: For integers outside the range -5 to 256, 
   Python creates a new object each time an assignment is made, even if the values are the same.'''

'''For small integers, caching saves memory and speeds up operations.
   Larger integers are less frequently used, so caching them wouldn't be as efficient.'''


# Now the Question is, Interning is only done on integers? 
# We will see float now, for other datatypes we will see them on their Specific file

float_var1 = 10.0
float_var2 = 10.0

# Try to execute them in terminal not in any IDE or IDLE
if(id(float_var1)==id(float_var2)):
    print("Both float Values pointing to same memory location")
else:
    print("Both Pointing to different memory locations")

''' In the Above Block our else statement will execute, so the Interning is not done on float values, not even for small values'''



# Now we will see Type Conversion

'''Type Conversion means, Convert one dataType into another'''
'''int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
   float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
   str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals'''

# Convert into integer type

x = int(1)   # x will be 1
y = int(2.8) # y will be 2, When we convert float to int, the decimal part is truncated.
z = int("3") # z will be 3

# Convert into float type

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# Convert into Complex Type, We can’t convert a complex data type number into int data type and float data type numbers.
# We can’t apply complex built-in functions on strings.
x = complex(5)

# Convert into String dataType

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


''' There are special Numbers also in python which give us Nan (Not a Number), -inf (-ve infinity), inf (infinity) '''

import math
n = math.nan 
print(n)

x = float('inf')
y = float('-inf')
print(x)
print(y)






