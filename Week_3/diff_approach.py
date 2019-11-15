def pay_sched():
    balance = float(input('Enter balance:'))
    payment = float(input('Enter payment:'))
    apr = float(input('Enter APR:'))
    month = 0
    cal_int = calcd_interest(balance, apr)

    print('Month\t\tInt.\t\tPay\t\tBalance')
    if month == 0:
        print(month, '\t\t\t\t\t\t', balance)
        month += 1
    bal_pos = True
    while bal_pos == True:
        balance -= (payment - cal_int)
        print(month, '\t\t', cal_int, '\t\t', payment, '\t\t', balance)
        month += 1
        cal_int = calcd_interest(balance, apr)
        if balance < payment:
            payment = balance + cal_int
            balance = 0
            print(month, '\t\t', cal_int, '\t\t', payment, '\t\t', balance)
            bal_pos = False


def calcd_interest(bal, rate):
    applied_rate = (rate/100)/12
    interest = bal * applied_rate
    return round(interest, 2)


pay_sched()
