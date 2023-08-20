# 시간 복잡도
> 프로그램이 주어졌을 때, 프로그램이 입력값을 받아 동작하고 결과를 만들어내는 데 얼마나 오래 걸리는지의 정도 (얼마나 많은 메모리를 사용하는지 -> 공간 복잡도)

## 빅오 표기법
> 최악의 경우 이 정도의 시간이 걸린다  

최대 자수를 고려한다.
$$f(n) = 4n^2+4n+1$$
<div align='center'>↓</div>  

$$O(n^2)$$  

시간복잡도 크기 비교  
O(1) < O(logn) < O(n) < O(nlogn) < O(n²) < O(2ⁿ) < O(n!)

## 시간 복잡도 선택 시 참고할 만한 사항
### 최대 시간이 1초일 때 입력 데이터 수에 따른 시간 복잡도
1. 1,000개 -> O(n²) 이하
2. 10,000개 -> O(n²) 미만
3. 100,000개 -> O(nlogn) 이하
4. 1,000,000개 -> O(nlogn) 미만
5. 그 이상 -> 특정 알고리즘 사용하기
### 자주 사용하는 자료 구조의 시간 복잡도
|자료구조|탐색|삽입|삭제|
|---|---|---|---|
|배열|O(n)|O(n)|O(n)|
|정렬된 배열|O(nlogn)|O(n)|O(n)|
|연결 리스트|O(n)|O(1)|O(1)|
|스택/큐|O(n)|O(1)|O(1)|
|해시|O(1)|O(1)|O(1)|
|이진 트리|O(nlogn)|O(nlogn)|O(nlogn)|

## 시간 복잡도 줄이기
### readline() : 입력 속도를 빠르게
```python
import sys
input = sys.stdin.readline
```
### 리스트 곱셈 : 초기화 할당을 빠르게
```python
data1 = [0] * 1000
data2 = [[0] * 100 for _ in range(100)]
```
### 문자열 합치기 : ".join()"을 쓰고 +는 사용하지 말자
+는 각각의 문자열을 새로운 메모리에 복사하여 새 문자열을 만들기 때문에 시간 복잡도가 O(n²)이다.
### 조건문 연산 줄이기 : 짧은 것부터 먼저 계산하자
여러 if를 거치지 않도록 코드 구성하기
### 슬라이싱 : 불필요한 연산을 최소로
a[start:end:step]
### 표준 라이브러리 활용하기 : 속도와 안정성 모두 잡기
- heapq 최소힙
- collections (deque, counter..)
- itertools (permutations, combinations, permutations_with_replacement, permutations_with_replacement)
- math (gcd, lcm, sqrt, log, log2, factorial, exp..)
[더 많은..](https://docs.python.org/ko/3/library/math.html)
```python
    from math import gcd
    from math import lcm # 지원 안되는 버전도 있음

    lcm(a, b) #최대공배수
    gcd(a, b) #최대공약수
```
### 리스트 컴프리헨션
```python
data = []
for i in range(1, 11):
    data.append(i)
```
<div align='center'>↓</div>  
</br> 

```python  
[i for i in range(1, 11)]
```  
선언 -> 할당 -> 재구성 과정을 단 한 줄에 모두 끝낼 수 있다.

### 데이터 돌려쓰기 : 중복 피하기
```python  
def solution(data): # 제곱해서 반환
    answer = data
    for i in range(len(answer)):
        temp = answer[i] * answer[i]
        answer[i] = temp
    return answer
```
<div align='center'>↓</div>  
</br> 

```python  
def solution(data): # 제곱해서 반환
    return [i*i for i in data]
```
