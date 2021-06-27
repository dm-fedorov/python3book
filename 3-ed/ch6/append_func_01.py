# append_func_01.py
def append_twice(a_list, val):
	a_list.append(val)
	a_list.append(val)

nums = [1, 2, 3]
append_twice(nums, 7)
print(nums)
