import sys

# 입력 받기 / - 기준으로 분리
# 예시) 20 - (10 + 80) - (20 + 70)
expression = sys.stdin.readline().rstrip().split('-')
num_list = []

# + 기준으로 분리
for i in expression:
  cnt = 0
  plus = i.split('+')
  
  # + 덩어리들 더하기
  for j in plus:
    cnt += int(j)
  
  num_list.append(cnt)

# 첫 번째 요소에서 + 덩어리들을 - 해준다.   
num = num_list[0]

for i in range(1, len(num_list)):
  num -= num_list[i]
  
print(num)