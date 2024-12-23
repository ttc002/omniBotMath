import math
bot_radius = 200 #radius from bot center to wheel; mm
diametr_wheel = 50 #diametr of wheel; mm
steps_per_rot = 800
class TimeZeroError(Exception):
    pass
class math_bot:
    def __init__(self, bot_radius_mm,diametr_wheel_mm,steps_per_rot):
        self.steps_per_mm = steps_per_rot/(math.pi*diametr_wheel_mm)
        self.steps_per_degree = (bot_radius_mm*2*math.pi*self.steps_per_mm)/360
        #print(self.steps_per_mm)
 
    def divide_vector(self,vector, k = 1,rotating = True,degrees = True):
        """"
        input: vectors list(3 vectors);  k - coefficient; rotating vector for length = natural number
        output: vectors [[len,0],[len,120],[len,240]] or vectors [len,len,len]
        """
        ang_rad = math.radians(vector[1])
        V = vector[0]
        vectors = [None,None,None]
        if degrees:
            vectors[0] = [round(k * V * math.sin(ang_rad+math.pi/2),3),0]
            vectors[1] = [round(k * V * math.sin(math.radians(240)-ang_rad+math.pi/2),3),240]
            vectors[2] = [round(k * V * math.sin(math.radians(120)-ang_rad+math.pi/2),3),120]
            print("0:",math.cos(ang_rad))
            print("1:",math.cos(math.radians(240)-ang_rad))
            print("2:",math.cos(math.radians(120)-ang_rad))
        else:
            vectors[0] = round(k * V * math.sin(ang_rad+math.pi/2),3)
            vectors[1] = round(k * V * math.sin(math.radians(240)-ang_rad+math.pi/2),3)
            vectors[2] = round(k * V * math.sin(math.radians(120)-ang_rad+math.pi/2),3)
        
        print("before rotating:",vectors)
        if rotating:
            for i in range(3):
                if vectors[i][0] < 0:
                    vectors[i][1] += 180
                    vectors[i][1] = vectors[i][1]%360
                    vectors[i][0] = abs(vectors[i][0])
            print("After rotting",vectors)
        else:
            pass
            #print("NO Rotating")
        return vectors

    def sum_vectors(self,vectors):
        """
        input: vectors [[len,angle],.....]
        output: [len,angle]
        """
        x_sum = 0
        y_sum = 0
        for length, angle in vectors:
            x_sum += length * math.cos(math.radians(angle))
            y_sum += length * math.sin(math.radians(angle))
        #print("Sums:",x_sum,y_sum)
        result_length = round(math.sqrt(x_sum**2 + y_sum**2),3)
        result_angle = abs(round(math.degrees(math.atan2(y_sum, x_sum)),3))
        return [result_length, result_angle]

    def vector_to_coords(self,vector):
        """
        input: [len,angle]
        output: [x,y]
        """
        x = round(vector[0] * math.cos(math.radians(vector[1])))
        y = round(vector[0] * math.sin(math.radians(vector[1])))
        return [x,y]

    def coords_to_vector(self,coords_move):
        move_x = coords_move[0]
        move_y = coords_move[1]
        ang = 0
        print("move X,Y: ",move_x,move_y)
        if move_x < 0 and move_y >=0:
            ang += 90
            print("adding 90 X")
        if move_y < 0 and move_x >=0:
            ang += 270
            print("adding 270 Y")
        if move_x < 0 and move_y < 0:
            ang+=180
            print("adding 180 XY")
        
        module = abs(math.sqrt(abs(move_x)**2 + abs(move_y)**2))
        angle = ang + math.degrees(math.atan2(abs(move_y) , abs(move_x)))
        angle = round(angle%360)
        #print(f"Len - {module}. Angle - {angle}")
        return [module,angle]

    def add_rot(self,steps,angle):
        if angle > 0:
            step = self.steps_per_degree * angle
        elif angle < 0:
            step = -1 *  self.steps_per_degree * angle
        else:
            step = 0
            print("No rotation")
        for i in range(3):
            steps[i] += step
        return steps
         
    def mm_to_steps(self,mm):
        steps = [0,0,0]
        for i in range(3):
            steps[i] = mm[i] * self.steps_per_mm
            
        return steps
    def mm_to_speed(self,time, vector):
        """
        input: time; vector
        output:vector speed(mm/s)
        """
        try:
            return [vector[0]/time,vector[1]]
        except:
            raise TimeZeroError
    def count_bot_steps(self, coords_move, ang_request,time):
        """
        input: coords moving, angle of bot rotation, time for all moving
        output: speeds for stepper motors
        """
        vector_move = self.coords_to_vector(coords_move)
        print("V move:",vector_move)
        vector_move = self.mm_to_speed(time,vector_move)
        divided_vectors = self.divide_vector(vector_move)
        print("vectors:",divided_vectors)
        k_count_vector = self.sum_vectors(divided_vectors)
        if abs(k_count_vector[1] - vector_move[1])>=0.1:
            print("VECTOR SUMMING ERROR")
            print("Sum:",k_count_vector)
            print("In:",vector_move)
            return [0,0,0]
        try:
            k = vector_move[0] / k_count_vector[0]
        except:
            k=1
        print("K:",k)
        wheel_mm = self.divide_vector(vector_move,k = k,rotating = False,degrees = False)
        wheel_mm = self.add_rot(wheel_mm,ang_request)

        steps = self.mm_to_steps(wheel_mm)
        return steps


if __name__ == "__main__":
    #a = input("coords now: ").split()
    #a[0] = int(a[0])
    #a[1] = int(a[1])
    b = input("coords req: ").split()
    b[0] = int(b[0])
    b[1] = int(b[1])
    c = int(input("time: "))
    d = int(input("ang req: "))
    botik = math_bot(200,50,800)
    print(botik.count_bot_steps(b,d,c))
