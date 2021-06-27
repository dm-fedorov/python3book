# append_func_03.py
def append_twice_good(a_list, val):
	a_list = a_list + [val, val]
	return a_list

nums = [1, 2, 3]
nums = append_twice_bad(nums, 7)
print(nums)
