N, M = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
for i in range(N):
    sum += A[i]

if sum <= M:
    print("Yes")
else:
    print("No")