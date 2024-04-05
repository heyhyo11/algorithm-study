import sys
input = sys.stdin.readline

l = 1
cnt = 0

while True:
    ans = 0
    l, p, v = map(int, input().split())
    if l == 0:
        break
    ans += (v // p) * l + min(v % p, l)
    cnt += 1
    print(f'Case {cnt}: {ans}')