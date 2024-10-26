import math
def divide_vector(ang,module):
    ang_rad = math.radians(ang)
    V = module
    V1 = V * math.cos(ang_rad)
    return V1

print(divide_vector(int(input("angle: ")),int(input("len: "))))
