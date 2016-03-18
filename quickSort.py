# 03/18/2016 after failed in interviewing for Alibaba.

def quicksort(nums,low,high):
	if low < high:					# ***
		mid = divide(nums,low,high)
		quicksort(nums,low,mid-1)
		quicksort(nums,mid+1,high)
"""
Consider this situations [3,1]   [1,3]    [7,1,7]  [7,9,7]
"""
def divide(nums,low,high):
	pivot = nums[high]
	right = high -1 				 # *** 
	left = low
	done = 0
	while not done:
		while nums[left]<pivot:
			left = left + 1
		while nums[right]>pivot:
			right = right -1
		if left >= right:			# ***  >=
			done = 1
		else:
			nums[left],nums[right] = nums[right],nums[left]
	nums[left],nums[high] = nums[high],nums[left]				# ***
	return left


	# def quickSort1(nums, low = 0, high = None):
# 	if high == None:
# 		high = len(nums)-1
# 	if low<high:
# 		mid = partition1(nums,low,high)
# 		quickSort1(nums, low, mid-1)
# 		quickSort1(nums, mid, high)

# def partition1(nums,low,high):
# 	piv = nums[high]
# 	for i in range(low,high):
# 		if nums[i] <= piv:
# 			nums[low], nums[i] = nums[i], nums[low]
# 			low = low + 1
# 	nums[low],nums[high] = nums[high],nums[low]
# 	return low

# def quickSort2(nums,l,h):
# 	if(l<h):
# 		m = partition2(nums,l,h)
# 		quickSort2(nums,l,m-1)
# 		quickSort2(nums,m+1,h)

# def partition2(nums,l,h):
# 	piv = nums[h]
# 	# while nums[l] <= piv:
# 	while l<h:
# 		while nums[h] > piv and l<h:
# 			h = h - 1
# 		while nums[l] < piv and l<h:
# 			l = l + 1
# 		if l < h:
# 			nums[l],nums[h] = nums[h],nums[l]
# 	return h


