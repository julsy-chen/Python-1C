def FibDict(n):
    a = {0:0, 1:1}

    if n in a:
        return a
    else:
        for i in range(2, n+1):
            a[i] = a[i-1] + a[i-2]

    return a

print(FibDict(10))