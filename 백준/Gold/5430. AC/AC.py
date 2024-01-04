import sys
from collections import deque


input = sys.stdin.readline
n = int(input())


for i in range(n):
    command = input()
    arr_len = int(input())
    arr = input()[1:-2].split(',')
 
    deq = deque(arr)

    flag = 0 # R의 개수에 따라 마지막 reverse 할지 말지 결정됨

    if arr_len == 0:
        deq = []

    for j in command:
        if j == 'R':
            flag += 1
        elif j == 'D':
            if len(deq) == 0:
                print('error')
                break
            else:
                if flag % 2: # 홀수
                    deq.pop()
                else: # 짝수
                    deq.popleft()
    else:
        if flag % 2: # 홀수
            deq.reverse()
            print("[" + ",".join(deq) + "]")
        else: # 짝수
            print("[" + ",".join(deq) + "]")
