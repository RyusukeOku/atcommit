def is_palindrome(s):
    return s == s[::-1]

def base_convert(n, base):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % base) + result
        n //= base
    return result

A = int(input())
N = int(input())

total_sum = 0
k = 1

# 奇数桁の回文を生成してチェック
while True:
    s_k = str(k)
    palindrome_str = s_k + s_k[:-1][::-1]
    palindrome_num = int(palindrome_str)
    
    if palindrome_num > N:
        break
    
    base_a_str = base_convert(palindrome_num, A)
    if is_palindrome(base_a_str):
        total_sum += palindrome_num
    
    k += 1

k = 1
# 偶数桁の回文を生成してチェック
while True:
    s_k = str(k)
    palindrome_str = s_k + s_k[::-1]
    palindrome_num = int(palindrome_str)

    if palindrome_num > N:
        break
        
    base_a_str = base_convert(palindrome_num, A)
    if is_palindrome(base_a_str):
        total_sum += palindrome_num
        
    k += 1

print(total_sum)