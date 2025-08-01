n = int(input())
d = list(map(int, input().split()))

ans = []
for i in range(len(d)):
    j = i + 1
    while j < n:
        ans.append(sum(d[i:j]))
        j += 1
    print(*ans)
    ans = []