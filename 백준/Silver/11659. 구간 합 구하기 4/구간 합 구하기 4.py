import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
temp = 0
prefix_sum = [0] # 합 배열

# 합 배열 생성
for i in nums:
    temp += i
    prefix_sum.append(temp)

# 합 배열에서 구간 합 구하기
for i in range(m):
    num1, num2 = map(int, input().split())
    print(prefix_sum[num2]-prefix_sum[num1-1])
