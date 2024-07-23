temperature = float(input("体温を入力: "))
# int関数は文字列を"整数"に変換
# float関数は文字列を"小数"に変換
if temperature < 36.5:
    print("低体温")
elif temperature < 37.5: # 36.5度～37.499999度
# elif 36.5 <= temperature < 37.5:
    print("平熱")
else: # 37.5度以上
    print("発熱")