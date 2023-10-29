# append_func_02.py
def append_twice_bad(a_list, val):
	a_list = a_list + [val, val]

nums = [1, 2, 3]
append_twice_bad(nums, 7)
print(nums)
