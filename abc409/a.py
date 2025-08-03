n = int(input())
t = input().rstrip()
a = input().rstrip()

want = False
for i in range(n):
    if t[i]==a[i]=='o':
        want = True
        break

if want:
    print("Yes")
else:
    print("No")