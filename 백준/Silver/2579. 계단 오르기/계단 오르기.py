## 참고사이트: https://www.youtube.com/watch?v=1ehx6uoFZkU

import sys

def solve():
    n = int(sys.stdin.readline().rstrip())
    arr = [0] # 계단의 숫자
    for _ in range(n):
        x = int(sys.stdin.readline().rstrip())
        arr.append(x)
    g = [0, 0] # i-1번째에서 i번째 계단으로 가는 경우
    h = [0, arr[1]] # i-2번째에서 i번째 계단으로 가는 경우
    for i in range(2, n+1):
        g.append(h[i-1] + arr[i])
        h.append(max(h[i-2], g[i-2]) + arr[i])
    print(max(g[n], h[n]))
    
solve()
    