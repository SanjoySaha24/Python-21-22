# Write a program to read two numbers from the user and perform basic mathematical operations (addition, multiplication,
# subtraction, division) by handling all possible exceptions.

try:
    a, b = map(int, input('Enter two numbers: ').split())
    c = input('Enter a for addition, m for multiplication, s for subtraction , d for division : ')
    if c == 'a':
        print('Addition-', a+b)
    elif c == 'm':
        print('Multiplication-', a*b)
    elif c == 's':
        print('Subtraction-', a-b)
    elif c == 'd':
        print('Division-', a/b)
except(TypeError, ZeroDivisionError, ArithmeticError, FloatingPointError, OverflowError, ValueError) as e:
    print('Errors handled-\n', e)
else:
    print('No error(s) found')
