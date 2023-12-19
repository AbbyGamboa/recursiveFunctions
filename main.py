# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def Fib(n):
    # Use a breakpoint in the code line below to debug your script.
    if (n == 1):
        return 1
    if (n == 2):
        return 1
    return Fib(n - 1) + Fib(n - 2)

def T(n):
    if n == 1:
        return 1
    else:
        return 2 * T(n - 1) + 1

def S(n):
    if (n == 1):
        return 1
    else:
        return S(n - 1) + n

def g(n):
    if (n == 1 or n == 2):
        return 1
    else :
        return (-4 * g(n-1)) + (4 * g(n - 2))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(Fib(5))
    print(T(4))
    print(S(3))
    print(g(4))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
