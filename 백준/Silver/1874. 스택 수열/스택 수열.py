import sys

n = int(sys.stdin.readline())
stack = []
answer = []
cnt = 1
error_message = "YES"

for i in range(n):
  num = int(sys.stdin.readline())
  
  while cnt <= num:
    stack.append(cnt)
    answer.append('+')
    cnt += 1
    
  if stack[-1] == num:
    stack.pop()
    answer.append('-')
  else:
    error_message = 'NO'
  
if error_message == 'NO':
  print('NO')
else:
  print(*answer, sep='\n')