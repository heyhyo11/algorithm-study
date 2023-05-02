n = int(input())
blank = 0

for i in range(n):
  print(' '*blank+'*'*n)
  n-=1
  blank+=1