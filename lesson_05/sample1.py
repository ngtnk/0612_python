# ユーザに残高を入力させて、moneyという変数に代入
money = int(input("電子マネー残高を入力してください -> "))
# 「もしmoneyが1000未満だったら」
# 「5000円チャージする」
if money < 1000:
    money += 5000
    print("自動で5000円チャージしました。")
# 電子マネー残高を表示
print(f"電子マネー残高: {money:,}円")