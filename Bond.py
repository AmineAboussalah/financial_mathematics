class BondOnePeriod:

    def __init__(self, r):
        """
        The bound only depends on the interest rates.
        When considering x several bonds, we will multiply the bound value B by x.
        """
        self.interest_rate = float(r)
        self.initial_value = 1
        self.final_value = self.initial_value*(1+self.interest_rate)
