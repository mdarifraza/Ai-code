def selection(arr1):
    n = len(arr1)
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr1[j] < arr1[mini]:
                mini = j
        # Swap elements
        arr1[i], arr1[mini] = arr1[mini], arr1[i]
        print("Iteration", i+1, ":", arr1)  # Print array after each iteration


arr1 = [24, 41, 33, 42, 17]
print("Original array:", arr1)
selection(arr1)
print("Sorted array is:", arr1)
