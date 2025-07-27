N = int(input())
d = [int(input()) for _ in range(N)]
d.sort(reverse=True)
ans = 0
for i in range(N):
    if i == 0:
        ans += 1
    elif d[i] == d[i-1]:
        continue
    else:
        ans += 1

print(ans)