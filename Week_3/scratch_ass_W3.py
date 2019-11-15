

# REQUIREMENTS:
# so, first it takes initial_balance and
# multiplies it by apr/12.
# then, it prints that as interest for month 1,
# adds that to balance,
# subtracts a payment of $150 from balance,
# then prints that amount as the new balance
# can i use a balance -=
# if the balance is below payment, payment = balance
# and some sort of something else i suppose


#ans = 199 / 12
#print('A two decimal floating point {0:.2f}'.format(ans))


# def pay_sched():
#    # first, take input
#    balance = float(input('Enter balance:'))
#    payment = float(input('Enter payment:'))
#    apr = float(input('Enter APR:'))
#    month = 0
#    cal_int = round(calcd_interest(balance, apr))
#
#    print("Month\t\tInt.\t\tPay\t\tBalance")
#    # calculate interest for first month's payment
#
#    while balance >= payment:
print(month, "\t\t", cal_int, "\t\t", payment, "\t\t", balance)
month += 1
balance -= (payment - cal_int)
cal_int = calcd_interest(balance, apr)
#
#
# def calcd_interest(bal, rate):
#    applied_rate = (rate/100)/12
#    interest = bal * applied_rate
#    return round(interest, 2)
#
#
# pay_sched()
##print(calcd_interest(1000, 19.9))
#


def pay_sched():
    balance = float(input('Enter balance:'))
    payment = float(input('Enter payment:'))
    apr = float(input('Enter APR:'))
    month = 0
    cal_int = (calcd_interest(balance, apr))

    print('Month\t\tInt.\t\tPay\t\tBalance')

    while balance >= payment:
        print(month, '\t\t', '{0:.2f}\t\t{1:.2f}\t\t{2:.2f}'.format(
            cal_int, payment, balance))
        month += 1
        balance -= (payment - cal_int)
        cal_int = round((calcd_interest(balance, apr)), 2)
        if balance < payment:
            payment = balance + cal_int
            print(month, '\t\t', '{0:.2f}\t\t{1:.2f}\t\t{2:.2f}'.format(
                cal_int, payment, balance))
            balance = 0
            break
# the problem is in the last if statement if balance < payment:
# balance should be zero afterward


def calcd_interest(bal, rate):
    applied_rate = (rate/100)/12
    interest = bal * applied_rate
    return round(interest, 2)


pay_sched()
