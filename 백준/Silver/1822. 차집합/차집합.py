import sys

input = sys.stdin.readline

n_a, n_b = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

ans =[]

for i in set_a:
    if i not in set_b:
        ans.append(i)
        
ans.sort()
print(len(ans))
print(*ans)

