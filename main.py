def count_elements_with_greater(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        has_greater = False
        for j in range(n):
            if i != j and arr[j] > arr[i]:
                has_greater = True
                break
        if has_greater:
            count += 1
    return count
A = [3, 1, 2]
result = count_elements_with_greater(A)
print("Number of elements with at least one greater element:", result)
A = [5, 5, 3]
result = count_elements_with_greater(A)
print("Number of elements with at least one greater element:", result)
