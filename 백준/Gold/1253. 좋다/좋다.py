import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
answer = 0

# 좋은 수 타겟을 하나씩 이동한다
for k in range(n):
    find = a[k] # 좋은 수
    i = 0
    j = n-1
    while i < j:
        # 좋은 수 찾은 경우
        if a[i] + a[j] == find:
            if i != k and j != k:
                answer += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1

        # 좋은 수보다 작은 경우
        elif a[i] + a[j] < find:
            i += 1
        
        # 좋은 수보다 큰 경우
        else:
            j -= 1

print(answer)
