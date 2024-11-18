import math
bot_radius = 200 #radius from bot center to wheel; mm
diametr_wheel = 50 #diametr of wheel; mm
steps_per_rot = 800

class math_bot:
    def __init__(self, bot_radius_mm,diametr_wheel_mm,steps_per_rot):
        self.steps_per_mm = steps_per_rot/(math.pi*diametr_wheel_mm)
        self.steps_per_degree = (bot_radius_mm*2*math.pi*self.steps_per_mm)/360
        self.coords = [0,0]
        self.angle = 0
        
    def divide_vector(self,vector):
        ang_rad = math.radians(vector[1])
        V = vector[0] 
        vectors = [None,None,None]
        vectors[0] = [round(V * math.cos(ang_rad),2),0]
        print("VX:",vectors[0])
        VNX = self.sum_vectors([vector,[vectors[0][0],180]])
        print("VNX:",VNX)
        vectors[1] = [VNX[0] * math.cos(math.radians(210)-math.radians(VNX[1])),210]
        vectors[2] = self.sum_vectors([VNX,[vectors[1][0],(vectors[1][1]+180)%360]])
        for i in range(3):
            if vectors[i][0] < 0:
                vectors[i][0] = abs(vectors[i][0])
                vectors[i][1] = (vectors[i][1]+180)%360
        return vectors

    def sum_vectors(self,vectors):
        x_sum = 0
        y_sum = 0
        for length, angle in vectors:
            x_sum += length * math.cos(math.radians(angle))
            y_sum += length * math.sin(math.radians(angle))
        #print("Sums:",x_sum,y_sum)
        result_length = round(math.sqrt(x_sum**2 + y_sum**2),2)
        result_angle = abs(round(math.degrees(math.atan2(y_sum, x_sum)),2))
        return [result_length, result_angle]

    def vector_to_coords(self,vector):
        """
        input: [len,angle]
        output: [x,y]
        """
        x = round(vector[0] * math.cos(math.radians(vector[1])))
        y = round(vector[0] * math.sin(math.radians(vector[1])))
        return x,y

    def coords_to_vector(self,coords_from,coords_to):
        move_x = coords_to[0] - coords_from[0]
        move_y = coords_to[1] - coords_from[1]
        ang = 0
        print(move_x,move_y)
        if move_x < 0 or move_y < 0:
            ang = 180
        module = math.sqrt((coords_from[0]-coords_to[0])**2 + (coords_from[1] - coords_to[1])**2)
        angle = ang + math.degrees(math.atan2(abs(move_y) , abs(move_x)))
        angle = round(angle%360,2)
        print(f"Len - {module}. Angle - {angle}")
        return [module,angle]

    def add_rot(self,steps,angle,steps_per_rot,diametr_wheel,bot_radius):
        pass

    def count_bot_steps(self, coords_request, ang_request):
        """
        передаётся: координаты конца движения, угол на который робот должен повернуться
        возвращается: шаги в виде списка вида [колесо1, колесо2, колесо3]
        """
        ang_move = (self.angle - ang_request)%360
        vector_move = self.coords_to_vector(self.coords, coords_request)
        divided_vectors = self.divide_vector(vector_move)
        print("vectors:",divided_vectors)
        k_count_vector = self.sum_vectors(divided_vectors)
        
        print("Summed Vectors:",k_count_vector)

if __name__ == "__main__":
    #a = input("coords now: ").split()
    #a[0] = int(a[0])
    #a[1] = int(a[1])
    b = input("coords req: ").split()
    b[0] = int(b[0])
    b[1] = int(b[1])
    #c = 0 int(input("ang now: "))
    d = int(input("ang req: "))
    botik = math_bot(200,50,800)
    print(botik.count_bot_steps(b,d))
