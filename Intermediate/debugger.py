'''pdb module is used for debugging'''
import pdb

def transform(x, y):
    z = x + y
    return z

z = 5
x = 50
y = 60
n = 1000

pdb.set_trace()         # this is a break point
transform(x, y)

print('z = ' + str(z))

n = transform(2,3)                #  p(n) to print variable n
print('n = ' + str(n))


'''
n ---- execute next line
c ---- complete execution
l ---- list 3 lines before and after current line
s ---- step into function call
b ---- show list of all break points
b[int] ---- set break point at line number (eg. b10)
f[func] ----- break at function name
cl ----- clear all break points
cl[int] ----- clear break point at line number (eg. cl10)
p ----- print
'''
