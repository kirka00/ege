def f(n):
    if n <= 18:
        return n + 3
    else:
        if n % 3 == 0:
            return (n // 3) * f(n // 3) + n - 12
        else:
            return f(n - 1) + n ** 2 + 5
        

k = 0
for i in range(1, 1001):
    if all(int(q) % 2 == 0 for q in str(f(i))):
        k += 1
        
print(k)