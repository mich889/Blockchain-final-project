def add(a, b):
    res = []
    res.append((a & b) + (a | b))
    res.append((a ^ b) + (a & b)*2)
    res.append((~a & b) + (a & ~b) + 2*(a & b))
    return (all(res))


for i in range(10):
    for j in range(10):
        print(add(i, j))
