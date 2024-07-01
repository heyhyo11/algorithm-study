import sys

input = sys.stdin.readline
string = list(input())

for char in string:
    if char == char.upper(): # 대문자인 경우
        print(char.lower(), end='')
    else: # 소문자인 경우
        print(char.upper(), end='')