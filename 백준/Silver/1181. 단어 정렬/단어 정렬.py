import sys

input = sys.stdin.readline
n = int(input())
ans = []

for _ in range(n):
  str = input().rstrip()
  ans.append(str)
  
ans = list(set(ans))
ans.sort(key=lambda x:(len(x), x))

print(*ans, sep="\n")