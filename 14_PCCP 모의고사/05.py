from itertools import permutations

def solution(ability):
    answer = 0
    n, m = len(ability), len(ability[0])
    combi = list(permutations([i for i in range(n)], m))
    
    for students in combi:
        stats = 0
        for i, student in enumerate(students):
            stats += ability[student][i]
        answer = max(answer, stats)
    
    return answer