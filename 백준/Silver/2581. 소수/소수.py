import sys

def prime_number(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

prime_list = []
min_num = 0

for i in range(M, N+1):
  if i == 1:
    continue
  elif prime_number(i):
    prime_list.append(i)
    
if len(prime_list) == 0:
  print(-1)
else:    
  print(sum(prime_list))
  print(min(prime_list))