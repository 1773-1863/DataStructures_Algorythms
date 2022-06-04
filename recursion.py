# a functions that calls itself until it doesn't
# the process has to be same
# base case - terminate scenerio
# recursive case - the scenerio that calls function

print("-------------- CALL STACk / RECURSION ----------------")

def func3():
    print("three")

def func2():
    func3()
    print("two")

def func1():
    func2()
    print("one")

func1()

print("-------------- FACTORIAL/ RECURSION ----------------")

def factorial(n):
    if n < 0:
        return False
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(15))
