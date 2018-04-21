import numpy as np

class StockOnePeriod:
    """
    In this class, we only consider (at the moment) European call option.
    """
    def __init__(self, s, u, d, p, k):
        self.initial_value = float(s)
        self.strike_price = float(k)
        self.upward = float(u)
        self.downward = float(d)
        self.probability = float(p)

        self.final_value = np.asarray([self.upward * self.initial_value, \
                                   self.downward * self.initial_value])

    def compute_derivative(self):
        self.derivative = np.maximum(self.final_value-self.strike_price, 0)
        return(self.derivative)
