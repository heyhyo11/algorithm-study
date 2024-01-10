import sys

input = sys.stdin.readline
ans = 0
left_cnt = 0

string = input().rstrip()

for i in range(len(string)):

    # string[i]이 왼쪽 괄호라면 left_cnt += 1
    if string[i] == '(':
        left_cnt += 1
    
    else:
        # 스택이 비어있지 않고 그 전의 string[i]가 ( 인 경우, pop()
        # left_cnt(왼쪽 괄호) 개수 - 1
        # ans += left_cnt
        if string[i-1] == '(':
            left_cnt -= 1
            ans += left_cnt

        # 스택이 비어있지 않고 그 전의 string[i]가 ) 인 경우, pop() 1번
        # left_cnt(왼쪽 괄호) 개수 - 1
        # ans += 1
        elif string[i-1] == ')':
            left_cnt -= 1
            ans += 1

print(ans)