import sys
import sys
from collections import deque

input = sys.stdin.readline

# N: 데이터 개수, L: 최소값 구하는 범위
# mydeque: 데이터 담을 덱 자료구조
# now: 주어진 숫자 데이터 가지는 리스트

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    # 덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    # 덱의 마지막 위치에 현재 값 저장
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i-L: # 윈도우 범위 벗어나면 첫 번째 값 삭제
        mydeque.popleft()
    print(mydeque[0][0], end=' ')