n = int(input())
arr = [True] * (n+1)
for i in range(2, int(n ** 0.5)+1):
    if arr[i] == True:
        for j in range(i+i, n+1, i):
            arr[j] = False

for i in range(2, n+1):
    if arr[i]:
        print(i)
