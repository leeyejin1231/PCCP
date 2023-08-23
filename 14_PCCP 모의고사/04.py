def solution(input_string):
    answer = []
    apear = []
    
    for i in range(len(input_string)):
        if input_string[i] not in apear:
            apear.append(input_string[i])
        else:
            if input_string[i-1] != input_string[i] and input_string[i] not in answer:
                answer.append(str(input_string[i]))
    if answer:
        answer.sort()
        return ''.join(answer)
    else:
        return 'N'