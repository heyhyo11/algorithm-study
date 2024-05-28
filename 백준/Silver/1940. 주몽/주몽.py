import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

answer = 0
i = 0
j = n-1

while i < j:
    # 정답인 경우
    if n_list[i] + n_list[j] == m:
        answer += 1
        i += 1
        j -= 1
    
    # 목표치가 부족한 경우
    elif n_list[i] + n_list[j] < m:
        i += 1
    
    # 목표치를 초과한 경우
    else:
        j -= 1

print(answer)