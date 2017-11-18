import xlrd
from account_book.data.data import Bill, TradeType


def read(location):
    workbook = xlrd.open_workbook(location)
    sheet_outcome = workbook.sheets()[0]
    sheet_income = workbook.sheets()[1]
    sheet_init = workbook.sheets()[2]
    sheet_transfer = workbook.sheets()[3]

    result = []
    result.extend(analytic(sheet_outcome, TradeType.OUTCOME))
    result.extend(analytic(sheet_income, TradeType.INCOME))
    result.extend(analytic(sheet_transfer, TradeType.TRANSFER))
    result.extend(analytic(sheet_init, TradeType.INIT))
    return result


def analytic(workbook, trade_type):
    bills = []
    for row_num in range(1, workbook.nrows):
        row = workbook.row_values(row_num)
        bill = Bill()
        if row:
            bill.trade_type = trade_type
            bill.date = row[9]
            bill.category = row[1]
            bill.sub_category = row[2]
            bill.first_account = row[3]
            bill.last_account = row[4]
            bill.project = row[8]
            bill.member = row[6]
            bill.merchant = row[7]
            bill.money = row[5]
            bill.remark = row[10]
            bills.append(bill)
    return bills


if __name__ == '__main__':
    lst = read("/Users/friday/Downloads/money.xls")
    print len(lst)
    print lst[0].category
    print lst[len(lst)-1].money
