# Parameters a, b, c and d are all integers
# The function should return an integer
#Four X-tremes
#EASY
#100/100
#Jade Fjestad

def four_xtremes(a, b, c, d):
    sortcount = 0
    while sortcount < 3:
        if a > b:
            temp = a
            a = b
            b = temp
        else:
            sortcount = 1
        if b > c:
            temp = b
            b = c
            c = temp
        else:
            sortcount += 1
        if c > d:
            temp = c
            c = d
            d = temp
        else:
            sortcount += 1
    return d - a
    
a, b, c, d = map(int, input().split(' '))
max_diff = four_xtremes(a, b, c, d)
print(max_diff)