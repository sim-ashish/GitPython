''' Python has following bult-in dataTypes
    Texttype : str
    Numeric Types : int, float, complex
    Sequence Type : list, tuple, range, strings
    Mapping Type  : dict (Dictionary)
    Set Typex     : set, frozenset
    Boolean Type  : bool
    Binary Types  : bytes, bytearray, memoryview
    None Type     : NoneType '''


a = 5                   # Integer DataType
b = 5.3                 # Float DataType
c = 2+3j                # Complex DataType
d = [2,3,'Ashish']              #   List DataType
e = (1,2,3,4,5.6)               #   Tuple DataType
f = range(1,12)                 #   Range DataType, it will return Iterator Object
g = "hello"                     #   String DataType, can be written inside single quote also
h = {"a":1,"b":2}               #   Dictionary DataType
i = {1,2,3,4,5,6}               #   Set
j = frozenset({1,2,3,4,5,6})    #   frozen Set
k = True                        #   boolean DataType, it can have False also or (0,1)
l = b"Hello"                    #   bytes
m = bytearray(5)                #   bytearray
n = memoryview(bytes(5))        #   memoryview
o = None                        #   None DataType


''' We use type() function tio check the DataType of the Variable '''

print(type(a));
print(type(b));
print(type(c));
print(type(d));
print(type(e));
print(type(f));
print(type(g));
print(type(h));
print(type(i));
print(type(j));
print(type(k));
print(type(l));
print(type(m));
print(type(n));
print(type(o));

''' We can check the Size of the Variable using getsizeof() function from sys module'''
from sys import getsizeof
print(getsizeof(a))
print(getsizeof(b))
''' ........ '''

''' Setting The Specific DataType'''

x = str("Hello World")	                        #str	
x = int(20)	                                    #int	
x = float(20.5)	                                #float	
x = complex(1j)	                                #complex	
x = list(("apple", "banana", "cherry"))	        #list	
x = tuple(("apple", "banana", "cherry"))	    #tuple	
x = range(6)	                                #range	
x = dict(name="John", age=36)	                #dict	
x = set(("apple", "banana", "cherry"))	        #set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	                                    #bool	
x = bytes(5)	                                #bytes	
x = bytearray(5)	                            #bytearray	
x = memoryview(bytes(5))                        #memoryview


''' Note : Its Important to see how these dataTypes are stored in memory '''