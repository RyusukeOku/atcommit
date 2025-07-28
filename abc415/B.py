S = list(input().strip())

ans = []
for i in range(len(S)):
    if S[i] == '#':
        ans.append(i)
    if len(ans) == 2:
        print(f"{ans[0]+1},{ans[1]+1}")
        ans = []