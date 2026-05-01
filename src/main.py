from experiment import Experiment
from searcher import Searcher
from sorter import Sorter


def main():
    sorter = Sorter()
    searcher = Searcher()
    experiment = Experiment()

    sample = sorter.generate_random_array(10)

    print("Sample array:")
    sorter.print_array(sample)

    sorted_sample = sample.copy()
    sorter.advanced_sort(sorted_sample)

    print("Sorted sample:")
    sorter.print_array(sorted_sample)

    target = sorted_sample[5]
    index = searcher.search(sorted_sample, target)
    print(f"Binary Search: target {target} found at index {index}")
    print()

    experiment.run_all_experiments()


if __name__ == "__main__":
    main()
