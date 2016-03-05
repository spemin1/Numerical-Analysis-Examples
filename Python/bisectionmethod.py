import math

n = 0
eps = 1e-3
a = input("a: ")
b = input("b: ")

# def f(x):
#     return x*math.exp(-x)+math.pow(x, 3.0)+1

def f(x):
    return ((math.pi-2*x)*math.sin(x)*math.cos(x)-math.pow(math.sin(x), 2))

#    print("n", "  a", "  b", "    m", "    f(a)*f(m)", "|Dx/2|")

while True:
    m = (a + b) / 2.0
    Dx = math.fabs((b - a) / 2.0)
    print(n+1, a, b, m, f(a), f(m), f(a)*f(m), Dx)
#    print(n+1, "%.4f" % a, "%.4f" % b, "%.4f" % m, "+" if f(a) * f(m) > 0 else "-", "%.4f" % Dx)
    if f(a) * f(m) < 0:
        b = m
    else:
        a = m
    n += 1
    if Dx < eps:
        break
