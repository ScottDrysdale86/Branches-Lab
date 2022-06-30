import unittest

from src.compound_interest import CompoundInterest


class CompoundInterestTest(unittest.TestCase):
    def setUp(self):
        self.calculation1 = CompoundInterest(100, 10, 20)
        self.calculation2 = CompoundInterest(100, 6, 10)
        self.calculation3 = CompoundInterest(100000, 5, 8)
        self.calculation4 = CompoundInterest(0, 10, 1)
        self.calculation5 = CompoundInterest(100, 0, 10)

    # Tests
    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_100_10_20_result_732_81(self):
        self.assertEqual(
            732.81,
            self.calculation1.compound_interest_calculator(
                self.calculation1.principle_amount,
                self.calculation1.interest_rate,
                self.calculation1.years,
            ),
        )

    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_100_6_10_result_181_94(self):
        self.assertEqual(
            181.94,
            self.calculation2.compound_interest_calculator(
                self.calculation2.principle_amount,
                self.calculation2.interest_rate,
                self.calculation2.years,
            ),
        )

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_100000_5_8_result_149058_55(self):
        self.assertEqual(
            149058.55,
            self.calculation3.compound_interest_calculator(
                self.calculation3.principle_amount,
                self.calculation3.interest_rate,
                self.calculation3.years,
            ),
        )

    # Should return 0.00 given 0 principal, 10 percent, 1 year
    def test_0_10_1_result_0_00(self):
        self.assertEqual(
            0.00,
            self.calculation3.compound_interest_calculator(
                self.calculation4.principle_amount,
                self.calculation4.interest_rate,
                self.calculation4.years,
            ),
        )

    # Should return 100.00 given 100 principal, 0 percent, 10 years
    def test_100_0_10_result_100_00(self):
        self.assertEqual(
            100.00,
            self.calculation5.compound_interest_calculator(
                self.calculation5.principle_amount,
                self.calculation5.interest_rate,
                self.calculation5.years,
            ),
        )

    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month
