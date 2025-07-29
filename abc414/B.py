N = int(input())

ans = ""
count = 0
for i in range(N):
    c, l = input().split()
    l = int(l)
    count += l
    if count > 100:
        ans = "Too Long"
        break
    for j in range(l):
        ans += c

print(ans)