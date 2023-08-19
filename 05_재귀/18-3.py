# 모음사전 - Level2
# 등비수열의 합으로 구하는 방법
def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5**(5-i)-1)/ (5-1)*"AEIOU".index(n)+1
    return answer