import sys

n, m = map(int, sys.stdin.readline().split())
x, y = divmod(n, m)

print(x, y, sep='\n')