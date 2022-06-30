class CompoundInterest:
    def __init__(self, _principle_amount, _interest_rate, _years):
        self.principle_amount = _principle_amount
        self.interest_rate = _interest_rate
        self.years = _years

    def compound_interest_calculator(self, principle_amount, interest_rate, years):
        p = principle_amount
        r = interest_rate / 100
        t = years
        n = 12

        final_amount = p * (1 + (r / n)) ** (n * t)
        return round(final_amount, 2)
