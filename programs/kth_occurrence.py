def kth_occurrence(x, k, A, i, j):
	cnt = 0
	for index in range(i, j+1):
		if A[index] == x:
			cnt += 1
		if cnt == k:
			return index
	return -1

if __name__ == '__main__':
	A = [1,2,5,2,5,6,2,4]
	k = 1
	print(kth_occurrence(4, k, A, 0, len(A)-1))
