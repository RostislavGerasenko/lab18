N = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(N)]
last_odd = None
for item in reversed(arr):
    if item%2 == 1:
        last_odd = item
        break
if last_odd is not None:
    arr = [item + last_odd if item %2 == 1 else item for item in arr]
print (f"The array after all odd elements are incremented by the value of the last odd element: {arr}")
