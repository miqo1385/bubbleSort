import unittest


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def bubble_sort_modified(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        #  check if any swaps occurred in this pass
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

    return arr


class our_function_test(unittest.TestCase):
    """A randomly generated array of integers."""

    def test_01(self):
        arr = [0, -1, 3, 2, 1]
        sort = bubble_sort(arr)
        self.assertEqual(sort, [-1, 0, 1, 2, 3])

    """An array already sorted in ascending order."""

    def test_02(self):
        arr = [1, 2, 3, 4]
        sort = bubble_sort(arr)
        self.assertEqual(sort, [1, 2, 3, 4])

    """An array sorted in descending order."""

    def test_03(self):
        arr = [4, 3, 2, 1, -1]
        sort = bubble_sort(arr)
        self.assertEqual(sort, [-1, 1, 2, 3, 4])

    """An array with all elements being the same."""

    def test_04(self):
        arr = [1, 1, 1, 1, 1, 1]
        sort = bubble_sort(arr)
        self.assertEqual(sort, [1, 1, 1, 1, 1, 1])

    """An empty array"""

    def test_05(self):
        arr = []
        sort = bubble_sort(arr)
        self.assertEqual(sort, [])

    """ an array with one element (edge cases)."""

    def test_06(self):
        arr = [1]
        sort = bubble_sort(arr)
        self.assertEqual(sort, [1])

    """A randomly generated array of integers."""

    def test_07(self):
        arr = [0, -1, 3, 2, 1]
        sort = bubble_sort_modified(arr)
        self.assertEqual(sort, [-1, 0, 1, 2, 3])

    """An array already sorted in ascending order."""

    def test_08(self):
        arr = [1, 2, 3, 4]
        sort = bubble_sort_modified(arr)
        self.assertEqual(sort, [1, 2, 3, 4])

    """An array sorted in descending order."""

    def test_09(self):
        arr = [4, 3, 2, 1, -1]
        sort = bubble_sort_modified(arr)
        self.assertEqual(sort, [-1, 1, 2, 3, 4])

    """An array with all elements being the same. here none elements will swap so the code will break without any 
    changes """

    def test_10(self):
        arr = [1, 1, 1, 1, 1, 1]
        sort = bubble_sort_modified(arr)
        self.assertEqual(sort, [1, 1, 1, 1, 1, 1])

    """An empty array"""

    def test_11(self):
        arr = []
        sort = bubble_sort_modified(arr)
        self.assertEqual(sort, [])

    """ an array with one element (edge cases)."""

    def test_12(self):
        arr = [1]
        sort = bubble_sort_modified(arr)
        self.assertEqual(sort, [1])


if __name__ == "__main__":
    unittest.main()
