import sys

input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))

down, up = 0, n-1
min_val = float('inf')
ans = [float('inf'), float('inf')]

while down < up:
    tmp_sum = liquid[down] + liquid[up]
    if abs(tmp_sum) < min_val:
        min_val = abs(tmp_sum)
        ans = [liquid[down], liquid[up]]

    if liquid[down] + liquid[up] < 0:
        down += 1
    else:
        up -= 1

print(*ans)