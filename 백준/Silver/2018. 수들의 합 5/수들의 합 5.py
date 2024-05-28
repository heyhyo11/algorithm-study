import sys
input = sys.stdin.readline

n = int(input())
answer = 1
start_index = 1
end_index= 1
sum = 1

while end_index != n:
    
    # 정답인 경우
    if sum == n: 
        answer += 1
        end_index += 1
        sum += end_index

    # 목표치보다 작은 경우
    elif sum < n:
        end_index += 1
        sum += end_index

    # 목표치보다 큰 경우
    else: 
        sum -= start_index
        start_index += 1

print(answer)