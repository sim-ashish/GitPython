import logging
import logger

logging.basicConfig(filename='Basic.log', level=logging.DEBUG,
                    format = '%(asctime)s:%(levelname)s:%(message)s') 


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
logging.debug('Addition: {} + {} = {}'.format(num1, num2, add_result))


sub_result = sub(num1, num2)
logging.debug('Subtract: {} + {} = {}'.format(num1, num2, sub_result))




mul_result = mul(num1, num2)
logging.debug('Multiplication: {} + {} = {}'.format(num1, num2, mul_result))




div_result = div(num1, num2)
logging.debug('Division: {} + {} = {}'.format(num1, num2, div_result))

