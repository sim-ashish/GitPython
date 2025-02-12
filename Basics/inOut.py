''' print(object= separator= end= file= flush=) fucntion is used to show output
    Here,
    object - value(s) to be printed
    sep (optional) - allows us to separate multiple objects inside print().
    end (optional) - allows us to add add specific values like new line "\n", tab "\t"
    file (optional) - where the values are printed. It's default value is sys.stdout (screen)
    flush (optional) - boolean specifying if the output is flushed or buffered. Default: False'''

print("Python Programming")

# Python print() with end Parameter

print("Hello", end = ' ')
print("Coders")

# Python print() with sep parameter

print('New Year', 2025, 'See you soon!', sep= '. ')

# Print Concatenated Strings

print("Python" + "Library")

## Output formatting, Sometimes we would like to format our output to make it look attractive. This can be done by using the str.format() method.

a = 10
b = 15
print("Value of a is {} and value of b is {}".format(a,b))

print("Name is {0} and balance is {1:9.3f}".format("Ashish", 250.2236)) # positional arguments
print("Name is {name} and balace is {bal:6.5}".format(name="Ashish", bal=556.2366)) # Keyword Argument

# integer arguments
print("The number is:{:d}".format(123))

# float arguments
print("The float number is:{:f}".format(123.4567898))

# octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))



''' input(prompt) function is used to take arguments from console'''

# using input() to take user input
num = input('Enter a number: ')

print('You Entered:', num)

print('Data type of num:', type(num))   # It takes input in String, we can type cast it using int(), float() etc......


''' We have another option to take arguments from the console at the run time, which is args '''
import sys # we gave to import sys module to use argv, which is array

print(sys.argv[1])              # python3 inOut.py hello

#It will print hello

