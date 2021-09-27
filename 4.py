N = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(N)]
min_value = min(arr)
max_value = max(arr)
min_index = arr.index(min_value)
max_index = arr.index(max_value)
later = max_index if max_index > min_index else min_index
earlier = max_index if max_index < min_index else min_index
for i in range(earlier+1, later):
    arr[i] = 0
print(f"An array after zeroing out all elements between the minimum and the maximum: {arr}")
