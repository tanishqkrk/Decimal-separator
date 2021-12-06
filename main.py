n = float(input("Enter a decimal number: "))
x = len(str(n))


def part(n):
    temp = 0
    a = int(n)

    ba = n % 1
    b_round = round(ba, x)
    b_temp = str(b_round)
    for i in b_temp:
        b_slice = b_temp[2::]
    b = b_slice

    print(a)
    print(b)


part(n)
