
# Comment  # Keyboard Shortcut ctrl + /
# python3 filename  # Command to Run Program


''' Doc String Used to Give Information related to Class, Functions etc.. '''

''' Below are the keywords in python
    False   await       else    import      pass
    None    break       except  in          raise
    True    class       finally is          return
    and     continue    for     lambda      try
    as      def         from    nonlocal    while
    assert  del         global  not         with
    async   elif        if      or          yield '''
# import keyword
# print(keyword.kwlist) 

# Print function
print("Hello World")   

# Variable declaration and Initialization,  Variable names are case-sensitive.
a = 5                   


# Multiple Variable declaration and initialization in the same line
b, c = 10, 15     

# Single Value assign for two variables
name = username = 'Ashish'  

# Unpacking, works with list, tuple
fruits = ["Apple", "Banana", "Cherry"]
fruit_one, fruit_two, fruit_three = fruits

print(fruit_one, fruit_two, fruit_three)


# Printing Variables
print(a,b,c)            

# Print in the same Line, we can have any seperator
print("Python", end=" ") 
print("Programming")

# Formated String use {variable | expression} to add variables in the String
print(f'Value of a is {a}, value of b is {b} and value of c is {c}')    


# Input Function to take input from console in String format
company = input("Enter Company Name: ")

# Convert it into number to get integer output
salary = int(input("Enter Your Salary: "))