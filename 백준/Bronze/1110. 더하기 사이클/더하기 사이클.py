x = input()
y = int(x)
len = 0

while True: # 26

    x = str(x)
    if int(x) < 10:
        x = "0" + x

    sum = int(x[0]) + int(x[1]) # 8
    sum = str(sum)

    if int(sum) < 10:
        sum = "0" + sum # 08

    x = int(x[1]) * 10 + int(sum[1])
    len += 1

    if y == x:
        print(len)
        break