import sys
input = sys.stdin.readline
n = int(input())
num = map(int, list(input().rstrip()))

print(sum(num))