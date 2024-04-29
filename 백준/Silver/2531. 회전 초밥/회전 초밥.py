# 풀이 참고

import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
ans = 0

for i in range(n):
    eat_sushi = 1
    check = [0] * (d+1)
    check[c] = 1
    for j in range(i, i+k):
        plate = sushi[j % n]

        if not check[plate]:
            eat_sushi += 1
        check[plate] += 1
    ans = max(ans, eat_sushi)

print(ans)