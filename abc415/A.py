N = int(input())
A = list(map(int, input().split()))
X = int(input())

contains = False
for i in range(N):
    if A[i] == X:
        contains = True
        break

print("Yes" if contains else "No")