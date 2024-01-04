import sys
from collections import deque


input = sys.stdin.readline
deq = deque()
n = int(input())

for i in range(n):
    command = input().rstrip().split()
    if command[0] == 'push_front':
        deq.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        deq.append(int(command[1]))
    elif command[0] == 'pop_front':
        if len(deq) <= 0:
            print(-1)
        else:
            print(deq.popleft())
    elif command[0] == 'pop_back':
        if len(deq) <= 0:
            print(-1)
        else:
            print(deq.pop())
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if len(deq) <= 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(deq) <= 0:
            print(-1)
        else:
            print(deq[0])
    elif command[0] == 'back':
        if len(deq) <= 0:
            print(-1)
        else:
            print(deq[-1])