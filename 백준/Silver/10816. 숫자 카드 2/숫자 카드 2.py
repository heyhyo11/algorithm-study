## 참고 사이트: https://chancoding.tistory.com/45

from collections import Counter
import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

N_cnt_list = Counter(N_list)
print(' '.join(f'{N_cnt_list[i]}' if i in N_cnt_list else '0' for i in M_list))