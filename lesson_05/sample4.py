required_unit = int(input("取得している必修単位数 -> "))
total_unit = int(input("取得している合計単位数 -> "))
# 必修が40、合計が128以上
if required_unit >= 40 and total_unit >= 128:
    print("卒業")
elif required_unit < 40 and total_unit >= 128:
    print("必修足りません")
# elif required_unit >= 40 and total_unit < 128:
elif required_unit >= 40: # すでに合計足りない人しかいないから
    print("合計足りません")
else:
    print("何も足りていません")