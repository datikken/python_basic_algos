def binary_search(numbers, n):
	low = 0
	high = len(numbers)-1
	while low <= high:
		middle = (low + high) // 2
		if n == numbers[middle]:
			return middle
		elif n > numbers[middle]:
			low = middle + 1
		else:
			high = middle - 1
	return "Not found"