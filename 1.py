N = int(input("Size of the arrays: "))
arr1 = [int(input(f"Element number {i+1} of the first array: ")) for i in range(N)]
arr2 = [int(input(f"Element number {i+1} of the second array: ")) for i in range(N)]
for i in range(N):
    arr1[i], arr2[i] = arr2[i], arr1[i]
print(f"Array A: {arr1}, Array B: {arr2}")
