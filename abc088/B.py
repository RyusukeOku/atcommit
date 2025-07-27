N = int(input())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)
sum_A = sum(A)
sum_B = 0

for i in range(N):
    if (i+1) % 2 == 0:
        sum_A -= A[i]
        sum_B += A[i]

print(sum_A - sum_B)  # Output the result