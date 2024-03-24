import sys

input = sys.stdin.readline
coins = []
n, k = map(int, input().split()) 

# 동전 넣기
for _ in range(n):
    coins.append(int(input()))
    
# 동전 정렬 (내림차순)   
coins.sort(reverse=True)

# 정답
ans = 0

# 큰 액수부터 돌면서 계산
for coin in coins:
    if k >= coin:
        ans += k // coin # 동전 개수
        k %= coin # 남은 금액
        if k <= 0: # 계산이 끝나면 중간에 나오기
       		break
            
print(ans) 