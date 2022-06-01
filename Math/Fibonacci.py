# 반복문 구현
N = int(input())
Fn = 0; Fn1 = 1; Fn2 = Fn + Fn1
if(N == 0):
    print("0")
else:
    for i in range(N-2):
        Fn = Fn1
        Fn1 = Fn2
        Fn2 = Fn + Fn1
    print(Fn2)


## 재귀 구현
n = int(input())
def fibonacci(n):
    if(n <= 1):
        return n
    return fibonacci(n-1) +fibonacci(n-2)
print(fibonacci(n))