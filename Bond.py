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
        self.final_value = np.round(self.initial_value*(1.+self.r), 2)


class BondMultiPeriod:

    """
    Parameters:
    - r: (Float) interest rate of the bond
    - T: (int) period

    Attributes:
    - initial_value: (Float)
    - final_value: (Float)
    """

    def __init__(self, r, T):
        self.r = r
        self.T = T
        self.values = [None]*T

        self.values[0] = 1.

        for i in range(1, T):
            self.values[i] = np.round(self.values[i-1]*(1+self.r), 2)
