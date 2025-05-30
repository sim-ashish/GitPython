import logging

######## Logging Levels ##########
# DEBUG : Detailed information, typically of interest only when diagnosing problems.

# INFO : Confirmation that things are working as expected

# WARNING : An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected .

# ERROR : Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL : A serious error, indicating that the program itself may be unable to continue running

'''Default level is warning'''
# Changing Default level 
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='test.log', level=logging.DEBUG)  # Including a file for log rather than logging to console



def add(x, y):
    '''Addition Function'''
    return x + y

def sub(x, y):
    '''Subtraction Function'''
    return x - y

def mul(x, y):
    '''Multiplication Function'''
    return x * y

def div(x, y):
    '''Divide Function'''
    return x / y

num1 = 10
num2 = 5

add_result = add(num1, num2)
# print('Addition: {} + {} = {}'.format(num1, num2, add_result))
logging.debug('Addition: {} + {} = {}'.format(num1, num2, add_result))


sub_result = sub(num1, num2)
# print('Subtract: {} + {} = {}'.format(num1, num2, sub_result))
logging.debug('Subtract: {} + {} = {}'.format(num1, num2, sub_result))




mul_result = mul(num1, num2)
# print('Multiplication: {} + {} = {}'.format(num1, num2, mul_result))
logging.debug('Multiplication: {} + {} = {}'.format(num1, num2, mul_result))




div_result = div(num1, num2)
# print('Division: {} + {} = {}'.format(num1, num2, div_result))
logging.debug('Division: {} + {} = {}'.format(num1, num2, div_result))

