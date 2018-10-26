
def dec(f):
    n = 7
    def wrapper(*args, **kw):
        return f(*args, **kw) * n
    return wrapper


@dec
def foo(n):
    return n * 6

print(foo(10))
