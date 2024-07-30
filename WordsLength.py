def wordLength(lst):
    a = {}

    for w in lst:
        n = len(w)
        a.update({w : n})

    return a

lst = ["apple", "banana", "cherry", "date"]
print(wordLength(lst))