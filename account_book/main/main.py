from account_book.reader import excel_reader
from account_book.saver import sqlite_saver

if __name__ == "__main__":
    lst = excel_reader.read('/Users/friday/Downloads/myMoney.xls')
    sqlite_saver.create()
    sqlite_saver.insert(lst)
