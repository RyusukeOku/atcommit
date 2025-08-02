n, q = map(int, input().split())
x = list(map(int, input().split()))

b = [0] * n
ans = []
for i in range(q):
    if x[i] >= 1:
        b[x[i] - 1] += 1
        ans.append(x[i])
    else:
        tmp = b.index(min(b))
        b[tmp] += 1
        ans.append(tmp + 1)

print(*ans)