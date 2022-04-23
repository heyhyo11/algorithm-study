import sys

# 1. 입력 받기
x, y, w, h = map(int, sys.stdin.readline().rstrip().split())

# 3. 최종 최소거리 구하기
print(min(x, y, w-x, h-y))