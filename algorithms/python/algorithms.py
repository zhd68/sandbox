import random

def _binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    step = 0

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        step += 1
        if guess == item:
            return True, step
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return False, step


def _selection_sort(arr: list) -> list:

    def _search_smallest(arr: list) -> int:
        smallest_idx = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[smallest_idx]:
                smallest_idx = i
        return smallest_idx

    arr = arr.copy()
    new_arr = []
    for _ in range(len(arr)):
        smallest_idx = _search_smallest(arr)
        new_arr.append(arr.pop(smallest_idx))
    return new_arr


def _quick_sort(arr: list) -> list:
    arr = arr.copy()
    if len(arr) < 2:
        return arr

    pivot_idx = random.randint(0, len(arr)-1)
    left, ridht = 0, len(arr)-1

    arr[pivot_idx], arr[ridht] = arr[ridht], arr[pivot_idx]

    for i in range(len(arr)):
        if arr[i] < arr[ridht]:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1

    arr[left], arr[ridht] = arr[ridht], arr[left]

    return _quick_sort(arr[:left]) + [arr[left]] + _quick_sort(arr[left+1:])


def main():
    print('Binary search/бинарный поиск:')
    my_list_int = [i for i in range(1, 101)]
    my_list_str = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    print(_binary_search(my_list_int, 50))
    print(_binary_search(my_list_str, 'c'))

    print('Selection sort/сортировка выбором:')
    my_list = [1, 5, 7, 2, 2, 5, 90, 10]
    print(_selection_sort(my_list))
    
    #my_list = [1, 5, 7, 2, 2, 5, 90, 10]
    new_list = [random.randint(0, 20) for i in range(100)]
    print(new_list)
    print('Quick sort/быстрая сортировка')
    print(_quick_sort(new_list))


if __name__ == '__main__':
    main()
