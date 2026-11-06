import random
import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

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

def counting_sort(ratings):
    max_val = max(ratings) if ratings else 0
    count = [0] * (max_val + 1)                  

    for r in ratings:               
        count[r] += 1

    result = []
    for rating in range(len(count)):         
        result.extend([rating] * count[rating])
    return result

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
    if not arr:
        return arr
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        arr = counting_by_digit(arr, exp)
        exp *= 10
    return arr

def bucket_insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

def bucket_sort(scores):
    if not scores:
        return scores
    max_val = max(scores)
    num_buckets = 5
    buckets = [[] for _ in range(num_buckets)]  

    for s in scores:
        # Dinamik bucket aralığı
        index = min(int(s / (max_val + 1) * num_buckets), num_buckets - 1)
        buckets[index].append(s)

    result = []
    for b in buckets:
        result.extend(bucket_insertion_sort(b))  
    return result


algorithms = {
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Bubble Sort": bubble_sort,
    "Merge Sort": merge_sort,
    "Comb Sort": comb_sort,
    "Counting Sort": counting_sort,
    "Radix Sort": radix_sort,
    "Bucket Sort": bucket_sort,
}

sizes = [100, 250, 500, 1000, 1500, 2000]  
repeats = 3                             


def measure(func, data):
    start = time.perf_counter()
    func(data.copy())  
    return time.perf_counter() - start

def run_benchmark():
    results = {name: [] for name in algorithms}

    for size in sizes:
        data = [random.randint(0, 1000) for _ in range(size)]

        for name in algorithms:
            func = algorithms[name]
            total = 0
            for _ in range(repeats):
                total += measure(func, data)

            average = total / repeats
            results[name].append(average)

        print("n =", size, "completed")

    return results

def print_table(results):
    print("\nAverage times (seconds):")
    print("n", end="\t")
    for name in algorithms:
        print(name, end="\t")
    print()                         

    for i in range(len(sizes)):
        print(sizes[i], end="\t")
        for name in algorithms:
            sure = results[name][i]
            print(f"{sure:.5f}", end="\t")
        print()

def plot_results(results, filename="sort_graph.png"):
    plt.figure(figsize=(10, 6))
    for name in algorithms:
        plt.plot(sizes, results[name], marker="o", label=name)

    plt.title("Speed Comparison of Sorting Algorithms (Including Exercise 5)")
    plt.xlabel("List size (n)")
    plt.ylabel("Time (second)")
    plt.legend()                    

    plt.savefig(filename) 
    plt.show()      
    print("Chart saved:", filename)


if __name__ == "__main__":
    results = run_benchmark()
    print_table(results)
    plot_results(results)
