# 참고 블로그: https://pottatt0.tistory.com/entry/%EB%B0%B1%EC%A4%80-2504-%ED%95%B4%EC%84%A4-python-%EA%B4%84%ED%98%B8%EC%9D%98-%EA%B0%92

import sys
input = sys.stdin.readline
arr = input().rstrip()
stack = []
cnt = 1
res = 0
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
        cnt *= 2
    elif arr[i] == '[':
        stack.append(arr[i])
        cnt *= 3
    elif arr[i] == ')':
        if stack == [] or stack[-1] == '[':
            print(0)
            break
        else:
            if arr[i-1] =='(':
                res+=cnt
            stack.pop()
            cnt //= 2
    elif arr[i] == ']':
        if stack == [] or stack[-1] == '(':
            print(0)
            break
        else:
            if arr[i-1] =='[':
                res+=cnt
            stack.pop()
            cnt //= 3
else:
    if stack:
        print(0)
    else:
        print(res)