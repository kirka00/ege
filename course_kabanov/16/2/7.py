def fact(n):
    x = 1
    for i in range(1,n+1): 
           x *= i
    return x

def f(n):
    if n >= 50: 
        return fact(n)
    if 1 <=n <= 50: 
          return 2 * f(n + 1) // (n + 1)
print(1000 * f(7) // f(4))