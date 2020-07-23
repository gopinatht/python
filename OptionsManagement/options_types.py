import enum

class OptionMoneyStatus(enum.Enum):
   In_The_Money = 1
   Out_Of_The_Money = 2
   At_The_Money = 3

class OptionType(enum.Enum):
    Call = 1
    Put = 2


class OptionBase:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def option_init(strike_price, cost, symbol, owner, seller):
        self.strike_price = strike_price
        self.cost = cost
        self.symbol = symbol
        self.owner = owner
        self.seller = seller
        self.option_money_status = OptionMoneyStatus.At_The_Money
        
    

class PptionCall(OptionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def call_init(self, strike_price, cost, symbol, owner, seller):
        self.option_init(strike_price, cost, symbol, owner, seller)
        self.option_type = OptionType.Call


class OptionPut(OptionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def put_init(self, strike_price, cost, symbol, owner, seller):
        self.option_init(strike_price, cost, symbol, owner, seller)
        self.option_type = OptionType.Put

