
'''def dupeRemover(lst):
    answer = []
    for n in lst:
        if n not in answer:
            answer.append(n)
    return answer'''

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

def dupeRemover(lst):
    return set(lst)

print(dupeRemover(lst))