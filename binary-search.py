def binary_search(arr: list, x: int) -> int:
    high = len(arr) - 1
    low = 0
    while not high == low:
        mid = (low + high) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
            
# def binary_search_ranges(prefixSum: list, x: int) -> int:
    # [0, 4, 8, 12]
    # x = 6