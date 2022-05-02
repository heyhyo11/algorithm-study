import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial(n-1)

answer = factorial(N) // (factorial(K) * factorial(N-K))
print(answer)