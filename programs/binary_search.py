def binary_search(x, A, i, j):
	if i>j:
		return -1
	mid = int((i+j)/2)
	if A[mid] == x:
		return mid
	elif A[mid] >x:
		return binary_search(x, A, i, mid-1)
	else:
		return binary_search(x, A, mid+1, j)
