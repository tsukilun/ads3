import random


class Sorter:
    def basic_sort(self, arr):
        """Selection Sort."""
        n = len(arr)

        for i in range(n):
            min_index = i

            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

    def advanced_sort(self, arr):
        """Merge Sort."""
        if len(arr) <= 1:
            return

        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        self.advanced_sort(left)
        self.advanced_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def print_array(self, arr):
        print(arr)

    def generate_random_array(self, size):
        return [random.randint(1, 10000) for _ in range(size)]
