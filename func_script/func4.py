#coding: utf-8


def my_sum(*arg):
    return sum(arg)

def my_average(*arg):
    return sum(arg) / len(arg)


def dec(func):
    def in_dec(*arg):
        if len(arg) == 0:
            return 0

        for val in arg:
            if not isinstance(val, int):
                return 0

        return func(*arg)
    return in_dec

mysum = dec(my_sum)
myaverage = dec(my_average)


print (mysum(1,2,3,4,5))
print (mysum(1,2,3,4,5, '6'))

print (myaverage(1,2,3,4,5))
print (myaverage(1,2,3,4,5))
print (myaverage())
