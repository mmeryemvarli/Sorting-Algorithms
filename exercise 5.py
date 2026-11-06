def comb_sort(weights):
    arr = weights[:]            
    n = len(arr)
    gap = n                     
    swapped = True

    while gap != 1 or swapped:
        gap = max(1, int(gap / 1.3))   
        swapped = False

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:  
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr

print(comb_sort([8.5, 2.1, 9.7, 1.3, 5.5, 3.2]))

def counting_sort(ratings):
    count = [0] * 6                  

    for r in ratings:               
        count[r] += 1

    result = []
    for rating in range(6):         
        result.extend([rating] * count[rating])
    return result

print(counting_sort([5, 3, 0, 4, 5, 1, 3, 2, 5, 0]))

def counting_by_digit(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10

    for num in arr:
        digit = (num // exp) % 10    
        count[digit] += 1

    for i in range(1, 10):          
        count[i] += count[i - 1]

    for num in reversed(arr):       
        digit = (num // exp) % 10
        count[digit] -= 1
        output[count[digit]] = num
    return output

def radix_sort(ids):
    arr = ids[:]
    for exp in (1, 10, 100):         
        arr = counting_by_digit(arr, exp)
    return arr

print(radix_sort([329, 457, 657, 839, 436, 720, 355]))


def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

def bucket_sort(scores):
    buckets = [[] for _ in range(5)]  

    for s in scores:
        index = min(s // 20, 4)        
        buckets[index].append(s)

    result = []
    for b in buckets:
        result.extend(insertion_sort(b))  
    return result

print(bucket_sort([95, 12, 67, 45, 88, 33, 100, 59, 20, 0, 79]))
