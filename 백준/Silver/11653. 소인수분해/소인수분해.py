## 나의 풀이
# import sys

# N = int(sys.stdin.readline().rstrip())
# num_list = []
# cnt = 2

# while N >= cnt:
#   if N % cnt == 0:
#     num_list.append(cnt)
#     N = N / cnt
#   else:
#     cnt += 1
    
# print(*num_list, sep='\n')


## 다른 사람의 풀이
# 참고사이트: https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-11653%EB%B2%88-%EC%86%8C%EC%9D%B8%EC%88%98%EB%B6%84%ED%95%B4-in-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys

N = int(sys.stdin.readline().rstrip())
cnt = 2

while N != 1:
  if N % cnt == 0:
    N = N / cnt
    print(cnt)
  else:
    cnt += 1