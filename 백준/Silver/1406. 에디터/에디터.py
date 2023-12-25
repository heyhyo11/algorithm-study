import sys

input = sys.stdin.readline

# 구현 방법: 커서를 기준으로 string1(왼쪽), string2(오른쪽) 구분한다.
string1 = list(input().strip()) # 왼쪽
string2 = [] # 오른쪽
m = int(input())

for i in range(m):
    command = input().split()
    if command[0] == 'L':
        if string1:
            string2.append(string1.pop())
    elif command[0] == 'D':
        if string2:
            string1.append(string2.pop())
    elif command[0] == 'B':
        if string1:
            string1.pop()
    else:
        string1.append(command[1])

string1.extend(reversed(string2))
print(''.join(string1))