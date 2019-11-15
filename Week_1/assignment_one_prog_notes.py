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
###    make SSA a subclass of Triangle? even though it won't need all the same parameters?


#   side_a = int(input("Enter a length for side a"))
#   side_b = int(input("Enter a length for side b"))
#   angle_A = int(input("Enter angle A, in degrees"))

#
#def calc_ssa_step1():
#    # first find angle B
#    pass
#
#def calc_ssa_step2():
#    # then use all angle add to 180* to find C
#    pass
#
#def calc_ssa_step3():
#    # then use LOS again to find side c
#    pass
#
#def calc_ssa_second_possibility():
#    # somehow find out how to use the sin**-1 to find the other length. god i wish i remembered geometry better right now. 
#    pass
#
#def calc_ssa_no_solution():
#    # figure out what to do here if there isn't any solution
#    pass


#def Ssa(object):
#    __init__(self, side_a, side_b, angle_A)
#    self.side_a = side_a
#    self.side_b = side_b
#    self.angle_A = angle_A
#
#    def law_of_sines(self, side_a, side_b, angle_A):
#        angle_B = math.asin(side_a/math.sin(angle_A))
#        return angle_B
#
#
#class Triangle(object):
#    __init__(self, name, side_a = None, side_b = None, side_c = None, angle_A = None, angle_B = None, angle_C = None, no_sol = 'No solution!'):
#    self.name = name
#    self.side_a = side_a
#    self.side_b = side_b
#    self.side_c = side_c
#    self.angle_A = angle_A
#    self.angle_B = angle_B
#    self.angle_C = angle_C
#    self.no_sol = no_sol
#    if side_a == 'None' and side_b == 'None' and side_c == 'None':
#    raise ValueError('Please provide at least one side.')
#    if sum(x is None for x in (side_a, side_b, side_c) = 2 and sum(x is None for x in(angle_A, angle_B, angle_C) = 1:
#   
#    los_calc(self):

##def get_side_c(paired_angle, other_side, other_angle):
#    side_c = asin(paired_angle * other_side)/sin(other_angle)
#    return abs(side_c)