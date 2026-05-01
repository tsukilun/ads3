# Assignment 3: Sorting and Searching Algorithm Analysis

## Project Overview

This project compares sorting and searching algorithms using Python. The original assignment asks for Java, but this version uses Python with the same class idea:

- `Sorter` handles sorting.
- `Searcher` handles searching.
- `Experiment` runs tests and measures time.

Selected algorithms:

- Basic sorting: Selection Sort
- Advanced sorting: Merge Sort
- Searching: Binary Search

The purpose of the experiment is to see how algorithm speed changes with different input sizes and different input types.

## Algorithm Descriptions

### Selection Sort

Selection Sort finds the smallest element in the unsorted part of the array and puts it in the correct position.

Time complexity:

- Best case: O(n^2)
- Average case: O(n^2)
- Worst case: O(n^2)

Selection Sort is simple, but it becomes slow when the array gets large because it uses nested loops.

### Merge Sort

Merge Sort divides the array into two halves, sorts each half, and then merges the sorted halves back together.

Time complexity:

- Best case: O(n log n)
- Average case: O(n log n)
- Worst case: O(n log n)

Merge Sort is faster for large arrays because it divides the problem into smaller parts.

### Binary Search

Binary Search checks the middle element of a sorted array. If the target is smaller, it searches the left half. If the target is larger, it searches the right half.

Time complexity:

- Best case: O(1)
- Average case: O(log n)
- Worst case: O(log n)

Binary Search requires a sorted array because it removes half of the search area after every comparison.

Compared with Linear Search, Binary Search is more efficient for large sorted arrays. Linear Search checks elements one by one, so its average and worst case complexity is O(n). Binary Search has O(log n) complexity, so it needs fewer comparisons when the array size grows. The disadvantage is that Binary Search only works correctly when the array is sorted.

## Experimental Results

The program uses `perf_counter_ns()` in Python. It is similar to Java's `System.nanoTime()` because it measures time in nanoseconds.

| Size | Input Type | Selection Sort | Merge Sort | Binary Search |
| --- | --- | ---: | ---: | ---: |
| Small, 10 | Random | 5,800 ns | 7,900 ns | 1,800 ns |
| Small, 10 | Sorted | 3,800 ns | 6,600 ns | 1,100 ns |
| Medium, 100 | Random | 139,400 ns | 103,500 ns | 1,300 ns |
| Medium, 100 | Sorted | 131,100 ns | 81,300 ns | 1,000 ns |
| Large, 1000 | Random | 15,545,400 ns | 1,297,800 ns | 3,600 ns |
| Large, 1000 | Sorted | 15,579,300 ns | 1,085,500 ns | 2,200 ns |

## Analysis

Merge Sort performed faster than Selection Sort for medium and large arrays. This happened because Selection Sort has O(n^2) complexity, so the number of operations grows very quickly. Merge Sort has O(n log n) complexity, so it handles larger arrays much better.

For very small arrays, Selection Sort was faster. This can happen because simple algorithms have less extra work. Merge Sort creates smaller arrays and uses recursion, so the overhead can be bigger than the benefit when the array has only 10 elements.

Sorted input did not improve Selection Sort much because Selection Sort still looks for the minimum element in the remaining part of the array every time. Merge Sort was a little faster on sorted input, but its Big-O complexity stayed the same.

The results match the expected Big-O complexity. As the input size increased, Selection Sort became much slower than Merge Sort.

Binary Search was very fast in every test. It is efficient because it does not check every element. It repeatedly cuts the search area in half. Binary Search needs a sorted array because the algorithm must know which half can be ignored.

## Screenshots

Program output screenshots are saved here:

- [Terminal run 1](docs/screenshots/1.png)
- [Terminal run 2](docs/screenshots/2.png)

## Reflection

This assignment helped me understand why algorithm complexity matters. Two sorting algorithms can both give the correct result, but their speed can be very different when the array becomes larger.

The theoretical Big-O results mostly matched the practical results. One interesting detail is that small arrays can behave differently because simple algorithms may have less overhead. The main challenge was making the experiment fair by copying arrays before sorting them, so each algorithm works with the same input.

## How to Run

```bash
python src/main.py
```

## Project Structure

```text
assignment3-sorting-searching/
+-- src/
|   +-- sorter.py
|   +-- searcher.py
|   +-- experiment.py
|   +-- main.py
+-- docs/
|   +-- screenshots/
+-- README.md
+-- .gitignore
```
