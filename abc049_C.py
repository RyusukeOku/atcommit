def solve():
    s = str(input())
    words = ["dream", "dreamer", "erase", "eraser"]

    # 文字列と単語リストをそれぞれ反転
    reversed_s = s[::-1]
    reversed_words = [word[::-1] for word in words]

    can_match = False
    for word in reversed_words:
        # 文字列の先頭から単語が一致するか確認
        if reversed_s.startswith(word):
            # 一致した部分を除去
            remaining = reversed_s[len(word):]
            # 残りの文字列が空であればマッチ成功
            if not remaining:
                can_match = True
                break
            # 残りの文字列に対して再帰的にチェック
            if remaining in reversed_words:
                can_match = True
                break
    if can_match:
        print("YES")
        return
    else:
        print("NO")
        return

solve()