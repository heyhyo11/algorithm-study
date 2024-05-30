from collections import deque

def solution(numbers, target):
    queue = deque()
    n = len(numbers)
    answer = 0
    
    queue.append([numbers[0], 0]) # 양수, 인덱스
    queue.append([-1 * numbers[0], 0]) # 음수, 인덱스
    
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        
        if idx < n: # 모든 원소를 양수, 음수로 나눠서 큐에 넣는다
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
                
    return answer