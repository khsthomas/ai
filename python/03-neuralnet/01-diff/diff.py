def f(x):
    return x*x

def

dx = 0.001

def diff(f, x):
    df = f(x+dx)-f(x)
    return df/dx

print('diff(f,2)=', diff(f, 2))
