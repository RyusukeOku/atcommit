n = int(input())
a = list(map(int, input().split()))
k = int(input())

count = 0
for i in range(n):
    if a[i] >= k:
        count += 1

print(count)