def avgScore(dick):
    avg = 0
    c = 0
    for y in dick.values():
        for score in y.values():
            avg += score
            c += 1
    avg = avg / c
    return avg

dick = {"sergei": {'math' : 91, 'science' : 92, "comp sci" : 93, "english" : 94}, "sissi": {'math' : 98, 'science' : 95, "comp sci" : 85, "english" : 99}}
print(avgScore(dick))