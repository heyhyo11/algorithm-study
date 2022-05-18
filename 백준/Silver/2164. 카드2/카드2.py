# 참고 사이트: https://tooo1.tistory.com/88

from collections import deque
import sys

N = int(sys.stdin.readline())
deque = deque([i for i in range(1, N+1)])

while len(deque) != 1:
  deque.popleft()
  move_num = deque.popleft()
  deque.append(move_num)
  
print(deque[0])