n = int(input())
serial = [input().strip() for _ in range(n)]

# 숫자만 더한다.
def add_num(num):
    temp = 0
    for elem in num:
        if elem.isdigit():
            temp += int(elem)
    return temp

# 정렬 기준: 길이, 숫자합, 사전
serial.sort(key=lambda x: (len(x), add_num(x), x))
for i in serial:
    print(''.join(i))