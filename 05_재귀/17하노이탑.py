# 하노이 탑
def hanoi(n, start, to, mid, answer): # (개수, 시작점, 도착점, 중간, answer)
    if n == 1:
        return answer.append([start, to])
    hanoi(n-1, start, mid, to, answer) # (=n-1개를 중간지점으로 옮기자)
    answer.append([start, to])
    hanoi(n-1, mid, to, start, answer) # (중간에 있는 n-1개를 도착점으로 옮기자)

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer

