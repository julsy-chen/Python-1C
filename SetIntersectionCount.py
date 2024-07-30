def commonValues(lst):
    answer = 0
    
    a = lst[0]
    for n in lst:
        b = n
        c = a.intersection(b)

    return len(c)

lst = [ {1, 2, 3, 4, 5},
  {3, 4, 5, 6, 7},
  {5, 6, 7, 8, 9} ]
print(commonValues(lst))