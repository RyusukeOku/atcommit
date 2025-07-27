S = input()
T = S

char_list = list(T)
count = 0
for i in range(len(S)):
    if char_list[i] == "." and count < 1:
        char_list[i] = "o"
        count += 1
        continue

    elif char_list[i] == "#":
        count = 0
        continue

new_s = "".join(char_list)
print(new_s)