import sys

input = sys.stdin.readline
n, k = map(int, input().split())
tmp = 0
sieve = [True] * (n + 1)
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if sieve[j] != False:
            sieve[j] = False
            tmp += 1
            if tmp == k:
                print(j)