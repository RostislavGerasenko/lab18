N = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(N)]
arr_out = [sum(arr[:i+1])/(i+1) for i in range(N)]
print(f"Array of arithmetical means: {arr_out}")
