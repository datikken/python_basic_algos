#The main advantage of the selection sort is that it performs well on a small list.
def selection_sort(a):
	for j in range(len(a)-1):
		minimum = j
		for i in range(j+1, len(a)):
			if(a[i] < a[minimum]):
				minimum = i
		a[j], a[minimum] = a[minimum], a[j]