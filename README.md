# Sorting Algorithms Benchmark

A small Python project that measures, compares, and visualizes the running time of various sorting algorithms on random lists and datasets of increasing size.

# Algorithms

| Algorithm | Time Complexity (Best / Avg / Worst) | Idea / Approach |
|---|---|---|
| **Selection Sort** | O(n²) / O(n²) / O(n²) | Repeatedly picks the smallest remaining element and puts it in place |
| **Insertion Sort** | O(n) / O(n²) / O(n²) | Inserts each element into the already sorted left part |
| **Bubble Sort** | O(n) / O(n²) / O(n²) | Swaps neighbouring elements until the largest "bubbles up" to the end |
| **Merge Sort** | O(n log n) / O(n log n) / O(n log n) | Splits the list in half recursively, then merges the sorted halves |
| **Comb Sort** | O(n log n) / O(n² / 2ᵖ) / O(n²) | Improves on Bubble Sort by using a shrinking gap size to eliminate small values at the end |
| **Counting Sort** | O(n + k) / O(n + k) / O(n + k) | Non-comparison algorithm that counts occurrences of each unique value (for integers/discrete ranges) |
| **Radix Sort** | O(d * (n + k)) / O(d * (n + k)) / O(d * (n + k)) | Non-comparison algorithm that sorts numbers digit-by-digit from least to most significant |
| **Bucket Sort** | O(n + k) / O(n + k) / O(n²) | Distributes elements into buckets, sorts each bucket individually (e.g. using Insertion Sort), and concatenates them |

# How it works

1. Generates random datasets or arrays of various sizes.
2. Every algorithm sorts a copy of the exact same dataset to ensure a fair comparison.
3. Non-comparison algorithms (Counting, Radix, Bucket Sort) process suitable integer/range inputs efficiently.
4. Measurements are repeated and averaged using `time.perf_counter()`.
5. Results are printed in the console and saved as visual graphs.

# Getting Started

Requirements: Python 3 and matplotlib.

```bash
pip install -r requirements.txt
python sorting-benchmark.py

# Getting started

Requirements: Python 3 and matplotlib.

```bash
pip install -r requirements.txt
python sorting-benchmark.py
```
The script prints a table of average times and saves the chart as `sort_graph.png`.

# What I learned

- How common sorting algorithms work and why their complexity differs
- Measuring code performance fairly (copying input, repeating and averaging measurements)
- Visualizing results with matplotlib
