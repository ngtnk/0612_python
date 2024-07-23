score = int(input("点数: "))
while (score > 100) or (score < 0):
    print("ちゃんとにゅうりょくしてーや")
    score = int(input("点数: "))

print(f"点数は{score}点です")