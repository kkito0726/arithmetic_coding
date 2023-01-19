# 文字列のIDを返すメソッド
def find_char_id(char)
    chars = "abcd"
    for i in 0..chars.length do
        if char == chars[i]
            return i
        end
    end
end

# 文字列を算術符号化するメソッド
def str2num(query, a, b, c, d)
    front = [0, a, a+b, a+b+c]
    back = [a, a+b, a+b+c, a+b+c+d]
    line_width = [a, b, c, d]
    
    value = front[find_char_id(query[0])]
    width = back[find_char_id(query[0])]
   
    for i in 1..query.length-1 do
        id = find_char_id(query[i])
        value = value + (width * front[id])
        width = width * line_width[id]
    end

    return value
end

# 算術符号を文字列にデコードするメソッド
def num2str(number, a, b, c, d)
    front = [0, a, a+b, a+b+c]
    back = [a, a+b, a+b+c, a+b+c+d]
    line_width = [a, b, c, d]

    ans = ""
    chars = "abcd"
    while number > 0
        for i in 0..3 do
            if front[i] <= number && number < back[i]
                ans += chars[i]
                number = (number - front[i]) / line_width[i]
            end
        end
    end
    return ans
end

def main()
    puts "========================"
    print "文字列を入力: "
    query = gets.chomp  # デフォルトで改行コードが入る仕様のため、chompメソッドで削除する
    ans_num = str2num(query, 0.5, 0.3, 0.15, 0.05)
    puts "出力: #{ans_num}"
    puts "========================"

    print "算術符号を入力: "
    number = gets.to_f
    ans = num2str(number, 0.5, 0.3, 0.15, 0.05)
    puts "出力: #{ans}"
    puts "========================"

end

main()