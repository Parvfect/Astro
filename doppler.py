
class Body:
    
    def __init__(self, position_x, position_y, velocity_x, velocity_y, orbital_radius, radius, mass, time_period):
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.orbital_radius = orbital_radius
        self.radius = radius
        self.mass = mass
        self.time_period = time_period

class Triton(Body):
    
    def __init__(self, position_x, position_y):
        super.__init__(self, position_x, position_y, 3.1e3, 3.1e3, 3.5e8, 1.35e7, 2.14e22, 5.1e5)



a = Triton(0,0)
print(a.velocity_x, a.velocity_y)