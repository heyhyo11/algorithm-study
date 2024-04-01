# 풀이 참고

import sys

input = sys.stdin.readline
t = int(input())

# 유클리드 호제법
def get_gcd(a, b):
	while b : 
		a, b = b, a % b
	return a

for i in range(t):
	nums = list(map(int, sys.stdin.readline().split()))
	n = nums[0]
	sum_nums = 0
	for j in range(1, n):
		for k in range(j + 1, n + 1): 
			sum_nums += get_gcd(nums[j], nums[k])
	print(sum_nums)