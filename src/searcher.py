class Searcher:
    def search(self, arr, target):
        """Binary Search. The array must already be sorted."""
        left = 0
        right = len(arr) - 1

        while left <= right:
            middle = (left + right) // 2

            if arr[middle] == target:
                return middle

            if arr[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1
