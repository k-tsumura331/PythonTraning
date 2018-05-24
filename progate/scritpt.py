# Lesson1 リンゴの購入
apple_price = 200
money = 1000
input_count = input("購入するりんごの個数を入力してください：")
count = int(input_count)
total_price = apple_price * count

print("購入するりんごの個数は" + str(count) + "個です")
print("支払金額は" + str(total_price) + "円です")

if money > total_price:
    print("りんごを" + str(count) + "個買いました")
    print("残金は" + str(money - total_price) + "円です")
elif money == total_price:
    print("りんごを" + str(count) + "個買いました")
    print("財布が空になりました")
else:
    print("お金が足りません")
    print("りんごを買えませんでした")


# Lesson2 「Hello World」と出力してください
print("HelloWorld")

# Lesson3 数値の出力
# 数値の7を出力してください
print(7)

# 9に3足した値を出力してください
print(9 + 3)

# 「9 + 3」を文字列として出力してください
print("9 + 3")

# Lesson4 数値の計算
# 9を2で割った値を出力してください
print(9 / 2)

# 7に5を掛けた値を出力してください
print(7 * 5)

# 5を2で割った時の余りを出力してください
print(5 % 2)

# Lesson5 変数
# 変数nameに文字列「にんじゃわんこ」を代入してください
name= "にんじゃわんこ"

# 変数nameの値を出力してください
print(name)

# 変数numberに数値の7を代入してください
number=7

# 変数numberの値を出力してください
print(number)

# Lesson6 変数名
# 良い例    date 英単語を用いる
#           user_name 2語以上の場合はアンダーバーで区切る
apple_count = 3     # リンゴの個数
apple_price = 100   # リンゴの値段
total_price = apple_count * apple_price
print(total_price)

# 正方形の面積を計算
length = 5
area = length * length
print(area)

apple_price = 200
apple_count = 8

# apple_priceとapple_countを掛けた結果を、変数total_priceに代入してください
total_price = apple_price * apple_count

# total_priceの値を出力してください
print(total_price)

# Lesson7 変数の値を更新する
# 変数xを定義
x = 5
print(x)
x = 11
print(x) # 11
x = 5
print(x)
x = x + 3
print(x) # 8
# x = x + 10
x += 10
# x = x - 10
x -= 10
# x = x * 10
x *= 10
# x = x/ 10
x /= 10
# x = x % 10
x %= 10

money = 2000
print(money)

# 変数moneyに5000を足して、変数moneyを上書きしてください
money += 5000

# 変数moneyの値を出力してください
print(5000)

money = 2000
print(money)

# 変数moneyに5000を足して、変数moneyを上書きしてください
money += 5000

# 変数moneyの値を出力してください
print(money)

# Lesson8 文字列の連結
"""
docstringの使い方を説明するためのモジュール
"""
# my_nameという変数に「にんじゃわんこ」という文字列を代入してください
my_name = "にんじゃわんこ"

# my_nameを用いて、「私はにんじゃわんこです」となるように変数と文字列を連結して出力してください
print("私は" + my_name + "です")

# Lesson９ データ型
"Hello　Python" # 文字列型
3               # 数値型
#型変換 str int
price = 100
#print("リンゴの価格は" + price + "円です") # Error
print("リンゴの価格は" + str(price) + "円です")

count = "3"
price = 100
total_price = price * int(count)
print(total_price)
age = 24
# ageを用いて「私は24歳です」と出力してください
print("私は" + str(age) + "歳です")


count = "5"
# countに1を足した値を出力してください
print(int(count) + 1)

# Lesson9 条件分岐
score = 100
if score == 100:    # 条件式が成り立つ場合
    print("よくできました")

# x == y 左右の値が等しい場合に成り立つ
# x != y 左右の値が等しく無い時成り立つ
score = 50
if score == 50 :
    print("よくできました！")
    print("次もがんばりましょう！") # インデントが無いため、if分の外とみなされる

x = 7 * 10
y = 5 * 6

# xが70と等しい場合に「xは70です」と出力してください
if x == 70 :
    print('xは70です')


# yが40と等しくない場合に「yは40ではありません」と出力してください
if y != 40 :
    print("yは40ではありません")

# Lesson10 真偽値
score = 100
if score == 100:
    print("よくできました！")
print(score == 100)

print