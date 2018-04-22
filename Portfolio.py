from financial_mathematics.Bond import BondOnePeriod
from financial_mathematics.Stock import StockOnePeriod

import numpy as np

class Portfolio:

    """
    Parameters:
    - stock: (StockOnePeriod) the stock owned in the Portfolio
    - bond: (BondOnePeriod) the bond owned in the Portfolio
    - x: (Float) number of SEK in the account
    - y: (Float) number of owned stock

    Attributes:
    - initial_value: (Float) Value of the Portfolio at time t=O
    - final_value: (Float) Value of the Portfolio at time t=1
    - replicating: (Boolen) Is the Portfolio replicating the stock
    """

    def __init__(self, stock, bond, replicating_portfolio = False, x = 1, y = 1):
        """
        A portfolio contains by definition both a stock and a bond, that should
        defined prior to initializing a Portfolio.

        Regarding (x, y), there are two ways to initialize those values:
        1. Pass them as parameters, therefore indicating how many stocks and bonds are owned.
        2. (x, y) should replicate the claim X on the stock and should satisfy risk neutral validation formula.
        We therefore compute the x and y based on the above mentioned formula.
        """
        # Stock and bond
        self.bond = bond
        self.stock = stock

        # Construct a replicating portfolio based on the stock and the bond
        if(replicating_portfolio):
            self.x = (1/(1+self.bond.r))*\
                        (self.stock.d*self.stock.derivative[0]-self.stock.u*self.stock.derivative[1])/(self.stock.u - self.stock.d)
            self.y = (1/self.stock.initial_value)*(self.stock.derivative[0]-self.stock.derivative[1])/(self.stock.u - self.stock.d)

        # Define manually the portfolio
        else:
            self.x = x
            self.y = y

        # Compute the initial and final value of the portfolio
        self.initial_value = self.x * self.bond.initial_value + self.y * self.stock.initial_value
        self.final_value = self.x * self.bond.final_value + self.y * self.stock.final_value

    def is_replicating(self):
        """
        Based on the stock, the bond, x and y, this method checks whether the portfolio replicates
        the claim X. The portfolio does if its final value is equal to the derivative of the stock.
        """
        if(np.all(self.final_value == self.stock.compute_derivative())):
            self.replicating = True
        else:
            self.replicating = False
        return(self.replicating)

    def price_option(self):
        """
        If the portfolio replicates the claim X, a proposition indicates that the price of the option
        can be computed as discounted expectations of future payoffs.
        Careful: we should use the martingale probabilities Q, rather than objective probabilities P.
        """
        if(self.is_replicating()):
            q = ((1+self.bond.r)-self.stock.d)/(self.stock.u-self.stock.d)
            price_option = (1/(1+self.bond.r))*(q*self.stock.derivative[0] + (1-q)*self.stock.derivative[1])

        return(price_option)
