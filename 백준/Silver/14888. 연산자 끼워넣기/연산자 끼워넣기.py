# 풀이참고

import sys

input = sys.stdin.readline

def dfs(n, sm, add, sub, mul, div):
    global mn, mx
    # [예외처리] 결과값/중간 값의 범위: int(-1e8)~int(1e8)
    if sm < int(-1e9) or int(1e9)<sm:
        return

    # 종료조건(정답처리): arr의 마지막 요소에 도달했을 때
    if n==N:
        mn = min(mn, sm)
        mx = max(mx, sm)
        return

    # 하부호출: 연산자 개수 남았을 경우만 호출 가능
    if add>0: # 더하기
        dfs(n+1, sm+arr[n], add-1, sub, mul, div)
    if sub>0: # 빼기
        dfs(n+1, sm-arr[n], add, sub-1, mul, div)
    if mul>0: # 곱하기
        dfs(n+1, sm*arr[n], add, sub, mul-1, div)
    if div>0: # 나누기
        dfs(n+1, int(sm/arr[n]), add, sub, mul, div-1)

N = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

mn, mx = int(1e9), int(-1e9)
dfs(1, arr[0], add, sub, mul, div)
print(mx, mn, sep='\n')