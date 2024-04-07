import sys

input = sys.stdin.readline

x = int(input())
n = 1

while x > n:
  x -= n
  n += 1

if n % 2 == 0:
  print(f'{x}/{n-x+1}')
else:
  print(f'{n-x+1}/{x}')