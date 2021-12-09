def combine(d1, d2):
    sol = d1
    k1 = d1.keys()
    k2 = d2.keys()
    for key in k2:
        if key in sol.keys():
            sol[key] += d2[key]
        else:
            sol[key] = d2[key]

    return sol

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

print(combine(d1, d2))
