import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    # Tests
    def setUp(self):
        self.list = [1200, 6789, 1234, 43739, 2427, 2]

    # Test latest score (the last thing in the list)
    def test_latest_score_result_2(self):
        self.assertEqual(2, latest(self.list))

    # Test personal best (the highest score in the list)
    def test_personal_best_result_43739(self):
        self.assertEqual(43739, personal_best(self.list))

    # Test top three from list of scores
    def test_top_three(self):
        self.assertEqual([43739, 6789, 2427], personal_top_three(self.list))

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
