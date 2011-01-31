numbers = [3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 73, 78, 81, 92, 95, 97, 99]

def valid_subset(list_nums):
	list_nums.sort()
	if sum(list_nums[:-1]) == list_nums[-1]:
		return True
	return False


for index,n in enumerate(numbers):
	for size in range(index+1,len(numbers)):
		print numbers[index:size]