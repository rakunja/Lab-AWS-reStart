x = lambda a : a + 10
print(x(5))

def myfunc(n):
    return lambda a : a*n

dbl = myfunc(2)
tpl = myfunc(3)

print(dbl(11))
print(tpl(11))
