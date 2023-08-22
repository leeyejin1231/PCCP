def solution(triangle):
    n = len(triangle[-1])
    
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                left = 0
            else:
                left = triangle[i-1][j-1]
            if j == i:
                right = 0
            else:
                right = triangle[i-1][j]
                
            triangle[i][j] = triangle[i][j] + max(left, right)

    return max(triangle[n-1])