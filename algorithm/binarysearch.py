import types


def search_list_num_index(nums, number):
    min_index = 0
    max_index = len(nums) - 1

    while max_index >= min_index:
        mid = int((min_index + max_index) / 2)
        guess = nums[mid]

        if guess == number:
            return mid

        if guess > number:
            max_index = mid - 1
        elif guess < number:
            min_index = mid + 1

    return None


# index = search_list_num_index([1, 2, 4, 6, 7, 10], 2)
# print(index)


def sum_numbers(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums.pop() + sum_numbers(nums)


def element_number(lists):
    if len(lists) == 0:
        return 0
    else:
        lists.pop()
        return 1 + element_number(lists)


def max_num(lists):
    if len(lists) == 1:
        return lists[0]
    else:
        num1 = lists[0]
        num2 = lists[1]
        if num1 > num2:
            lists.pop(1)
            return max_num(lists)
        else:
            lists.pop(0)
            return max_num(lists)


num = max_num([10, 8, 7, 2, 3, 11])
print(hasattr(num, "x"))
print(num)
