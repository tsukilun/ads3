from time import perf_counter_ns

from searcher import Searcher
from sorter import Sorter


class Experiment:
    def __init__(self):
        self.sorter = Sorter()
        self.searcher = Searcher()

    def measure_sort_time(self, arr, sort_type):
        test_arr = arr.copy()

        start_time = perf_counter_ns()

        if sort_type == "basic":
            self.sorter.basic_sort(test_arr)
        elif sort_type == "advanced":
            self.sorter.advanced_sort(test_arr)
        else:
            raise ValueError("sort_type must be 'basic' or 'advanced'")

        end_time = perf_counter_ns()
        return end_time - start_time

    def measure_search_time(self, arr, target):
        sorted_arr = arr.copy()
        self.sorter.advanced_sort(sorted_arr)

        start_time = perf_counter_ns()
        index = self.searcher.search(sorted_arr, target)
        end_time = perf_counter_ns()

        return end_time - start_time, index

    def run_all_experiments(self):
        sizes = [
            ("Small", 10),
            ("Medium", 100),
            ("Large", 1000),
        ]

        print("Algorithm Performance Results")
        print("=" * 70)
        print("Basic sort: Selection Sort")
        print("Advanced sort: Merge Sort")
        print("Search: Binary Search")
        print("=" * 70)
        print()

        for size_name, size in sizes:
            random_arr = self.sorter.generate_random_array(size)
            sorted_arr = list(range(1, size + 1))

            self._print_dataset_results(size_name, "Random", random_arr)
            self._print_dataset_results(size_name, "Sorted", sorted_arr)

    def _print_dataset_results(self, size_name, data_type, arr):
        target = arr[len(arr) // 2]

        basic_time = self.measure_sort_time(arr, "basic")
        advanced_time = self.measure_sort_time(arr, "advanced")
        search_time, found_index = self.measure_search_time(arr, target)

        print(f"{size_name} array ({data_type}, {len(arr)} elements)")
        print(f"Selection Sort time: {basic_time} ns")
        print(f"Merge Sort time:     {advanced_time} ns")
        print(f"Binary Search time:  {search_time} ns")
        print(f"Target {target} found at sorted index: {found_index}")

        if advanced_time < basic_time:
            print("Faster sorting algorithm: Merge Sort")
        else:
            print("Faster sorting algorithm: Selection Sort")

        print("-" * 70)
