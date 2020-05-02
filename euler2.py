def fibs(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print(sum(i for i in fibs(4000000) if i % 2 == 0))
