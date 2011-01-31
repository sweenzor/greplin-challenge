from itertools import combinations

numbers = [3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 73, 78, 81, 92, 95, 97, 99]

def valid_subset(list_nums):
	list_nums.sort()
	if sum(list_nums[:-1]) == list_nums[-1]:
		return True
	return False


count = 0
for size in range(2,len(numbers)):
	for subset in combinations(numbers,size):
		if valid_subset(list(subset)):
			print subset
			count = count + 1

print 'count= ',count
