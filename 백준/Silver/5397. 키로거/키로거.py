import sys

input = sys.stdin.readline

# 구현 방법: 커서를 기준으로 string1(왼쪽), string2(오른쪽) 구분한다.
m = int(input())

for i in range(m):
    string1 = []
    string2 = []
    command = list(input().rstrip())
    for j in command:
        if j == '<':
            if string1:
                string2.append(string1.pop())
        elif j == '>':
            if string2:
                string1.append(string2.pop())
        elif j == '-':
            if string1:
                string1.pop()
        else:
            string1.append(j)

    string1.extend(reversed(string2))
    print(''.join(string1))