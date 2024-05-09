import math
from itertools import permutations

def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):	
    	if x % i == 0:		
        	return False
    return True
                    
def solution(numbers):
    numbers = list(numbers)
    per = []
    answer = []
    for i in range(1, len(numbers)+1):
        per += list(permutations(numbers, i))
    int_num = [int(''.join(i)) for i in per]
    for i in int_num:
        if i < 2:
            continue
        if primenumber(i):
            answer.append(i)
    return len(set(answer))
