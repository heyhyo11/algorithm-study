import sys

input = sys.stdin.readline

n, m = map(int, input().split())
waiting_list = {}
cnt = 1

for _ in range(m):
    student_id = input().strip()
    if student_id in waiting_list:
        del waiting_list[student_id]
        waiting_list[student_id] = 1
    else:
        waiting_list[student_id] = 1

print(*list(waiting_list.keys())[:n], sep='\n')
