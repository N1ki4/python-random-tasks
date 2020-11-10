arr1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]
arr2 = [2, 5, 1, 3, 4]
ch = "geeksforgeeks"


def first(arr):
	res = {}
	for i in arr:
		if i in res:
			print(res)
			return f"{i} Is first recurring char in collection"
		else:
			res[i] = 0


print(first(arr1))
