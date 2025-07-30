T = int(input())
while T > 0:
    T -= 1
    N = int(input())
    S = input().strip()
    S = "0"+S
    ok = [0] * (1 << N)
    ok[0] = 1
    for i in range(1<<N):
        if ok[i] == 0:
            continue
        for j in range(N):
            if i & (1<<j):
                continue
            next = (i | (1 << j))
            if S[next] == "0":
                ok[next] = 1
    if ok[(1 << N) - 1]:
        print("Yes")
    else:
        print("No")
