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







