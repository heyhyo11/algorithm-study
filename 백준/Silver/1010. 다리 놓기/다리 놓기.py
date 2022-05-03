import math, sys

T = int(sys.stdin.readline())

for _ in range(T): # mCn = m! / ((m-n)!n!)
  N, M = map(int, sys.stdin.readline().rstrip().split())
  answer = math.factorial(M) // (math.factorial(M-N) * math.factorial(N))
  print(answer)