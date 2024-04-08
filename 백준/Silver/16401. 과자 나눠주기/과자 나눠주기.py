# 풀이 참고
import sys

input = sys.stdin.readline
m, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(key=int, reverse=True)

left = 0
right = arr[0]

def isPossible(size):
    idx = 0
    eat = 0
    while idx < n and eat < m:
        if arr[idx] >= size:
            eat += int(arr[idx]/size)
            idx += 1
        else:
            break
    if eat >= m:
        return True
    return False

while right - left > 1:
    mid = int((left + right) / 2)
    if isPossible(mid):
        left = mid
    else:
        right = mid
        
if isPossible(right):
    print(right)
else:
    print(left)
