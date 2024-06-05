from collections import deque

def solution(people, limit):
    cnt = 0
    deq = deque(sorted(people))
    
    while deq:
        if len(deq) == 1:
            cnt += 1
            break
            
        if deq[0] + deq[-1] <= limit:
            deq.pop()
            deq.popleft()
        else:
            deq.pop()
        cnt += 1
    return cnt