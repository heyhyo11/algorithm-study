import sys

input = sys.stdin.readline

k = int(input()) # 부등호 개수
arr = input().split() # 실제 부등호 목록
check = [True] * 10 # 방문 표시
mx, mn = "", "" # 출력할 최댓값, 최솟값

# 부등호에 따라 숫자가 잘 배치되었는지 확인 용도
def possible(i, j, s):
    if s == '<':
        return i < j
    if s == '>':
        return i > j
    
# 실제 로직
def solve(cnt, temp):
    global mx, mn

    # 종료 조건 (숫자는 항상 부등호 개수보다 +1)
    if cnt == k+1:
        if len(mn)==0:
            mn = temp
        else:
            mx = temp
        return
    
    # 숫자는 중복 없이 0~9까지 있으므로 전부 돌려본다.
    for i in range(10):
        # 방문하지 않았고,
        if check[i]: 
            # 처음이거나 부등호 관계를 만족하는 경우 아래 실행
            if cnt == 0 or possible(temp[-1], str(i), arr[cnt-1]):
                check[i] = False
                solve(cnt+1, temp+str(i))
                check[i] = True

solve(0, "")
print(mx, mn, sep='\n')