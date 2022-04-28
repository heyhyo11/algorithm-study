import sys

N = int(sys.stdin.readline().rstrip())

def fibonacci(N):
  if N == 0:
    return 0
  elif N == 1:
    return 1
  return fibonacci(N-2) + fibonacci(N-1)

print(fibonacci(N))