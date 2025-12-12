#dynamic typing in Python
n = 0
print('n =',n)

n = 'abc'
print('n =',n)

# Multiple assignments
n, m = 1, 2
print('n =',n)
print('m =',m)  

# Incrementing a variable
n = n + 1
n += 1
print('n =',n)

# None is null(no value) in Python
n = 0
n = None
print('n =',n)

# If statement
# No parentheses needed around conditions
# Indentation is used to define blocks
# Parentheses are needed for multiple lines
# && is and, || is or, ! is not
n = 1
if (n > 0 and n < 5) or n == -10:
    n += 1
elif n == 0:
    n = 1
else:
    n -= 1
    
# While loop are same
n = 0
while n < 5:
    print('n =',n)
    n += 1
    
# For loop with range
for i in range(5):
    print('i =',i)  
    
for i in range(2,6):
    print(i)