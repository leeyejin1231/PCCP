def solution(numbers):    
    numbers = list(map(str, numbers))             
    numbers.sort(key = lambda x : x*3, reverse=True)  
        
    return str(int(''.join(numbers)))



3
30
301

333
303030
3013013031