import sys

while True:
  # 숫자 입력받기
  n = sys.stdin.readline().rstrip()
  
  # 0이면 while문 종료
  if n == '0':
    break

  # 처음과 끝자리수를 비교하며 리스트에 카운트
  no_list = []
  for i in range(len(n)//2):
    if n[i] != n[len(n)-1-i]:
      no_list.append('no')
  
  # answer 리스트 길이가 0이면 yes
  if len(no_list) == 0:
    print('yes')
  else:
    print('no')