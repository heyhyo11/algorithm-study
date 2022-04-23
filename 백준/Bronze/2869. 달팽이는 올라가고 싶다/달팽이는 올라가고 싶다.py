import sys, math


# 1. 입력 받기
A, B, V = map(int, sys.stdin.readline().rstrip().split()) # 사용자 입력
D = 0 # 거리
day = 0 # 날짜

# 2. 계산하기 A*day - B*(day-1) >= V, 즉 day >= (V-B)/(A-B)
day = (V-B)/(A-B) # 반복문 쓰면 시간 초과가 나와서 한번에 계산해야 함
print(math.ceil(day)) # 4.2는 5일이 걸린다는 뜻