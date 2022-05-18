# 참고사이트: https://yoonsang-it.tistory.com/49
import sys

# 입력 받고, 0으로 구성된 num_list를 만든다
N = int(sys.stdin.readline())
num_list = [0] * 10001

# num_list의 입력 받은 숫자와 동일한 인덱스에 +1을 해준다 
for _ in range(N):
  num_list[int(sys.stdin.readline())] += 1
  
# 답 출력  
for i in range(10001):
  if num_list[i] != 0:
    for j in range(num_list[i]):
      print(i)