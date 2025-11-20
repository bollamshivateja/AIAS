import unittest
from Task2 import merge_sort, merge

class TestMergeSort(unittest.TestCase):
    
    def test_empty_array(self):
        """Test sorting an empty array"""
        self.assertEqual(merge_sort([]), [])
    
    def test_single_element(self):
        """Test sorting a single element"""
        self.assertEqual(merge_sort([5.0]), [5.0])
    
    def test_already_sorted(self):
        """Test sorting an already sorted array"""
        self.assertEqual(merge_sort([1.0, 2.0, 3.0, 4.0]), [1.0, 2.0, 3.0, 4.0])
    
    def test_reverse_sorted(self):
        """Test sorting a reverse sorted array"""
        self.assertEqual(merge_sort([5.0, 4.0, 3.0, 2.0, 1.0]), [1.0, 2.0, 3.0, 4.0, 5.0])
    
    def test_unsorted_array(self):
        """Test sorting an unsorted array"""
        self.assertEqual(merge_sort([3.5, 1.2, 4.8, 2.1]), [1.2, 2.1, 3.5, 4.8])
    
    def test_duplicates(self):
        """Test sorting array with duplicate weights"""
        self.assertEqual(merge_sort([2.0, 1.0, 2.0, 1.0]), [1.0, 1.0, 2.0, 2.0])
    
    def test_negative_weights(self):
        """Test sorting array with negative values"""
        self.assertEqual(merge_sort([1.0, -2.5, 3.0, -1.0]), [-2.5, -1.0, 1.0, 3.0])
    
    def test_two_elements(self):
        """Test sorting two elements"""
        self.assertEqual(merge_sort([2.0, 1.0]), [1.0, 2.0])
class TestMerge(unittest.TestCase):  
    def test_merge_sorted_arrays(self):
        """Test merging two sorted arrays"""
        self.assertEqual(merge([1.0, 3.0], [2.0, 4.0]), [1.0, 2.0, 3.0, 4.0])
    def test_merge_empty_left(self):
        """Test merging with empty left array"""
        self.assertEqual(merge([], [1.0, 2.0]), [1.0, 2.0])
    
    def test_merge_empty_right(self):
        """Test merging with empty right array"""
        self.assertEqual(merge([1.0, 2.0], []), [1.0, 2.0])
    
    def test_merge_both_empty(self):
        """Test merging two empty arrays"""
        self.assertEqual(merge([], []), [])

        def test_merge_with_duplicates(self):
            """Test merging arrays with duplicate elements"""
            self.assertEqual(merge([1.0, 2.0, 2.0], [2.0, 3.0]), [1.0, 2.0, 2.0, 2.0, 3.0])

        def test_merge_with_negative_numbers(self):
            """Test merging arrays with negative numbers"""
            self.assertEqual(merge([-3.0, -1.0, 2.0], [-2.0, 0.0, 1.0]), [-3.0, -2.0, -1.0, 0.0, 1.0, 2.0])

        def test_merge_with_floats(self):
            """Test merging arrays with float values"""
            self.assertEqual(merge([1.1, 2.2, 3.3], [1.2, 2.3, 4.4]), [1.1, 1.2, 2.2, 2.3, 3.3, 4.4])

        def test_merge_with_all_left_smaller(self):
            """Test merging where all left elements are smaller"""
            self.assertEqual(merge([1.0, 2.0, 3.0], [4.0, 5.0]), [1.0, 2.0, 3.0, 4.0, 5.0])

        def test_merge_with_all_right_smaller(self):
            """Test merging where all right elements are smaller"""
            self.assertEqual(merge([4.0, 5.0], [1.0, 2.0, 3.0]), [1.0, 2.0, 3.0, 4.0, 5.0])
if __name__ == '__main__':
    unittest.main()