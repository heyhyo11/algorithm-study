# 참고사이트: https://assaeunji.github.io/python/2020-05-07-bj2110/

import sys

n, c = map(int, sys.stdin.readline().split())
house = sorted([int(sys.stdin.readline()) for _ in range(n)])

start = 1
end = house[-1] - house[0]
result = 0

while (start <= end):
    mid = (start+end)//2
    old = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= old+mid:
            count+=1
            old = house[i]
    
    if count >=c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)