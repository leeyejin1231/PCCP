def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command
        print(i, j, k)
        answer = array[i-1:j]
        answer.sort()
        result.append(answer[k-1])
    
    return result