time = int(input("今何時ですか？0～23を入力してください -> "))

if time < 12:  # 時間が12時より前なら
    print(f"午前{time}時です。")
else:  # 12時以降なら
    print(f"午後{time - 12}時です。")
