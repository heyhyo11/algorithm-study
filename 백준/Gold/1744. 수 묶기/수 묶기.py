# 풀이 참고

import sys

input = sys.stdin.readline
n = int(input())

negative = []  # 음수
positive = []  # 양수
zeros = False  # 0 체크
ones = 0  # 1의 개수

for i in range(n):
    number = int(input())

    # 0
    if not number:
        zeros = True  # 수열에 0 이 있다고 표시

    # 1
    elif number == 1:
        ones += 1

    # 양수
    elif number > 0:
        positive.append(number)  

    # 음수
    else:
        negative.append(number)  


negative.sort(reverse=True) # 내림차순 정렬
positive.sort()

total = 0  # 결과

# 양수
while len(positive) > 1:  # 2개 이상
    total += positive.pop() * positive.pop()  # 가장 큰 양수들끼리 연산

if positive:  # 양수 홀수라면
    total += positive[0]  # 합에 더함

# 음수
while len(negative) > 1: 
    total += negative.pop() * negative.pop()  # 절대값이 가장 큰 음수들끼리 연산

if not zeros and negative:  # 음수 1개 남은 경우
    total += negative[0]   # 음수를 더함

# 1연산
total += ones  # 1 전부 더함

print(total)