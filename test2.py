# 関数のdoxygen作成
##
# @fn DifferenceBetweenTwoDates(date1, date2)
# @brief 2つの日付の差を求める関数
# @param date1 日付1
# @param date2 日付2
# @return 2つの日付の差
# @exception ValueError 日付ではない場合"ValueError"を返す
def DifferenceBetweenTwoDates(date1, date2):
	from datetime import datetime
	date1 = datetime.strptime(date1, '%Y/%m/%d').date()
	date2 = datetime.strptime(date2, '%Y/%m/%d').date()
	return abs((date2 - date1).days)


# 関数のdoxygen作成
##
# @fn random_select(array, n)
# @brief 配列からランダムにn個の要素を選択する関数
# @param array 配列
# @param n 選択する要素数
# @return 選択された要素の配列を返す。選択する要素数が0以下の場合は空の配列を返す
# @exception ValueError 選択する要素数が配列の要素数より多い場合"ValueError"を返す
def random_select(array, n):
	import random
	if n > len(array):
		raise ValueError
	if n <= 0:
		return []
	return random.sample(array, n)

# 関数のdoxygen作成
##
# @fn test_random_select()
# @brief random_select関数のテストコード
# @exception AssertionError テストが失敗した場合"AssertionError"を返す
# @detail テスト結果の比較は返却された配列の要素数を比較する.
def test_random_select():
	assert len(random_select([1, 2, 3, 4, 5], 3)) == 3
	assert len(random_select([1, 2, 3, 4, 5], 0)) == 0
	assert len(random_select([1, 2, 3, 4, 5], 5)) == 5
	assert len(random_select([1, 2, 3, 4, 5], 6)) == 5
	assert len(random_select([1, 2, 3, 4, 5], -1)) == 0
test_random_select()

# 関数のdoxygen作成
##
# @fn test_random_select()
# @brief random_select関数のテストコード
# @exception AssertionError テストが失敗した場合"AssertionError"を返す
# @detail テスト結果の比較は返却された配列の要素数を比較する。ただし、ValueErrorを返す場合は例外として扱う
def test_random_select():
	assert random_select([1, 2, 3], 2) == [1, 2]
	assert random_select([1, 2, 3], 0) == []
	assert random_select([1, 2, 3], -1) == []
	try:
		random_select([1, 2, 3], 4)
	except ValueError:
		pass
	else:
		raise AssertionError