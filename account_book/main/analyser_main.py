# -*- coding: utf-8 -*-

import sqlite3
from account_book.analyser import analyser
from account_book.data.data import Summary

DATABASE = 'ACCOUNT_BOOK'


def get_summary():
    conn = sqlite3.connect(DATABASE)
    conn.text_factory = str
    summary = Summary()
    try:
        summary.init = analyser.get_init(conn)
        summary.income_json = analyser.get_json_income(conn)
        summary.income_grace = analyser.get_grace_income(conn)
        summary.income_share = analyser.get_share_income(conn)
        summary.outcome_json = analyser.get_json_outcome(conn)
        summary.outcome_grace = analyser.get_grace_outcome(conn)
        summary.outcome_share = analyser.get_share_outcome(conn)
        summary.income = analyser.get_income(conn)
        summary.outcome = analyser.get_outcome(conn)
        return summary
    except Exception, e:
        print e
    finally:
        conn.close()


def analyse(summary):
    init = summary.init
    if init is None:
        init = 0
        summary.init = 0
    now = summary.init + summary.income - summary.outcome
    surplus = now - init
    print init, now, surplus

    json_surplus = summary.income_json - summary.outcome_json - summary.outcome_share * 0.7
    print json_surplus
    grace_surplus = summary.income_grace - summary.outcome_grace - summary.outcome_share * 0.3
    print grace_surplus


if __name__ == '__main__':
    analyse(get_summary())
