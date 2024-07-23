time = int(input("今何時ですか？0～23を入力してください -> "))

if time < 12: # 12時より前
    print(f"午前{time}時です。")
elif time == 12: # それ以外で、12時のケース
    print("正午です。")
else: # それ以外
    print(f"午後{time - 12}時です。")