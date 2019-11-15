def admitter():
    gpa = float(input('Enter GPA:'))    
    if gpa >= (4.0):
        print('Admit')
    elif gpa >= 3.5:
        sat = float(input('Enter Sat:'))
        if sat >= 1400:
            print('Admit')
        elif sat >= 1100:
            print('Wailist')
        else:
            print('Deny')
    elif gpa >= 3.0:
        sat = float(input('Enter Sat:'))
        if sat >= 2000:
            print('Admit')        
        elif sat >= 1500:
            print('Waitlist')
        else:
            print('Deny')
    elif gpa < 3.0:
        sat = float(input('Enter Sat:'))
        if sat >= 2300:
            print('Admit')
        else:
            print('Deny')
    else:
        print('Deny')
admitter()