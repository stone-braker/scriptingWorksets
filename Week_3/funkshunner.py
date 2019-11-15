def pay_sched():
    balance = float(input('Enter balance:'))
    payment = float(input('Enter payment:'))
    apr = float(input('Enter APR:'))
    month = 0
    cal_int = (calcd_interest(balance, apr))

    print('Month\t\tInt.\t\tPay\t\tBalance')

    while balance >= payment:
        if month == 0:
            print(month, '\t\t\t\t\t\t', balance)
            month += 1
            balance -= (payment - cal_int)
        else:
            print(month, '\t\t', '{0:.2f}\t\t{1:.2f}\t\t{2:.2f}'.format(
                cal_int, payment, balance))
            month += 1
            balance -= (payment - cal_int)
            cal_int = round((calcd_interest(balance, apr)), 2)
            # if balance < payment:
            #    payment = balance + cal_int
            #    balance = 0
            #    print(month, '\t\t', '{0:.2f}\t\t{1:.2f}\t\t{2:.2f}'.format(
            #        cal_int, payment, balance))
            #    break
            if balance < payment:
                payment = balance + cal_int
                print(month, '\t\t', '{0:.2f}\t\t{1:.2f}\t\t{2:.2f}'.format(
                    cal_int, payment, balance))
                balance = 0
                month += 1
                print(month, '\t\t', '{0:.2f}\t\t{1:.2f}\t\t{2:.2f}'.format(
                    cal_int, payment, balance))
                break


def calcd_interest(bal, rate):
    applied_rate = (rate/100)/12
    interest = bal * applied_rate
    return round(interest, 2)


pay_sched()
