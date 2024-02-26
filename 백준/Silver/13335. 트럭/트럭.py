# 참고 링크: https://velog.io/@highcho/Algorithm-bakejoon-13335

import sys

input = sys.stdin.readline

# n: 트럭 수, w: 다리길이, l: 다리 최대하중
n, w, l = map(int, input().split())
# truck: 트럭 무게 리스트
truck = list(map(int, input().split()))
 
arr = [0] * w # 다리 리스트
ans = 0
while arr: # 다리 위에 아무것도 없을 때까지
    ans += 1
    arr.pop(0) # 다리 맨 앞 삭제
    if truck: # 아직 트럭 남아있으면 다리에 올리기
        if sum(arr) + truck[0] <= l: # 하중 초과하지 않으면
            arr.append(truck.pop(0)) # 다리에 올리기
        else:
            arr.append(0) # 남은 다리 공간 채우기
print(ans)