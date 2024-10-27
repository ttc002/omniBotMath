import math
bot_radius = 200 #radius from bot center to wheel; mm
diametr_wheel = 50 #diametr of wheel; mm
steps_per_rot = 800
def divide_vector(vector, k = 1):
    ang_rad = math.radians(vector[1])
    V = vector[0]
    V1 = round(k * V * math.cos(ang_rad))
    V2 = round(k * V * math.cos(math.radians(30)-ang_rad))
    V3 = round(k * V * math.cos(math.radians(150)-ang_rad))
    return [V1,V2,V3]


def vector_to_coords(vector):
    """
    input: [len,angle]
    output: [x,y]
    """
    x = round(vector[0] * math.cos(math.radians(vector[1])))
    y = round(vector[0] * math.sin(math.radians(vector[1])))
    return x,y
def coords_to_vector(coords_from,coords_to):
    module = math.sqrt((coords_from[0]-coords_to[0])**2 + (coords_from[1] - coords_to[1])**2)
    angle = math.degrees(math.atan2(coords_from[1]-coords_to[1] , coords_from[0] - coords_to[0]))
    print(f"Len - {module}. Angle - {angle}")
    return [module,angle]

def add_rot(steps,angle):
    pass
def count_bot_steps(coords_now, coords_request, ang_now, ang_request):
    """
    передаётся: координаты конца движения, угол на который робот должен повернуться
    возвращается: шаги в виде списка вида [колесо1, колесо2, колесо3]
    """
    ang_move = (ang_now - ang_request)%360
    #coords_move = [coords_now[0]-coords_request[0],coords_now[1]-coords_request[1]]
    vector_move = coords_to_vector(coords_now,coords_request)
    steps = divide_vector(vector_move)
    print(steps)
    
    pass
if __name__ == "__main__":
    a = input("coords now: ").split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    b = input("coords req: ").split()
    b[0] = int(b[0])
    b[1] = int(b[1])
    c = int(input("ang now: "))
    d = int(input("ang req: "))
    print(count_bot_steps(a,b,c,d))
