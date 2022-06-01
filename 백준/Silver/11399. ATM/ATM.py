import sys

N = int(sys.stdin.readline())
num_list = sorted(map(int, sys.stdin.readline().split()))
answer = 0

for i in num_list:
  answer += i * N
  N -= 1
  
print(answer)