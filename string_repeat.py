import re
import numpy

def string_repeat_rename(text, num_row, num_column):
    """文字列を繰り返す

    Args:
        text (str): 表示する文字列
        num_row (int): 繰り返す行の数
        num_column (int): 繰り返す列の数

    Raises:
        ValueError: 長さをチェックするエラー
        ValueError: アルファベットをチェックするエラー

    Returns:
        str: 繰り返した文字列
    """
    # NOTE:エラー処理
    if not (5 <= len(text) <= 10):
        # TODO:5や10の定数化
        raise ValueError("error! : 正しい長さの文字列を入力してください")
    if not (re.fullmatch(r"[a-zA-Z]+", text)):
        raise ValueError("error! : アルファベットのみを使用してください")

    # 変数定義
    result = ""
    
    # メイン繰り返し処理
    result = (text + " ") * num_row
    result = (result + "\n") * num_column
    # TODO:改行コードの仕様要確認

    return result

# 関数実行
try:
    text = "hello"
    num_row = numpy.random.randint(0, 10)
    num_column = numpy.random.randint(0, 10)

    print(string_repeat_rename(text, num_row, num_column))
except ValueError as e:
    print(e)