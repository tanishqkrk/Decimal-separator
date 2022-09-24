def decsep(n):
    temp = 0
    x = len(str(n))
    a = int(n)
    ba = n % 1
    b_round = round(ba, x)
    b_temp = str(b_round)
    for i in b_temp:
        b_slice = b_temp[2::]
    b = b_slice
    x = int(b)

    return [a, x]
