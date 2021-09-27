N = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(N)]
min_value = min(arr)
arr.remove(min_value)
arr.insert(0, min_value)
print(f"Sorted array: {arr}")
