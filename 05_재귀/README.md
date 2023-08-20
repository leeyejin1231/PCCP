# 재귀 함수란?
> 자기 자신을 호출하는 함수

## for문에서 벗어나기
### 구현해야할 알고리즘이 반복문보다 훨씬 자연스러울 떄
### 상태 변화를 위한 변수 사용 감소
### 전반적인 가독성 증가

```python
def fib_rec(n):
    if n < 3: return 1
    return fib_rec(n - 1) + fib_rec(n - 2)
```
```python
def fib_tail(n, first, second):
    if n <= 1: return second
    return fib_tail(n - 1, second, first + second)
```
