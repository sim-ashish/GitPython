# Importing dispatch from multipledispatch to enable function overloading in Python.
# By default, Python does not support method overloading (only the last defined method is retained),
# but multipledispatch allows us to create multiple functions with the same name but different parameters.
from multipledispatch import dispatch

# Function to process a single integer
@dispatch(int)  # This decorator specifies that this function will handle a single integer argument.
def process(value: int) -> str:
    """
    Processes an integer input.
    
    Args:
        value (int): The integer value to be processed.
    
    Returns:
        str: A formatted string showing the processed integer.
    """
    return f"Processing integer: {value}"

# Function to process two integers
@dispatch(int, int)  # This decorator specifies that this function handles two integer arguments.
def process(value1: int, value2: int) -> str:
    """
    Processes two integers by summing them.
    
    Args:
        value1 (int): The first integer.
        value2 (int): The second integer.
    
    Returns:
        str: A formatted string showing the sum of the integers.
    """
    return f"Processing sum: {value1 + value2}"

# Function to process a string
@dispatch(str)  # This decorator specifies that this function handles a string argument.
def process(value: str) -> str:
    """
    Processes a string by converting it to uppercase.
    
    Args:
        value (str): The input string.
    
    Returns:
        str: A formatted string with the input string converted to uppercase.
    """
    return f"Processing string: {value.upper()}"

# Running test cases only when this script is executed directly (not when imported as a module).
if __name__ == "__main__":
    print(process(42))       # Calls process(int) -> Output: Processing integer: 42
    print(process("hello"))  # Calls process(str) -> Output: Processing string: HELLO
    print(process(4, 6))     # Calls process(int, int) -> Output: Processing sum: 10
