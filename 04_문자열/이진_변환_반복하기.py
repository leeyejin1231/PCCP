# 이진 변환 반복하기 - level2
def solution(s):
    number = 0
    zeros = 0
    
    while s != '1':
        number += 1
        zeros += s.count('0')
        s = s.replace('0', '')
        s = str(bin(len(s))[2:])
    
    return [number, zeros]

