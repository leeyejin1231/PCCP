# 삼각 달팽이 - level2
def solution(n):
    result = [[0] * i for i in range(1, n+1)]
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    x, y = 0, 0
    angle = 0
    num = 1
    
    for i in range(n):
        for _ in range(i, n):
            result[y][x] = num
            nx = x + dx[angle]
            ny = y + dy[angle]
            num += 1
            if 0 <= nx < n and 0 <= ny < n and result[ny][nx] == 0:
                x, y = nx, ny
            else:
                angle = (angle + 1) % 3
                x += dx[angle]
                y += dy[angle]
                
    return [i for j in result for i in j]