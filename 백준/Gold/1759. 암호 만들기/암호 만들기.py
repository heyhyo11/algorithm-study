# 참고 링크: https://aia1235.tistory.com/71

import sys

input = sys.stdin.readline

l, c = map(int, input().split())
char_list = list(input().split())
char_list.sort()
vowel = ['a', 'e', 'i', 'o', 'u']
ans = []


def check(arr):
    v_count, c_count = 0, 0 # 모음 개수, 자음 개수

    for i in arr:
        if i in vowel:
            v_count += 1
        else:
            c_count += 1

    if v_count >= 1 and c_count >= 2:
        return True
    else:
        return False

def dfs(arr):

    if len(arr) == l:
        if check(arr):
            print("".join(arr))
            return

    for i in range(len(arr), c):
        if arr[-1] < char_list[i]:
            arr.append(char_list[i])
            dfs(arr)
            arr.pop()

for i in range(c - l + 1):
    a = [char_list[i]]
    dfs(a)