def admitter():
    gpa = float(input('Enter GPA:'))    
    if gpa >= (4.0):
        print('\nAdmit')
    elif gpa >= 3.5:
        sat = float(input('\nEnter SAT:'))
        if sat > 1400:
            print('\nAdmit')
        elif sat >= 1100:
            print('\nWaitlist')
        else:
            print('\nDeny')
    elif gpa >= 3.0:
        sat = float(input('Enter SAT:'))
        if sat >= 2000:
            print('\nAdmit')        
        elif sat >= 1500:
            print('\nWaitlist')
        else:
            print('\nDeny')
    elif gpa < 3.0:
        sat = float(input('Enter SAT:'))
        if sat >= 2300:
            print('\nAdmit')
        else:
            print('\nDeny')
    else:
        print('\nDeny')
admitter()