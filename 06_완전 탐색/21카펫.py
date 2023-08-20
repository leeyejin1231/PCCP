# 카펫 - level2
# 어쨌거나, 다 합치면 넓이, 나눠서 길이를 구하자
def solution(brown, yellow):
    grid = brown + yellow
    for n in range(3, int(grid ** 0.5) + 1): #최소 길이3. 세로 부터 구하자.
        if grid % n != 0:
            continue
        m = grid // n
        if (n-2) * (m-2) == yellow: # 감싸져 있기 때문에 -2 씩 해주기.
            return[m, n]