''' Python operators are categorized in the following categories −
    Arithmetic Operators
    Comparison (Relational) Operators
    Assignment Operators
    Logical Operators
    Bitwise Operators
    Membership Operators
    Identity Operators '''

## Arithmetic Operators 

'''     Operator	Operation	        Example
        +	        Addition	        5 + 2 = 7
        -	        Subtraction	        4 - 2 = 2
        *	        Multiplication	    2 * 3 = 6
        /	        Division	        4 / 2 = 2
        //	        Floor Division	    10 // 3 = 3
        %	        Modulo	            5 % 2 = 1
        **	        Power	            4 ** 2 = 16 
'''
a = 7
b = 2

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b)  



## Comparision Operators

'''
    Operator	    Meaning	                    Example
    ==	            Is Equal To	                3 == 5 gives us False
    !=	            Not Equal To	            3 != 5 gives us True
    >	            Greater Than	            3 > 5 gives us False
    <	            Less Than	                3 < 5 gives us True
    >=	            Greater Than or Equal To	3 >= 5 give us False
    <=	            Less Than or Equal To	    3 <= 5 gives us True
'''

a = 5

b = 2

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)


## Assignment Operator
'''
    Operator	Name	                        Example
    =	        Assignment Operator	            a = 7
    +=	        Addition Assignment	            a += 1 # a = a + 1
    -=	        Subtraction Assignment	        a -= 3 # a = a - 3
    *=	        Multiplication Assignment	    a *= 4 # a = a * 4
    /=	        Division Assignment	            a /= 3 # a = a / 3
    %=	        Remainder Assignment	        a %= 10 # a = a % 10
    **=	        Exponent Assignment	            a **= 10 # a = a ** 10
'''

a = 21
b = 10
c = 0
print ("a: {} b: {} c : {}".format(a,b,c))
c = a + b
print ("a: {}  c = a + b: {}".format(a,c))

c += a
print ("a: {} c += a: {}".format(a,c))

c *= a
print ("a: {} c *= a: {}".format(a,c))

c /= a 
print ("a: {} c /= a : {}".format(a,c))

c  = 2
print ("a: {} b: {} c : {}".format(a,b,c))
c %= a
print ("a: {} c %= a: {}".format(a,c))

c **= a
print ("a: {} c **= a: {}".format(a,c))

c //= a
print ("a: {} c //= a: {}".format(a,c))


## Logical Operators

'''
    Operator	Example	        Meaning
    and	        a and b	        Logical AND: True only if both the operands are True
    or	        a or b	        Logical OR:  True if at least one of the operands is True
    not	        not a	        Logical NOT: True if the operand is False and vice-versa.
'''

# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False


var = 5

print(var > 3 and var < 10)
print(var > 3 or var < 4)
print(not (var > 3 and var < 10))


## Bitwise Operator, Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.

'''
        Operator	Meaning	                Example
        &	        Bitwise AND	            x & y = 0 (0000 0000)
        |	        Bitwise OR	            x | y = 14 (0000 1110)
        ~	        Bitwise NOT	            ~x = -11 (1111 0101)
        ^	        Bitwise XOR	            x ^ y = 14 (0000 1110)
        >>	        Bitwise right shift	    x >> 2 = 2 (0000 0010)
        <<	        Bitwise left shift	    x 0010 1000)
'''

a = 20            
b = 10            

print ('a=',a,':',bin(a),'b=',b,':',bin(b))     # bin() function show binary representation
c = 0

c = a & b;        
print ("result of AND is ", c,':',bin(c))

c = a | b;     
print ("result of OR is ", c,':',bin(c))

c = a ^ b;        
print ("result of EXOR is ", c,':',bin(c))

c = ~a;           
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2;       
print ("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2;       
print ("result of RIGHT SHIFT is ", c,':',bin(c))



## Identity or Special operators
'''
    Operator	Meaning	                                                                        Example
    is	        True if the operands are identical (refer to the same object)	                x is True
    is not	    True if the operands are not identical (do not refer to the same object)	    x is not True
'''

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

print(a is c)
print(a is b)

print(a is not c)
print(a is not b)

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False

print(x2 is y2)  # prints True

print(x3 is y3)  # prints False


## Membership or Special operators
'''
    Operator	Meaning	                                                    Example
    in	        True if value/variable is found in the sequence	            5 in x
    not in	    True if value/variable is not found in the sequence	        5 not in x
'''

a = 10
b = 20
list = [1, 2, 3, 4, 5 ]

print ("a:", a, "b:", b, "list:", list)

if ( a in list ):
   print ("a is present in the given list")
else:
   print ("a is not present in the given list")

if ( b not in list ):
   print ("b is not present in the given list")
else:
   print ("b is present in the given list")

c=b/a
print ("c:", c, "list:", list)
if ( c in list ):
   print ("c is available in the given list")
else:
    print ("c is not available in the given list")


message = 'Hello world'
dict1 = {1:'a', 2:'b'}

# check if 'H' is present in message string
print('H' in message)  # prints True

# check if 'hello' is present in message string
print('hello' not in message)  # prints True

# check if '1' key is present in dict1
print(1 in dict1)  # prints True

# check if 'a' key is present in dict1
print('a' in dict1)  # prints False