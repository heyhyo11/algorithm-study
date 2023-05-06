import sys

piece = [1, 1, 2, 2, 2, 8]
data = list(map(int, sys.stdin.readline().split()))

for i in range(len(data)):
  piece[i] -= data[i]

print(*piece)