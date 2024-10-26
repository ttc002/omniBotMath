import math
diametr_from_center_to_wheel = 10
diametr_wheel = 10
def divide_vector(ang,module):
    ang_rad = math.radians(ang)
    V = module
    V1 = round(V * math.cos(ang_rad),5)
    V2 = round(V * math.cos(math.radians(30)-ang_rad),5)
    V3 = round(V * math.cos(math.radians(150)-ang_rad),5)
    return V1,V2,V3


def vector_to_coords(vector):
    x = round(vector[0] * math.cos(math.radians(vector[1])))
    y = round(vector[0] * math.sin(math.radians(vector[1])))
    return x,y

def add_rot(steps,angle):

def count_bot_step(coords_now, coords_request, ang_now, ang_request):
    """
    передаётся: координаты конца движения, угол на который робот должен повернуться
    возвращается: шаги в виде списка вида [колесо1, колесо2, колесо3]
    """
        


print(divide_vector(int(input("angle: ")),int(input("len: "))))
