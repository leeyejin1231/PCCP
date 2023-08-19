# 문자열이란?
## 문자열의 특징
```python
big = "Programmers"
small = 'Programmers'
multiple = """Programmers with style
I like it a lot"""
```
### 문자열이란?
유니코드 사용  
배열로 취급하며, 비열처럼 사용할 수 있음
```python
sample = "Programmers is good"
print(sample[0])
print(sample[15:])
sample[15:] = "awesome"
```

### 문자열의 문제 유형
1. 문자열 뒤집기
a[::-1]
2. 아스키 코드 다루기
```python
chr(65)
ord(‘a’)
# 퀴즈(?)
print(chr(67))
```
### 진법 변경하기
```python
# 2진법 (return 문자열)
bin()
# 8진법 (return 문자열)
oct()
# 16진법 (return 문자열)
hex()
# 문자열 s를 n진수로 변환한 거 되돌리기 (10진수)
int(s, n)
```
### 애너그램 확인하기
> 영단어의 철자 위치를 바꿔 다른 영단어를 만들어 내는 문제

- 두 단어를 주고 이 단어가 애너그램인지 확인하는 문제
- 많은 단어를 주고, 이 중에서 애너그램 찾아내는 문제
### 문자열에서 원하는 문자 찾기
### 기준에 맞춰 재정렬하기
### 문자열 치환하기
a.replace('before', 'after')
### 정규표현식 다루기
```python
import re
```

# 정규 표현식
RE (Regular expression)  
> 수많은 문자열에서 원하는 데이터를 뽑아내기 위한 형태나 규칙을 정의하는 언어  

## 정규표현식이란?
### 자주 사용하는 정규표현식 (외우자!🥲)