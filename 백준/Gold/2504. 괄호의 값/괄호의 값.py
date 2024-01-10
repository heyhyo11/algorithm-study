import sys

input = sys.stdin.readline
string = input().rstrip()

ans = 0
num = 1
stack = []

for i in range(len(string)):

    # 괄호가 열릴 때마다 곱할 수를 정한다.
    if string[i] == '(':
        num *= 2
        stack.append(string[i])

    elif string[i] == '[':
        num *= 3
        stack.append(string[i])

    # 괄호가 닫힐 때마다 정답에 수를 더해준다.  
    elif string[i] == ')':

        # 이상한 괄호 순서일 경우 ans=0 처리해준다.
        # stack의 마지막이 [ 이거나 stack이 비어있는 경우
        if stack == [] or stack[-1] == '[':
            ans = 0
            break

        # () 인 경우 stack에서 마지막을 제거하고 ans에 더한다.
        # 더 이상 그 괄호 안에 들어갈 수 없으므로 num에도 괄호의 수를 나눈다.
        else: 
            if string[i-1] == '(':
                ans += num

            # 현재 ) 이고 stack의 마지막이 ], [ 인 경우
            # 괄호가 정상적으로 닫혔으므로 곱해주었던 수를 다시 나눠서 처음으로.
            stack.pop()
            num //= 2
    
    elif string[i] == ']':
        if stack == [] or stack[-1] == '(':
            ans = 0
            break
        else: 
            if string[i-1] == '[':
                ans += num
            stack.pop()
            num //= 3

if stack:
    print(0)

else:
    print(ans)