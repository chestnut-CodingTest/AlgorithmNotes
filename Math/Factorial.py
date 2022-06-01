## 반복문 구현
N = int(input())
n_factorial = 1 
for i in range(1, N+1):
    n_factorial = n_factorial * i
print(n_factorial)


## 재귀 구현
n = int(input())
def factorial(n):
    if(n == 0):
        return 1
    if(n == 1):
        return 1
    return n * factorial(n-1)
print(factorial(n))