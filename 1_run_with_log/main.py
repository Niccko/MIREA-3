from rwl import run_with_log


def func():
    a = 1/0
    print(a)

run_with_log(func)