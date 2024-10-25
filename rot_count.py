import math
wheel_diametr = 10
def count_main_wheel(speed, ang):
    global wheel_diametr
    tang_vel = math.degrees(speed/math.cos(math.pi/3 - math.radians(ang)))
    return math.degrees((1*tang_vel)/(math.pi*wheel_diametr))

def count_help_wheel(speed,ang):
    global wheel_diametr
    numerator = speed*math.degrees(math.sin(math.pi/3 - math.radians(ang)))
    denumerator = math.degrees(math.cos(math.pi/3-math.radians(ang))) * math.degrees(math.cos(math.pi/6 - math.radians(ang)))
    return math.degrees((1 * (numerator/denumerator))/(math.pi*wheel_diametr))

ang = 0
speed = 1 # m/s
print(count_main_wheel(speed,ang))
