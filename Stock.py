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
        Set the parameters s, u, p,  d and compute the initial and final values.
        """
        # Define the binomial model
        self.u = float(u)
        self.d = float(d)
        self.p = float(p)
        self.T = T

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

class StockMultiPeriod:
    """
    In this class, we only consider (at the moment) European call option.
​
    Parameters:
    - s: initial value of the stock
    - u, d: (upward factor, downward factor) possible values at time t=1
    - p: probability that the upward factor is activated
​
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
        self.T = T
​
        # Compute initial and final values
        self.values = [None]*(T+1)
        self.values[0] = s
​
        for i in range(1, T+1):
            self.values[i] = np.asarray([self.u * self.values[i-1], \
                                       self.d * self.values[i-1]])
            self.values[i] = np.sort(np.unique(self.values[i].ravel()))[::-1]

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

    def backward_computation(self, k, r):
        """
        The objective is to price the option at time t = 0. To do so, we use the
        risk neutral valuation that we compute one step at a time (with the martingales!).
        """
        # Compute q
        q = ((1+r)-self.d)/(self.u-self.d)

        # Allocate the pricing steps and set the last one
        self.pricing = [None]*(self.T+1)
        self.pricing[self.T] = self.compute_derivative(k)

        # Compute backward
        for i in reversed(range(1, self.T+1)):
            self.pricing[i-1] = np.zeros(i)
            for j in range(0, i):
                self.pricing[i-1][j] = (1/(1+r))*(np.mean(self.pricing[i][j: j+2]))

    def compute_portfolio(self, r):
        x = [None]*(self.T)
        y = [None]*(self.T)

        for i in range(0, self.T):
            x[i] = np.zeros(i+1)
            y[i] = np.zeros(i+1)
            for j in range(0, i+1):
                if i==0:
                    y[i][j] = (1/float(self.values[i]))*((self.pricing[i+1][j] - self.pricing[i+1][j+1])/(self.u-self.d))
                else:
                    y[i][j] = (1/self.values[i][j])*((self.pricing[i+1][j] - self.pricing[i+1][j+1])/(self.u-self.d))

                x[i][j] = (1/(1+r))*((self.u*self.pricing[i+1][j+1] - self.d*self.pricing[i+1][j])/(self.u-self.d))

        return(x, y)
