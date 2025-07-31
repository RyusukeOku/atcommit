s = input().strip()
t = input().strip()


is_match = True
for i in range(len(s)):
    if i == 0:
        continue
    if not is_match:
        break
    if ord("A") <= ord(s[i]) <= ord("Z"):
        for j in range(len(t)):
            if s[i-1] == t[j]:
                is_match = True
                break
            else:
                is_match = False

if is_match:
    print("Yes")
else:
    print("No")