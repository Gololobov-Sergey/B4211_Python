
def printLine(length=10, symbol='*'):
    for i in range(length):
        print(symbol, end='')
    print()

printLine()
printLine(20)
printLine(15, '#')
'''printLine(10, '*')
printLine(15, '@')
printLine(5, 'mama')'''

def add(a, b):
    c = a + b
    return c

print(add(3,4))

def isEven(a):
    if a % 2 == 0:
        return True
    else:
        return False

l = [34,54,56,67,76,53,34,32]
count = 0
for i in l:
    if(isEven(i)):
        count += 1

print(count)