def binary_search(n, numbers, start, stop):
	if start > stop:
		return f"{n} not found"
	else:
		mid = (start + stop)//2
		if n == numbers[mid]:
			return mid
		elif n > numbers[mid]:
			return binary_search(n, numbers, mid+1, stop)
		else:
			return binary_search(n, numbers, start, mid-1)
	return "Not found"