def bubble_sort(arr):
	n = len(arr)
	for i in range(0,n-1):
		for j in range(0,n-1-i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr


def selection_sort(arr):
	n = len(arr)
	for i in range(n-1):
		min_index = i
		for j in range(i+1,n):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[min_index], arr[i] = arr[i], arr[min_index]
	return arr


def insertion_sort(arr):
	n = len(arr)
	for i in range(1,n):
		pre_index = i-1
		current = arr[i]
		while pre_index >= 0 and arr[pre_index] > current:
			arr[pre_index+1] = arr[pre_index]
			pre_index -= 1
		arr[pre_index+1] = current
	return arr

# merge sort
def merge_sort(arr):
	# 递归将arr分成两个一组
	n = len(arr)
	if n <= 1: return arr
	mid = n // 2
	left = arr[0:mid]
	right = arr[mid:]
	return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
	l, r, left_len, right_len = 0, 0, len(left), len(right)

	result = []
	while l < left_len and r < right_len:
		if left[l] < right[r]:
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1
	while l < left_len:
		result.append(left[l])
		l += 1
	while r < right_len:
		result.append(right[r])
		r += 1
	return result


# quick sort
def quick_sort(arr, low, high):
	if len(arr) == 1: return arr
	# partition--sorting
	if low < high:
		pivot_index = partition(arr, low, high)

		# recursion for each partition
		quick_sort(arr, low, pivot_index-1)
		quick_sort(arr, pivot_index+1, high)
	return arr

def partition(arr, low, high):
	# pointer to swap with pivot
	i = low-1
	# pivot
	pivot_value = arr[high]
	for j in range(low, high):
		if arr[j] < pivot_value:
			i += 1
			arr[i], arr[j] = arr[j] , arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1
print(quick_sort([43,2,2,3,4,5,1,1,3], 0, 8)) 








