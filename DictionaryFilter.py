def dictFilter(dck, t):
    a = {}

    for x, y in dck.items():
        if y >= t:
          a.update({x : y})  
    
    return a

dck = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
t = 10

print(dictFilter(dck, t))
