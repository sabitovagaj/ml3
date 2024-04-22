from sympy import Symbol, solve

x = Symbol("x")
p=solve(x**2+x**3 - 1)
print(p)
