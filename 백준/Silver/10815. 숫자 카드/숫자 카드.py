import sys

input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

for i in check:
    if i in cards:
        print('1', end=' ')
    else:
        print('0', end=' ')