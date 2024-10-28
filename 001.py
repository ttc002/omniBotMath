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

def sum_vectors(vectors):
    x_sum = 0
    y_sum = 0
    for length, angle in vectors:
        x_sum += length * math.cos(math.radians(angle))
        y_sum += length * math.sin(math.radians(angle))
    result_length = round(math.sqrt(x_sum**2 + y_sum**2))
    result_angle = round(math.degrees(math.atan2(y_sum, x_sum)))
    return [result_length, result_angle]

def vector_to_coords(vector):
    """
    input: [len,angle]
    output: [x,y]
    """
    x = round(vector[0] * math.cos(math.radians(vector[1])))
    y = round(vector[0] * math.sin(math.radians(vector[1])))
    return x,y

def coords_to_vector(coords_from,coords_to):
    move_x = coords_to[0] - coords_from[0]
    move_y = coords_to[1] - coords_from[1]
    ang = 0
    print(move_x,move_y)
    if move_x < 0 or move_y < 0:
        ang = 180
    module = math.sqrt((coords_from[0]-coords_to[0])**2 + (coords_from[1] - coords_to[1])**2)
    angle = ang + math.degrees(math.atan2(abs(move_y) , abs(move_x)))
    angle = angle%360
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
    summed_vectors = divide_vector(vector_move)
    k_count_vector = sum_vectors([[summed_vectors[0],90],[summed_vectors[1],135],[summed_vectors[2],45]])
    print(k_count_vector)
    pass

if __name__ == "__main__":
    a = input("coords now: ").split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    b = input("coords req: ").split()
    b[0] = int(b[0])
    b[1] = int(b[1])
    c = 0#int(input("ang now: "))
    d = 0#int(input("ang req: "))
    print(count_bot_steps(a,b,c,d))
