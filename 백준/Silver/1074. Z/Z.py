# 풀이 참고

import sys
from collections import deque
 
input = sys.stdin.readline

N, r, c = map(int, input().rstrip().split())

def z(N, r, c, q):
    if N == 0:
        return(q)
    half = 2**(N-1)
    if r < half:
        if c < half:
            quad = 1
        else:
            quad = 2
            c -= half
    else:
        if c < half:
            quad = 3
            r -= half
        else:
            quad = 4
            r -= half
            c -= half

    q += (quad-1) * (half**2)
    return (z(N-1, r, c, q))
print(z(N, r, c, 0))