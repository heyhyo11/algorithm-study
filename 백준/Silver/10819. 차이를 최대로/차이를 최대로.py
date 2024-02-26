from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
mx = 0

for num in permutations(arr):
    sm = 0
    for i in range(n-1):
        sm += abs(num[i]-num[i+1])
    mx = max(mx, sm)

print(mx)