import sys

A, B = sys.stdin.readline().rstrip().split()

A = list(A)
B = list(B)

A.reverse()
B.reverse()

A = int(''.join(map(str, A)))
B = int(''.join(map(str, B)))

print(max([A, B]))