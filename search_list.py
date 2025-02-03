def search_ordered_list(lst, target):
    sorted_lst = sorted(lst)
    low = 0
    high = len(sorted_lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_lst[mid] == target:
            return True
        elif sorted_lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False 

numbers = [10, 3, 5, 7, 2, 8]
target = 5

found = search_ordered_list(numbers, target)
print(f"Is {target} in the list? {found}")