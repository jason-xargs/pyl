class TradeType(object):
    UNKNOWN = 0
    INCOME = 1
    OUTCOME = 2
    TRANSFER = 3
    INIT = 4


class Bill(object):
    def __init__(self, trade_type=TradeType.UNKNOWN, date=None, category=None, sub_category=None, first_account=None,
                 last_account=None, project=None, member=None, merchant=None, money=None, remark=None):
        self.trade_type = trade_type
        self.date = date
        self.category = category
        self.sub_category = sub_category
        self.first_account = first_account
        self.last_account = last_account
        self.project = project
        self.member = member
        self.merchant = merchant
        self.money = money
        self.remark = remark
