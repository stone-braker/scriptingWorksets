from math import sin, cos, pi, sqrt, acos, asin, degrees, radians

#side_a = int(input("Enter a length for side a"))
#side_b = int(input("Enter a length for side b"))
#angle_A = int(input("Enter angle A, in degrees"))

def get_angle_B(side_a, side_b, angle_A):
    """all integer inputs. angle_A must be input as degrees.
    this function converts it to radians and back"""
    nosol1 = "no SOLUTION one"
    nosol2 = "NO solution TWO"
    rad_A = radians(angle_A)
    side_bsine = side_b * sin(rad_A)
    # FIRST from laerd, with thre possibilities:
    if angle_A < 90 and side_a < side_b:
        if side_a < side_bsine:
            print(nosol1) # and stop doing the math
            angle_B = 0
            angleCee = 0
        elif side_a == side_bsine:
            angle_B = round(convert_degrees(abs(asin(sin(rad_A) * side_b/side_a))))
            angleCee = get_angle_C(angle_A, angle_B)
            print("One Solution:\nAngle B =", angle_B, chr(176), "\nAngle C =", angleCee, chr(176))
        elif side_b > side_a and side_a > side_bsine:
            angle_B = round(convert_degrees(abs(asin(sin(rad_A) * side_b/side_a))))
            angleCee = get_angle_C(angle_A, angle_B)
            angle_B2 = 180 - angle_B
            angleCee2 = 180 - (angle_A + angle_B2)
            print("Two Solutions:\nAngle B =", angle_B, chr(176), "\nAngle C =", angleCee, chr(176), "\nOR:\nAngle B =", angle_B2, chr(176), "\nAngle C=", angleCee2, chr(176))
    # SECOND from laerd, exactly one:
    elif angle_A < 90 and side_a >= side_b:
        angle_B = round(convert_degrees(abs(asin(sin(rad_A) * side_b/side_a))))
        angleCee = get_angle_C(angle_A, angle_B)
        print("Exactly One Solution:\nAngle B =", angle_B, chr(176), "Angle C =", angleCee, chr(176))
    # THIRD from laerd, two possibilities:
    elif angle_A >= 90 and side_a <= side_b:
        angle_B = 0
        angleCee = 0
        print(nosol2)
    elif angle_A >= 90 and side_a > side_b:
        angle_B = round(convert_degrees(abs(asin(sin(rad_A) * side_b/side_a))))
        angleCee = get_angle_C(angle_A, angle_B)
        print('\nOne Solution With Obtuse or Right Triangle.\nAngle B =', angle_B, chr(176), 'Angle C =', angleCee, chr(176))
#    return angle_B, angleCee

def convert_degrees(radian_input):
    converted = degrees(radian_input)
    return converted

def get_angle_C(angA, angB):
    angle_C = 180 - (int(angA) + int(angB))
    return angle_C
    
answerone = get_angle_B(15, 26, 29)
print(answerone)


###    read global module index for math (convert radians<>degrees?)
###    cmath.sin(x) - will this return sine of x, in degrees?
###    math.sin(x) - return the sine of x, in radians
###    math.cos(x) - return the cosine of x, in radians
###    law of cosines: c**2 = a**2 + b**2 - 2ab(cos(C))
###    law of sines: a/sin A = b/sin B = c/sin C ... use this first to find angle B
###    then use A + B + C = 180 degrees
###    then use law of sines again to find final side c
###    
###    create a Class Triangle with all a A b B c C possiblilities as empty arguments, ie (side_a = None, angle_A = None)
###    create Functions that will generate the missing angles and sides given the parameters of the Class object
###    six different types AAA AAS ASA SAS SSA SSS six different functions?
###    use if 'parameter equal to angle_A' == None, and the next and the next,
###    then it is an AAS, or an SSA or whatever it is, use to decide which functions should be ran,
###    ie, which formula is needed and in what order to figure out the other sides/angles
###