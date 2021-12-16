import bisect

N = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(N)]
first_value = arr.pop(0)
bisect.insort_left(arr, first_value)
print(f"Sorted array: {arr}")
