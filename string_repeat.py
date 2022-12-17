import re

def string_repeat(text, n1, n2):
    result = ""
    if len(text) >= 5 and len(text) <= 10:
        if re.fullmatch(r"[a-zA-Z]+", text):
            result = (text + " ") * n1
            result = (result + "\n") * n2
        else:
            raise ValueError("error! : アルファベットのみを使用してください")
    else:
        raise ValueError("error! : 正しい長さの文字列を入力してください")

    return result
try:
    print(string_repeat("hello", 5, 2))
except ValueError as e:
    print(e)