# 풀이 참고

import sys

input = sys.stdin.readline

n = int(input())
student = list(map(int, input().split()))
student.sort()
ans = 0

def solve(down, up, goal):
    global ans
    max_idx = n
    while down < up:
        tmp = student[down] + student[up]
        if tmp < goal:
            down += 1
        elif tmp == goal:
            if student[down] == student[up]:
                ans += up - down
            else: 
                if max_idx > up:
                    max_idx = up
                    while max_idx >= 0 and student[max_idx-1] == student[up]:
                        max_idx -= 1
                ans += up - max_idx + 1
            down += 1
        else:
            up -= 1

for i in range(n-2):
    down = i+1
    up = n-1
    goal = -student[i]
    solve(down, up, goal)
    
print(ans)