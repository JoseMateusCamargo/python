def bst(array, val, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    if begin <= end:
        m = (begin + end) // 2  # extração da parte inteira da divisão

        if array[m] == val:
            return m

        return bst(array, val, begin, m - 1) if val < array[m] else bst(array, val, m + 1, end)

    return None


list_array = [2, 3, 4, 4, 4, -4, 5, 66, 8, 2, 33]
print(f'Initial array: {list_array}')

list_array.sort()
print(f'Ordered array: {list_array}')

value = 4
print(f'Value {value} in index: {bst(list_array, value)}')
