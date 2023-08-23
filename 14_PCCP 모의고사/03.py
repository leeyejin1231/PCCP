def solution(foods):
    answer = ''
    for idx, food in enumerate(foods):
        if idx == 0:
            continue
        answer += str(idx) * (food//2)    
    answer = answer + '0' + answer[::-1]
    return answer