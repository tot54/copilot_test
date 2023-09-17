# フィボナッチ数列を生成する関数
# q: オーダーは？
# a: O(n)
def fib(n):
	a, b = 0, 1
	while b < n:
		print(b, end=' ')
		# a, b = b, a+b
		c = a + b
		a = b
		b = c
	print()
 
# フィボナッチ数列を生成し、出力する関数
# 引数に数列の要素数を指定する
# 再帰関数
# q: オーダーは？
# a: O(2^n)
def fib2(n):
	if n < 2:
		return n
	return fib2(n-1) + fib2(n-2)


def DifferenceBetweenTwoDates(date1, date2):
	from datetime import datetime
	date1 = datetime.strptime(date1, '%Y/%m/%d').date()
	date2 = datetime.strptime(date2, '%Y/%m/%d').date()
	return abs((date2 - date1).days)

 
# DifferenceBetweenTwodates関数のテストコード
###
# 下記にテストするべき項目をリストアップする
# 1. 同じ日付の場合
# 2. 1日違いの場合
# 3. 月が違う場合
# 4. 年が違う場合
# 5. うるう年の場合
# 6. うるう年ではない場合
# 7. うるう年の2月29日からうるう年ではない2月28日の場合
# 8. うるう年ではない2月28日からうるう年の2月29日の場合
# 9. 日付ではない場合
###
def test_DifferenceBetweenTwoDates():
	assert DifferenceBetweenTwoDates('2019/01/01', '2019/01/01') == 0
	assert DifferenceBetweenTwoDates('2019/01/01', '2019/01/02') == 1
	assert DifferenceBetweenTwoDates('2019/01/01', '2019/02/01') == 31
	assert DifferenceBetweenTwoDates('2019/01/01', '2020/01/01') == 365
	assert DifferenceBetweenTwoDates('2020/01/01', '2021/01/01') == 366
	assert DifferenceBetweenTwoDates('2019/02/28', '2019/03/01') == 1
	assert DifferenceBetweenTwoDates('2019/03/01', '2019/02/28') == 1
	assert DifferenceBetweenTwoDates('2019/01/01', '2019/01/32') == -1
	assert DifferenceBetweenTwoDates('2019/01/01', '2019/13/01') == -1
	assert DifferenceBetweenTwoDates('2019/01/01', '2019/00/01') == -1
	assert DifferenceBetweenTwoDates('2019/01/01', '2019/01/00') == -1
	assert DifferenceBetweenTwoDates('2019/01/01', '2019/01/01/00') == -1
	assert DifferenceBetweenTwoDates('2019/01/01', '2019/01/01/01') == -1
test_DifferenceBetweenTwoDates()