import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

down = 0
up = max(tree)
ans = 0

while down <= up:
    mid = (down + up) // 2
    cut = 0
    cut = sum((i - mid) if (i - mid) > 0 else 0 for i in tree)
    if cut == m:
        ans = mid
        break
    elif cut > m:
        ans = mid
        down = mid + 1
    else:
        up = mid-1

print(ans)