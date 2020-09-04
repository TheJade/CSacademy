#EASY
#Odd Divisor count
#100/100
#Jade FjestaD

# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

a = get_number()
b = get_number()

count = 0

for i in range(a, b + 1):
    t = i ** (1/2)
    if (t / int(t) == 1):
        dif = 2 * t + 1
        num = i
        while (num <= b):
            num += dif
            dif += 2
            count += 1
        break

print(count)
