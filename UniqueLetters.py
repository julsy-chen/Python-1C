def uniqueLetters(lst):
    answer = set()
    for w in lst:
        temp = set(w)
        answer = answer.union(temp)

    return answer

lst = ["apple", "banana", "cherry", "date"]
print(uniqueLetters(lst))