# 「商品名を入力してください: 」と表示して、ユーザが入力した文字列をproduct_nameという変数に代入
product_name = input("商品名を入力してください: ")
# 「単価（税抜）: 」と表示して、ユーザが入力した文字列を整数にしてpriceという変数に代入
price = int(input("単価（税抜）: "))
# 「個数: 」と表示して、ユーザが入力した文字列を整数にしてcountという変数に代入
count = int(input("個数: "))
# f文字をもちいて、「あなたは、1個○○円の××を△△個購入しました」にprice、product_name、countを埋め込んで表示する
text = f"あなたは、1個{price}円の{product_name}を{count}個購入しました"
print(text)
# 税込み価格を（単価）×（個数）×1.1で計算して、totalという変数に代入。掛け算は「*」で表します。
total = price * count * 1.1
# total = int(price * count * 1.1)
text = f"税込み価格は、{total}円です。"
print(text)