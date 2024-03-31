import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    ans = 0
    max = 0
    n = int(input())
    price = list(map(int,input().split()))
    
    for i in range(n-1, -1, -1):
        if price[i] > max:
            max = price[i]
        else:
            ans += max - price[i]
    print(ans)