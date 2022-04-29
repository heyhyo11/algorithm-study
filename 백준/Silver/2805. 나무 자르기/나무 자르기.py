# 참고한 사이트: https://dalseoin.tistory.com/entry/

n, m = map(int, input().split())
L = list(map(int, input().split()))
down = 0
up = max(L)
answer = -1
while down <= up: 
    mid = (down + up) // 2
    tree_total = sum((i - mid) if (i - mid) > 0 else 0 for i in L)
    if tree_total == m:  # 잘린 나무의 합이 필요한 것과 일치하면 끝
        answer = mid
        break
    elif tree_total > m:  # 잘린 나무의 합이 필요한 것보다 많으면
        answer = mid
        down = mid + 1
    elif tree_total < m:  # 잘린 나무의 합이 필요한 것보다 적으면
        up = mid - 1
    
print(answer)