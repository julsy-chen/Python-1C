def charFrequency(string):
    a = {}
    string = sorted(string.lower())

    for c in string:
        n = string.count(c)
        a.update({c : n})

    return a 

string = "helLo"
print(charFrequency(string))