month = int(input("月を入力: "))

# 1～12以外の値が入力された場合は「無効な月です。1～12の範囲で入力してください。」と表示してください。
if month <= 0:
    print("無効な月です。1～12の範囲で入力してください。")
# 1-3 -> 冬
elif month <= 3:
    print("冬です。")
# 4-6 -> 春
elif month <= 6:
    print("春です。")
# 7-9 -> 夏
elif month <= 9:
    print("夏です。")
# 10-12 -> 秋
elif month <= 12:
    print("秋です。")
else: 
    print("無効な月です。1～12の範囲で入力してください。")