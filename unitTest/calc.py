def add(x, y):
    '''Add Function - Will add two values'''
    return x + y

def diff(x, y):
    '''Subtract Function - Give difference between two values'''
    return x - y

def mul(x, y):
    '''Multiply Function - Give multiplication of two numbers'''
    return x * y

def div(x, y):
    '''Division Function - Give Division result of two values'''
    if y == 0:
        raise ZeroDivisionError("Can't divide by zero")
    
    return x/y