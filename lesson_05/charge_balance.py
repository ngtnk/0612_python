# - 変数 `balance` に `input` 関数を使用してユーザーに電子マネー残高を入力してもらい、`int` 関数で整数に変換してください。
balance = int(input("残高を入力: "))
# - 変数 `charge_amount` に `input` 関数を使用してユーザーに希望するチャージ額を入力してもらい、`int` 関数で整数に変換してください。
charge_amount = int(input("チャージ額を入力: "))
# - if文を使用して、残高が希望するチャージ額未満の場合に、自動でその額をチャージしてください。
if balance < charge_amount:
    balance += charge_amount
    # - チャージした場合は、チャージ額を含むメッセージを表示してください。
# - 最終的な残高を表示してください。
print(f"残高は{balance}です。")