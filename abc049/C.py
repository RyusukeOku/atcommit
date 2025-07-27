def solve_revised():
    s = input().rstrip()
    reversed_s = s[::-1]
    reversed_words = ["maerd", "remaerd", "esare", "resare"] # 事前に反転させておく

    i = 0
    n = len(reversed_s)

    while i < n:
        matched = False
        # 長い単語からチェックすると効率が良い場合がある
        # dreamer (7), eraser (6), dream (5), erase (5)
        for word in ["remaerd", "resare", "maerd", "esare"]:
            if reversed_s.startswith(word, i):
                i += len(word)
                matched = True
                break
        
        # 4つの単語のいずれとも一致しなかった場合
        if not matched:
            print("NO")
            return

    # ループを最後まで完走した場合
    print("YES")

solve_revised()