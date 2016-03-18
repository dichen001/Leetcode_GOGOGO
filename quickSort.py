# 03/18/2016 after failed in interviewing for Alibaba.
def quikSort(nums, low = 0, high = None):
	if high == None:
		high = len(nums)-1
	if low<high:
		mid = partition(nums,low,high)
		quikSort(nums, low, mid-1)
		quikSort(nums, mid, high)

def partition(nums,low,high):
	piv = nums[high]
	for i in range(low,high):
		if nums[i] < piv:
			nums[low], nums[i] = nums[i], nums[low]
			low = low + 1
	nums[low],nums[high] = nums[high],nums[low]
	return low


a = [12,4,5,6,7,3,1,15]
print quikSort(a)
print a

