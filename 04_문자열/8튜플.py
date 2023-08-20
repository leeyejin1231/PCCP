# 튜플 - level2
def solution(s):
    answer = []
    array = s[2:-2].split('},{')
    array.sort(key=lambda x:len(x))
    for item in array:
        for number in item.split(','):
            if int(number) not in answer:
                answer.append(int(number))

    return answer