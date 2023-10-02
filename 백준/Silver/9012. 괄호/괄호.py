## 참고한 사이트: https://pacific-ocean.tistory.com/70
import sys


T = int(sys.stdin.readline().rstrip())


for _ in range(T):
  S = sys.stdin.readline().rstrip()
  sum = 0
  for i in S:
    if i == '(':
      sum += 1
    elif i == ')':
      sum -= 1
    if sum < 0:
      print('NO')
      break
  if sum > 0:
    print('NO')
  elif sum == 0:
    print('YES')


## 강의 참고
# for _ in range(int(input())):
#     stk = []
#     is_vps = True
#     for ch in input():
#         if ch == '(':
#             stk.append(ch)
#         else:  # ')'
#             if stk:
#                 stk.pop()
#             else:
#                 is_vps = False
#                 break

#     if stk:
#         is_vps = False

#     print('YES' if is_vps else 'NO')
