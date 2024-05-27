import sys, heapq
input = sys.stdin.readline

t = int(input()) # 테스트 데이터 개수

for _ in range(t):
    k = int(input()) # 소설을 구성하는 장의 수
    answer = 0
    program = list(map(int, input().split()))
    heapq.heapify(program)

    while len(program) > 1:
        num1 = heapq.heappop(program)
        num2 = heapq.heappop(program)
        answer += num1 + num2
        heapq.heappush(program, num1+num2)
    
    print(answer)