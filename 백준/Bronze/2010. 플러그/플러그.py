import sys

input = sys.stdin.readline

n = int(input())
multitaps = [int(input()) for _ in range(n)]
print(sum(multitaps)-(n-1))