# -*- coding: utf-8 -*-

from account_book.data.data import Member
from account_book.data.data import TradeType


def get_sql(trade_type, *param):
    if len(param) == 0:
        return '''
            SELECT SUM(money) FROM ACCOUNT_BOOK WHERE TRADE_TYPE = ?
        ''', trade_type
    else:
        return '''
            SELECT SUM(money) FROM ACCOUNT_BOOK WHERE TRADE_TYPE = ? AND MEMBER = ?
        ''', trade_type, param[0]


def get_init(conn):
    sql = get_sql(TradeType.INIT)
    cursor = conn.execute(sql[0], sql[1])
    return cursor.fetchone()[0]


def get_income(conn):
    sql = get_sql(TradeType.INCOME)
    cursor = conn.execute(sql[0], sql[1])
    return cursor.fetchone()[0]


def get_outcome(conn):
    sql = get_sql(TradeType.OUTCOME)
    cursor = conn.execute(sql[0], sql[1])
    return cursor.fetchone()[0]


def get_json_income(conn):
    sql = get_sql(TradeType.INCOME, Member.JSON)
    return conn.execute(sql[0], (sql[1], sql[2])).fetchone()[0]


def get_grace_income(conn):
    sql = get_sql(TradeType.INCOME, Member.GRACE)
    return conn.execute(sql[0], (sql[1], sql[2])).fetchone()[0]


def get_share_income(conn):
    sql = get_sql(TradeType.INCOME, Member.SHARE)
    return conn.execute(sql[0], (sql[1], sql[2])).fetchone()[0]


def get_json_outcome(conn):
    sql = get_sql(TradeType.OUTCOME, Member.JSON)
    return conn.execute(sql[0], (sql[1], sql[2])).fetchone()[0]


def get_grace_outcome(conn):
    sql = get_sql(TradeType.OUTCOME, Member.GRACE)
    return conn.execute(sql[0], (sql[1], sql[2])).fetchone()[0]


def get_share_outcome(conn):
    sql = get_sql(TradeType.OUTCOME, Member.SHARE)
    return conn.execute(sql[0], (sql[1], sql[2])).fetchone()[0]
