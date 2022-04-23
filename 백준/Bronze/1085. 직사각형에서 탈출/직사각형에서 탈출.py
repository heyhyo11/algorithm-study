import sys

# 1. 입력 받기
x, y, w, h = map(int, sys.stdin.readline().rstrip().split())

# 2. x, y축 최소거리 구하기
x_distance = min(w-x, x)
y_distance = min(h-y, y)

# 3. 최종 최소거리 구하기
print(min(x_distance, y_distance))