import scipy as sp

def error(f,x,y):
    return sp.sum((f(x) - y)**2)

def func(x):
    return x**2

x = sp.array([1,2,3])
print(x)
y = func(x)
print(y)


fpl, residuals, rank, sv, rcond = sp.polyfit(x,y,1,full=True)
