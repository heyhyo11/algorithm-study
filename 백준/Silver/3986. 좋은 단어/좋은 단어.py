import sys

input = sys.stdin.readline
n = int(input())
cnt = 0

for _ in range(n):
    string = input().rstrip()
    stack = []
    
    for i in range(len(string)):
        # stack이 비어있지 않고 마지막 stack의 요소가 string[i]와 같다면 stack에서 삭제
        if stack and string[i] == stack[-1]:
            stack.pop()
        # 위의 조건이 아니라면 stack에서 삭제할 수 없으므로 append.
        else:
            stack.append(string[i])

    if not stack:
        cnt += 1

print(cnt)