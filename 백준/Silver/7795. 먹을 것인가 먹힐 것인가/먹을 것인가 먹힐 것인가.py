import sys

input = sys.stdin.readline

# 그냥 전체 돌리면 시간 초과 나서 이분 탐색으로 진행
def binary(target, arr):
    start = 0
    end = len(arr) - 1
    res = -1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res


t = int(input())

for _ in range(t):
    ans = 0
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    for i in a:
        ans += binary(i, b) + 1
    
    print(ans)