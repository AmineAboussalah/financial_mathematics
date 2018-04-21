from financial_mathematics.Bond import BondOnePeriod
from financial_mathematics.Stock import StockOnePeriod

import numpy as np

class Portfolio:

    def __init__(self, stock, bond, replicating_portfolio = False, x = 1, y = 1):

        if(replicating_portfolio):
            self.bond = bond
            self.stock = stock

            self.x = (1/(1+self.bond.interest_rate))*\
                        (self.stock.downward*self.stock.derivative[0]-self.stock.upward*self.stock.derivative[1])\
                        /(self.stock.upward - self.stock.downward)
            self.y = (1/self.stock.initial_value)*(self.stock.derivative[0]-self.stock.derivative[1])/(self.stock.upward - self.stock.downward)


            self.initial_value = self.x * self.bond.initial_value + self.y * self.stock.initial_value
            self.final_value = self.x * self.bond.final_value + self.y * self.stock.final_value
        else:
            self.x = x
            self.y = y

            self.bond = bond
            self.stock = stock

            self.initial_value = self.x * self.bond.initial_value + self.y * self.stock.initial_value
            self.final_value = self.x * self.bond.final_value + self.y * self.stock.final_value

    def is_replicating(self):
        if(np.all(self.final_value == self.stock.compute_derivative())):
            self.replicating = True
        else:
            self.replicating = False
        return(self.replicating)

    def price_option(self):
        if(self.is_replicating()):
            q = ((1+self.bond.interest_rate)-self.stock.downward)/(self.stock.upward-self.stock.downward)
            price_option = (1/(1+self.bond.interest_rate))*(q*self.stock.derivative[0] + (1-q)*self.stock.derivative[1])

        return(price_option)
