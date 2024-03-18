def pageCount(n,p):

    c1, c2 = 0, 0
    page = 1

    while page < p:
        c1 += 1
        page += 2

    page = n

    if n % 2 == 1:
        page -= 1

    while page > p:
        c2 += 1
        page -= 2

    return min(c1,c2)







print(pageCount(6,2))
