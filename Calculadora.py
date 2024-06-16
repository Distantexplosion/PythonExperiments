import math

def add(a, b):
    c = int (a) + int (b)
    return c

def sub(a, b):
    c = int (a) - int (b)
    return c

def div(a, b):
    c = int (a) / int (b)
    return c

def mul(a, b):
    c = int (a) * int (b)
    return c

def exp(a, b):
    c = int (a) ** int (b)
    return c

def fac(n):
    if (int (n) == 1):
        return 1
    c = int (n) * fac(int (n)-1)
    return c

fibs={0:1, 1:1}
def fib(n):
    if (int (n) in fibs):
        print('fibs[{}] was {}'.format(n, fibs[int(n)]))
        return fibs[int (n)]
    
    c = fib(int (n)-1) + fib(int (n)-2)
    fibs [n] = c
    return c

def pi(n):
    # Initialize denominator
    k = 1
 
    # Initialize sum
    s = 0
    
    for i in range(int (n)):
    
        # even index elements are positive
        if i % 2 == 0:
            s += 4/k
        else:
            # odd index elements are negative
            s -= 4/k
    
        # denominator is odd
        k += 2
        
    return s

def is_command_valid(x):
    return x == '+' or x =='-' or x == '/' or x == '*' or x == '**' or x == '!' or x == 'fib' or x == 'pi'

command = input("What operation would you like, master? (+, -, /, *, **, !, fib, pi, return to exit): ")

while (is_command_valid(command)):
    if(command == '+'):
       a = input('a:')
       b = input('b:')
       c = add(a, b)
       print(c)

    if(command == '-'):
       a = input('a:')
       b = input('b:')
       c = sub(a, b)
       print(c)

    if(command == '/'):
       a = input('a:')
       b = input('b:')
       c = div(a, b)
       print(c)
   
    if(command == '*'):
       a = input('a:')
       b = input('b:')
       c = mul(a, b)
       print(c)

    if(command == '**'):
        a = input('a:')
        b = input('b:')
        c = exp(a, b)
        print(c)

    if(command == '!'):
        a = input('n:')
        c = fac(a)
        print(c)

    if (command == 'fib'):
        a = input ('n:')
        c = fib(a)
        print(c)

    if (command == 'pi'):
            a = input ('n:')
            c = pi(a)
            print(c)
            print (c - math.pi)

    command = input("What operation would you like, master? (+, -, /, *, **, !, fib, pi, return to exit): ")


