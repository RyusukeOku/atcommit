n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(m):
    for j in range(len(a)):
        if a[j] == b[i]:
            a.remove(b[i])
            break

print(*a)