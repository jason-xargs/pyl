# -*- coding: utf-8 -*-
class TradeType(object):
    UNKNOWN = '0'
    INCOME = '1'
    OUTCOME = '2'
    TRANSFER = '3'
    INIT = '4'


class Member(object):
    JSON = 'Jason'
    GRACE = 'Grace'
    SHARE = '家庭公用'


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


class Summary(object):
    def __init__(self, income_json=None, income_grace=None, income_share=None, outcome_json=None, outcome_grace=None,
                 outcome_share=None, income=None, outcome=None, init=None):
        self.income_json = income_json
        self.income_grace = income_grace
        self.income_share = income_share
        self.outcome_json = outcome_json
        self.outcome_grace = outcome_grace
        self.outcome_share = outcome_share
        self.income = income
        self.outcome = outcome
        self.init = init
