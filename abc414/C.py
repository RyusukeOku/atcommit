a = int(input())
n = int(input())
ans = 0

def to_base_n_str(num_10, base):
    if num_10 == 0:
        return "0"
    
    str_n = ""
    while num_10 > 0:
        str_n += str(num_10 % base)
        num_10 //= base
    return str_n[::-1]

for i in range(1, n):
    i_str_10 = str(i)

    i_str_a = to_base_n_str(i, a)

    if i_str_10 == i_str_10[::-1] and i_str_a == i_str_a[::-1]:
        ans += i

print(ans)