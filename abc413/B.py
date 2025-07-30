N = int(input())
S = [input().strip() for _ in range(N)]
ans = []

for i in range(N):
    for j in range(N):
        if i != j:
            ans.append(S[i] + S[j])

ans.sort()
ans2 = []
for i in range(len(ans)):
    if i == 0 or ans[i] != ans[i - 1]:
        ans2.append(ans[i])

print(len(ans2))