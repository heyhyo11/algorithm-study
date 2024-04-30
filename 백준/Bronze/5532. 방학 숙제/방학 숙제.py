import sys, math

input = sys.stdin.readline

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

ans = l - (max(math.ceil(b/d), math.ceil(a/c)))
print(ans)