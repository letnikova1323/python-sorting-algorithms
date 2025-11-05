# 1.
def selection_sort_asc(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 2.
def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

# 3. 
def selection_sort_phones(phones):
    n = len(phones)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            # Сравниваем числовые значения без дефисов
            if int(phones[j].replace('-', '')) < int(phones[min_idx].replace('-', '')):
                min_idx = j
        phones[i], phones[min_idx] = phones[min_idx], phones[i]


