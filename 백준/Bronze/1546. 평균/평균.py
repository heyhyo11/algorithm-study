import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))

print(sum(score) * 100 / n / max(score))