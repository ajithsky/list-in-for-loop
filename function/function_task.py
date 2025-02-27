#1
def number(num):
    if num%2 == 0:
        print("Even.")
    else:
        print("odd")

prnit(number(5))





#2

def string(str):
    return str[::-1]

print(string("hello"))




#3


def num(n):
    return sum(n)


print(num([1,2,3,4,5]))
