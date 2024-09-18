class TimSheet:

    def __init__(
        self,
        pp: int = None,
        pcc: int = None,
        tpp: int = None,
        sf: int = None,
        compsf: int = None,
        remod_cost: int = None,
        aii: int = None,
        sp: int = None,
        cc7p: int = None,
        prof: int = None,
        profp: float = None,
        url: str = None,
    ):
        self.purchase_price = pp
        self.purchase_closing_cost = pcc
        self.total_purchase_price = tpp
        self.square_feet = sf
        self.comp_square_feet = compsf
        self.remod_cost = remod_cost
        self.all_in_investment = aii
        self.sales_price = sp
        self.cc_at_7p = cc7p
        self.profit = prof
        self.profit_percent = profp
        self.url = url

    def get_purchase_closing_cost(self):
        self.purchase_closing_cost = int(self.purchase_price * 0.02)
        return self.purchase_closing_cost

    def get_total_purchase_price(self):
        self.total_purchase_price = self.purchase_price + self.purchase_closing_cost
        return self.total_purchase_price

    def get_remod_cost(self):
        self.remod_cost = self.square_feet * 80
        return self.remod_cost

    def get_all_in_investment(self):
        try:
            self.all_in_investment = int(self.remod_cost + self.total_purchase_price)
        except:
            self.all_in_investment = None
        return self.total_purchase_price

    def get_sales_price(self):
        try:
            self.sales_price = self.comp_square_feet * self.square_feet
        except:
            self.sales_price = None
        return self.sales_price

    def get_cc_at_7p(self):
        try:
            self.cc_at_7p = int(self.sales_price * 0.07)
        except:
            self.cc_at_7p = None
        return self.cc_at_7p

    def get_profit(self):
        try:
            self.profit = round((self.sales_price - self.all_in_investment) - self.cc_at_7p, 2)
        except:
            self.profit = None
        return self.profit

    def get_profit_percent(self):
        try:
            self.profit_percent = round(self.profit / self.all_in_investment, 2)
        except:
            self.profit_percent = None
        return self.profit_percent

    def get_calculations(self):
        self.get_purchase_closing_cost()
        self.get_total_purchase_price()
        self.get_remod_cost()
        self.get_all_in_investment()
        self.get_sales_price()
        self.get_cc_at_7p()
        self.get_profit()
        self.get_profit_percent()