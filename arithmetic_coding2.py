def find_char_id(char):
  chars = "abcd"
  for i in range(len(chars)):
    if char == chars[i]:
      return i
    
def str2num(query, a=0.5, b=0.3, c=0.15, d=0.05):
  front = [0, a, a+b, a+b+c]
  back = [a, a+b, a+b+c, a+b+c+d]
  line_width = [a, b, c, d]
  
  value = front[find_char_id(query[0])]
  width = back[find_char_id(query[0])]
  
  for i in range(1, len(query)):
    id = find_char_id(query[i])
    value = value + (width * front[id])
    width = width * line_width[id]
    
  return value

def num2str(number, a=0.5, b=0.3, c=0.15, d=0.05):
  front = [0, a, a+b, a+b+c]
  back = [a, a+b, a+b+c, a+b+c+d]
  line_width = [a, b, c, d]
  
  ans = ""
  chars = "abcd"
  
  while number> 0.:
    for i in range(len(chars)):
      if front[i] <= number < back[i]:
        ans += chars[i]
        number = (number - front[i]) / line_width[i]
        
  return ans

if __name__ == '__main__':
  print("====================")
  query = input("文字列を入力: ")
  ans_num = str2num(query)
  print(f"出力: {ans_num}")
  print("====================")
  num = float(input("算術符号を入力: "))
  print(f"出力: {num2str(num)}")
  print("====================")
  