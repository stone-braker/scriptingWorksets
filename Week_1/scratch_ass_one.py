from math import sin, cos, pi, sqrt, acos, asin, degrees, radians

def get_angle_B(side_a, side_b, angle_A):
    """all integer inputs. angle_A must be input as degrees.
    this function converts it to radians and  before spitting it back out"""

    # these if statements are wrong. they don't match up with the laerd math site at all. 
    # fix em aight? you have until tuesday night. it's sunday biotch!
    
    if angle_A < 90 and side_a >= side_b:
        print('Exactly One Solution')
    if angle_A >= 90 and side_a <= side_b:
        print('NO SOLUTION!')
    elif angle_A >= 90 and side_a > side_b:
        print('\nOne Solution.\n')
    rad_A = radians(angle_A)
    angle_B = round(convert_degrees(abs(asin(sin(rad_A) * side_b/side_a))))
    print("Angle B is", angle_B, 'degrees\n')
    angleCee = get_angle_C(angle_A, angle_B)
    print("Angle C is", angleCee, 'degrees\n')
    return angle_B, angleCee

def convert_degrees(radian_input):
    converted = degrees(radian_input)
    return converted

def get_angle_C(angA, angB):
    angle_C = 180 - (int(angA) + int(angB))
    return angle_C
    
answerone = get_angle_B(28, 15, 110)
print(answerone)

#   1.
#   if angle_A is < 90 and side_a < side_b:
#       print('No solution')
#   if angle_A is < 90 and side_a == side_b:
#       print('One Solution')
#   if angle_A is acute angle and side_b > side_a and side_a > sin(side_a):
#       print('Two Solutions')
#   
#   2.
#   if angle_A is < 90 and side_a >= side_b:
#       print('Exactly One Solution')
#   
#   3.
#   if angle_A is >= 90 and side_a <= side_b:
#       print('No Solution')
#   if angle_A is >= 90 and side_a > side_b:
#       print("One Solution")
#   