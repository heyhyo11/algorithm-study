import sys
input = sys.stdin.readline


all_nums = list(range(2, 246912))
check = []

def prime_numbers(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True	

for i in all_nums:
    if prime_numbers(i):
        check.append(i)

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    for i in check:
        if n < i <= 2*n:
            cnt += 1
    print(cnt)