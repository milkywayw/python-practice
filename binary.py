def binary_search(num_list, target):

    if not num_list:
        return False

    pivot = len(num_list) / 2
    current = num_list[pivot]

    if current == target:
        return True

    if target < current:
        return binary_search(num_list[0 : pivot] , target)

    if target > current:
        return binary_search(num_list[pivot + 1 : len(num_list)], target)
