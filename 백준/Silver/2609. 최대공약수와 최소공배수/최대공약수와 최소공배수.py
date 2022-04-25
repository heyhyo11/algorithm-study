import sys


A, B = map(int, sys.stdin.readline().rstrip().split())

factor = max(A, B)

while True:
  if A % factor == 0 and B % factor == 0:
    multiple = A * B / factor
    break
  factor -= 1

print(factor, int(multiple), sep='\n')