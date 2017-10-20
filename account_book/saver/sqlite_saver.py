import sqlite3

DATABASE = 'ACCOUNT_BOOK'

DROP_SQL = 'DROP TABLE IF EXISTS ACCOUNT_BOOK;'

CREATE_SQL = '''CREATE TABLE IF NOT EXISTS ACCOUNT_BOOK
    (
      ID            INT PRIMARY KEY NOT NULL,
      TRADE_TYPE    TEXT            NOT NULL,
      DATE          TEXT            NOT NULL,
      CATEGORY      TEXT,
      SUB_CATEGORY  TEXT,
      FIRST_ACCOUNT TEXT            NOT NULL,
      LAST_ACCOUNT  TEXT,
      PROJECT       TEXT,
      MEMBER        TEXT            NOT NULL,
      MERCHANT      TEXT,
      MONEY         REAL            NOT NULL,
      REMARK        TEXT
    )'''

INSERT_SQL = '''INSERT INTO ACCOUNT_BOOK
              (ID, TRADE_TYPE, DATE,CATEGORY, SUB_CATEGORY, FIRST_ACCOUNT, LAST_ACCOUNT,PROJECT, MEMBER,MERCHANT, MONEY, REMARK)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
               )'''


def create():
    conn = sqlite3.connect(DATABASE)
    conn.execute(DROP_SQL)
    conn.execute(CREATE_SQL)
    conn.close()


def insert(bills):
    conn = sqlite3.connect(DATABASE)
    for i in range(len(bills)):
        bill = bills[i]
        conn.execute(INSERT_SQL, args(i, bill))
        conn.commit()


def args(index, bill):
    result = [
        index + 1, bill.trade_type, bill.date, bill.category, bill.sub_category, bill.first_account,
        bill.last_account,
        bill.project, bill.member, bill.merchant, bill.money, bill.remark]
    return result
