with open("files/24.txt") as f:
    s = f.readline().replace("O", "P").replace("N", "P")
    k = kmax = 1
    for i in range(1, len(s)):
        if s[i - 1] + s[i] != "PP":
            k += 1
            kmax = max(k, kmax)
        else:
            k = 1
print(kmax)

# 57
