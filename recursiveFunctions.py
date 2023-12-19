# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time


def Fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)


def T(n):
    if n == 1:
        return 1
    else:
        return 2 * T(n - 1) + 1


def S(n):
    if n == 1:
        return 1
    else:
        return S(n - 1) + n


def g(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (-4 * g(n-1)) + (4 * g(n - 2))


# Press the green button in the gutter to run the script.
def timecheck(func):
    t1 = time.time()
    print(func)
    t2 = time.time()
    print('Elapsed time: {} seconds'.format((t2-t1)))


if __name__ == '__main__':

    timecheck(Fib(34))
    timecheck(T(100))
    timecheck(S(100))
    timecheck(g(34))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
