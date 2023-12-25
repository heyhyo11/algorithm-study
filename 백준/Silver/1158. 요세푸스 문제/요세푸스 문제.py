import sys

input = sys.stdin.readline

# 구현 방법: 인덱스에 K를 더하고 리스트 길이를 넘어가면 % 연산으로 확인한다.

N, K = map(int, input().split())
index = 0
L = list(range(1, N+1))
ans = []

for _ in range(N):
    index += K-1
    if index >= len(L):
        index = index%len(L)
    ans.append(str(L.pop(index)))

print('<', ', '.join(ans), '>', sep='')