n = int(input())
a = list(map(int, input().split()))

a.sort()
b =[]
for i in range(n):
    if a[i] not in b:
        b.append(a[i])

print(len(b))
print(*b)