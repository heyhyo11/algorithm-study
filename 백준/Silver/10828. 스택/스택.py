import sys

num_list = []

# 구현하기 전, 참고용
# push x: append(x)
# pop: pop(-1)
# size: len(num_list)
# empty: if len(num_list) == 0
# top: print(num_list[-1])

N = int(sys.stdin.readline().rstrip())

for i in range(N):
  command = list(sys.stdin.readline().rstrip().split())
  if command[0] == 'push':
    num_list.append(command[1])
  elif command[0] == 'pop':
    if len(num_list) == 0:
      print(-1)
    else:
      print(num_list.pop())
  elif command[0] == 'size':
    print(len(num_list))
  elif command[0] == 'empty':
    if len(num_list) == 0:
      print(1)
    else:
      print(0)
  elif command[0] == 'top':
    if len(num_list) == 0:
      print(-1)
    else:
      print(num_list[-1])