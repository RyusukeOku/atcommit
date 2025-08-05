n, s = map(int, input().split())
t = list(map(int, input().split()))

wake_up = True
for i in range(n):
    if i==0:
        if t[i] > s + 0.5:
            wake_up = False
            break
    else:
        if t[i] - t[i-1] > s + 0.5:
            wake_up = False
            break

if wake_up:
    print("Yes")
else:
    print("No")