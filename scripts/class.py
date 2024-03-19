class Traiangle:
    number_of_side = 3

    def __init__(self, a1,a2,a3):
        self.angle1 = a1
        self.angle2 = a2
        self.angle3 = a3

    def check_angles(self):
        if self.angle1 + self.angle2+ self.angle3 == 180:
            return True
        else:
            return False
        

tri = Traiangle(60,60,60)
tri2 = Traiangle(1,2,4)

print(tri.check_angles())
print(tri2.check_angles())
print(tri2.number_of_side)