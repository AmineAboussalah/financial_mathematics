class BondOnePeriod:

    """
    Parameters:
    - r: (Float) interest rate of the bond

    Attributes:
    - initial_value: (Float)
    - final_value: (Float)
    """

    def __init__(self, r):
        """
        The bound only depends on the interest rates.
        When considering x several bonds, we will multiply the bound value B by x.
        """
        self.r = float(r)
        self.initial_value = 1.
        self.final_value = self.initial_value*(1.+self.r)
