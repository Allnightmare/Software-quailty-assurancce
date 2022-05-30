# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def maximum(a, b):

    if a >= b:
        return a
    else:
        return b


def reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1


def areaCircle(r):
    return (math.pi*r**2)


def circumCircle(r):
    return (2*math.pi*r)


def prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(maximum(5, 1))
    print(reverse("helloWorld"))
    print(areaCircle(3))
    print(circumCircle(3))
    print(prime(3))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
