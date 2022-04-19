count1 = int(input())

for i in range(count1):
    count2 = 0
    num = list(map(int, input().split()))
    if len(num) > 1:
        del num[0]
    avg = sum(num) / len(num)
    for j in range(len(num)):
        if num[j] > avg:
            count2 += 1
    percent = count2/len(num) * 100
    print(f"{percent:.3f}"+"%")