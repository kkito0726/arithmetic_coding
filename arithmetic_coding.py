# -*- coding: utf-8 -*-

# 文字列から算術符号を計算
def str2int(query, a=0.5, b=0.3, c=0.15, d=0.05):
    # 各範囲の開始と終わりと幅を辞書で格納する
    front = {
        "a": 0,
        "b": a,
        "c": a+b,
        "d": a+b+c
    }
    back = {
        "a": a,
        "b": a+b,
        "c": a+b+c,
        "d": a+b+c+d
    }
    line_width = {
        "a": a,
        "b": back["b"]-a,
        "c": back["c"]-back["b"],
        "d": back["d"]-back["c"]
    }
    
    value, width = 0, 0
    for i, q in enumerate(query):
        if i == 0:
            value, width = front[q], back[q]
        else:
            value = value + (width * front[q])
            width = width * line_width[q]
    
    return round(value, 2)

# 算術符号から文字列をデコード
def int2str(number, a=0.5, b=0.3, c=0.15, d=0.05):
    # 各範囲の開始と終わりと幅を辞書で格納する
    front = {
        "a": 0,
        "b": a,
        "c": a+b,
        "d": a+b+c
    }
    back = {
        "a": a,
        "b": a+b,
        "c": a+b+c,
        "d": a+b+c+d
    }
    line_width = {
        "a": a,
        "b": back["b"]-a,
        "c": back["c"]-back["b"],
        "d": back["d"]-back["c"]
    }
        
    ans = ""
    while number > 0.:
        if front["a"] <= number < back["a"]:
            ans += "a"
            number = round((number - front["a"]) / line_width["a"], 2)
            
        if front["b"] <= number < back["b"]:
            ans += "b"
            number = round((number - front["b"]) / line_width["b"], 2)
        
        if front["c"] <= number < back["c"]:
            ans += "c"
            number = round((number - front["c"]) / line_width["c"], 2)
        
        if front["d"] <= number < back["d"]:
            ans += "d"
            number = round((number - front["d"]) / line_width["d"], 2)
            
    
    return ans

if __name__ == '__main__':
    print("===============")
    S = input("文字列を入力: ")
    # print("文字列 => 算術符号")
    print(f"出力: {str2int(S)}")
    
    print("===============")
    N = float(input("算術符号を入力: "))
    # print("算術符号 => 文字列")
    print(f"出力: {int2str(N)}")
    print("===============")