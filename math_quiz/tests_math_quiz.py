import unittest
from math_quiz import rand_int, rand_op, math_prob, math_quiz


class TestMathGame(unittest.TestCase):

    def test_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_rand_op(self):
        # Test if random operator is one of the specified operators
        for _ in range(1000):
            rand_operator = rand_op()
            self.assertIn(rand_operator, ['+', '-', '*'])

    def test_math_prob(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                 (10, 5, '-', '10 - 5', 5),
                 (3, 4, '*', '3 * 4', 12),
                 (2, 3, '+', '2 + 3', 5)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # Test if the math problem and answer are correct
                problem, answer = math_prob(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
