from itertools import permutations
import math

def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    nums = [n for n in numbers]
    num = []

    for i in range(1, len(numbers)+1):
        num += list(permutations(nums, i))
    new_num = [int(''.join(y)) for y in num]
    print(new_num)

    for i in new_num:
        if checkPrime(i):
            answer.append(i)
    
    return len(set(answer))