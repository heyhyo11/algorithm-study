import sys

# 1. 전부 적힌 리스트 만들기
dial_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0


# 2. 입력 받기
S = list(sys.stdin.readline().rstrip())


# 3. 루프문 돌면서 하나의 알파벳이 있는지 확인하기
for i in S:
  for j in dial_list:
    if i in j:
      result += dial_list.index(j) + 3

# 4. 결과 출력
print(result)