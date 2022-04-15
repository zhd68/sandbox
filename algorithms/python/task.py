def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])


def count_item(arr):
    if arr == []:
        return 0
    return 1 + count_item(arr[1:])


def search_greatest(arr):
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[1]
        else:
            return arr[0]
    sub_max = max(arr[1:])
    if arr[0] < sub_max:
        return sub_max
    else:
        return arr[0]
    
def binary_search(arr, item) -> bool:
    if arr == []:
        raise Exception(f'Ooops! List is empty')

    if arr[0] < arr[-1]:
        route = 1
    else:
        route = -1

    low, high = 0, len(arr)
    mid = (low + high) // 2

    if len(arr) == 1:
        return True if arr[0] == item else False
    elif arr[mid] > item:
        return binary_search(arr[:mid:route], item)
    elif arr[mid] < item:
        return binary_search(arr[mid::route], item)


def main():
    arr = [1, 2, 3, 4, 5, 6]
    arr1 = [6, 5, 4, 3, 2, 1]
    arr2 = []
    print(sum(arr))
    print(count_item(arr))
    print(search_greatest(arr))
    print(binary_search(arr, 10))
    print(binary_search(arr1, 1))
    print(binary_search(arr1, 7))


if __name__ == '__main__':
    main()
