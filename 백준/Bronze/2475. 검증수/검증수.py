import sys

num_list = list(map(int, sys.stdin.readline().rstrip().split()))
sum = 0

for i in num_list:
  sum += i**2
  
print(sum%10)
