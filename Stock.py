import numpy as np

class StockOnePeriod:
    """
    In this class, we only consider (at the moment) European call option.

    Parameters:
    - s: initial value of the stock
    - u, d: (upward factor, downward factor) possible values at time t=1
    - p: probability that the upward factor is activated

    Attributes:
    - initial_value: initial value of the stock at time t = 0
    - final_value: possible values of the stock at time t = 1
    - k: strike price of the option (is defined)
    - derivative: payoffs at time t = 1 (with respect to k)
    """
    def __init__(self, s, u, d, p):
        """
        Set the parameters s, u, p, d and compute the initial and final values.
        """
        # Define the binomial model
        self.u = float(u)
        self.d = float(d)
        self.p = float(p)

        # Compute initial and final values
        self.initial_value = float(s)
        self.final_value = np.asarray([self.u * self.initial_value, \
                                   self.d * self.initial_value])

    def compute_derivative(self, k):
        """
        The derivative is the difference between the possible values of the stock
        at time t = 1 and the strike price.
        Careful: Valid only for European call option
        """
        # Define the strike price at which the option exercices
        self.k = k
        # Compute the derivative
        self.derivative = np.maximum(self.final_value-self.k, 0)
        return(self.derivative)

class StockMultiPeriod:
    """
    In this class, we only consider (at the moment) European call option.

    Parameters:
    - s: initial value of the stock
    - u, d: (upward factor, downward factor) possible values at time t=1
    - p: probability that the upward factor is activated

    Attributes:
    - initial_value: initial value of the stock at time t = 0
    - final_value: possible values of the stock at time t = 1
    - k: strike price of the option (is defined)
    - derivative: payoffs at time t = 1 (with respect to k)
    """
    def __init__(self, s, u, d, p, T):
        """
        Set the parameters s, u, p, d and compute the initial and final values.
        """
        # Define the binomial model
        self.u = float(u)
        self.d = float(d)
        self.p = float(p)

        # Compute initial and final values
        self.values = [None]*T
        self.values[0] = s

        for i in range(1, T):
            self.values[i] = np.asarray([self.u * self.values[i-1], \
                                       self.d * self.values[i-1]])

    def compute_derivative(self, k):
       """
       The derivative is the difference between the possible values of the stock
       at time t = 1 and the strike price.
       Careful: Valid only for European call option
       """
       # Define the strike price at which the option exercices
       self.k = k
       # Compute the derivative
       self.derivative = np.maximum(self.values[self.T]-self.k, 0)
       return(self.derivative)
