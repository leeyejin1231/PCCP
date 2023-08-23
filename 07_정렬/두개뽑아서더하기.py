from itertools import combinations

def solution(numbers):
    answer = []
    combi = list(combinations(numbers, 2))
    answer = [a+b for a, b in combi]
    answer = list(set(answer))
    
    return sorted(answer)