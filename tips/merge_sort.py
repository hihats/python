from random import shuffle
import sys


def merge_sort(a_list):
    if len(a_list) <= 1:
        return a_list

    mid = len(a_list) // 2
    left = a_list[:mid]
    right = a_list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return list(merge(left, right))


def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    if left:
        sorted_list.extend(left[left_index:])
    if right:
        sorted_list.extend(right[right_index:])

    return sorted_list


if __name__ == '__main__':
    argvs = sys.argv
    if argvs is None or not isinstance(argvs, list) or len(argvs) == 0:
        l = list(range(15)) # adjust to python3
    else:
        l = argvs[1:]
    lcopy = l[:]
    shuffle(l)
    print('Unsorted')
    print(l)
    assert l != lcopy
    print('Sorted')
    l = merge_sort(l)
    print(l)
    assert l == lcopy
