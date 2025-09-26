import unittest
from TASK2 import assign_grade


class TestGradeAssignment(unittest.TestCase):

    def test_grade_a(self):
        scores = [90, 91, 95, 99, 100]
        for score in scores:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), "A")

    def test_grade_b(self):
        scores = [80, 81, 85, 89, 89.9]
        for score in scores:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), "B")

    def test_grade_c(self):
        scores = [70, 71, 75, 79, 79.9]
        for score in scores:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), "C")

    def test_grade_d(self):
        scores = [60, 61, 65, 69, 69.9]
        for score in scores:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), "D")

    def test_grade_f(self):
        scores = [0, 1, 30, 50, 59, 59.9]
        for score in scores:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), "F")

    def test_boundary_values(self):
        boundary_tests = [
            (100, "A"),
            (90, "A"),
            (89.9, "B"),
            (80, "B"),
            (79.9, "C"),
            (70, "C"),
            (69.9, "D"),
            (60, "D"),
            (59.9, "F"),
            (0, "F")
        ]
        for score, expected_grade in boundary_tests:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), expected_grade)

    def test_invalid_negative_scores(self):
        invalid_scores = [-1, -10, -100, -0.1]
        for score in invalid_scores:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), "Invalid input: score must be between 0 and 100.")

    def test_invalid_high_scores(self):
        invalid_scores = [101, 150, 200, 100.1]
        for score in invalid_scores:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), "Invalid input: score must be between 0 and 100.")

    def test_invalid_input_types(self):
        invalid_inputs = ["abc", "hello", None, [], {}]
        for invalid_input in invalid_inputs:
            with self.subTest(input=invalid_input):
                self.assertEqual(assign_grade(invalid_input), "Invalid input: score must be a number.")
    
    def test_boolean_inputs(self):
        boolean_tests = [
            (True, "F"),
            (False, "F")
        ]
        for boolean_input, expected_grade in boolean_tests:
            with self.subTest(input=boolean_input):
                self.assertEqual(assign_grade(boolean_input), expected_grade)
    
    def test_decimal_scores(self):
        decimal_tests = [
            (89.5, "B"),
            (79.5, "C"),
            (69.5, "D"),
            (59.5, "F"),
            (95.7, "A"),
            (85.3, "B"),
            (75.8, "C"),
            (65.2, "D"),
            (45.9, "F")
        ]
        
        for score, expected_grade in decimal_tests:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), expected_grade)
    
    def test_integer_scores(self):
        integer_tests = [
            (100, "A"),
            (90, "A"),
            (80, "B"),
            (70, "C"),
            (60, "D"),
            (50, "F"),
            (0, "F")
        ]
        
        for score, expected_grade in integer_tests:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), expected_grade)


if __name__ == "__main__":
    unittest.main()
