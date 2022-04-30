import sys

def prime_number(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

N = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0

for i in num_list:
  if i == 1:
    continue
  elif prime_number(i):
    cnt += 1
    
print(cnt)