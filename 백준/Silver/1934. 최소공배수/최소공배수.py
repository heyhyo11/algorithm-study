import sys


T = int(sys.stdin.readline().rstrip())


def lcm(a, b):
  c, d = max(a, b), min(a, b)
  t = 1
  while t > 0:
    t = c % d
    c, d = d, t
  return int(a*b/c)


for _ in range(T):
  A, B = map(int, sys.stdin.readline().rstrip().split())
  print(lcm(A, B))
