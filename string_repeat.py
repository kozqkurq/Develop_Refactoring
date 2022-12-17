import re
import numpy

def string_repeat_rename(text):
    result = ""
    n1 = numpy.random.randint(0, 10)
    n2 = numpy.random.randint(0, 10)
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
    print(string_repeat_rename("hello"))
except ValueError as e:
    print(e)