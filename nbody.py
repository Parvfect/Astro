import math

import random
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

class point:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

class body:
    def __init__(self, location, mass, velocity, name = "", color="black"):
        self.location = location
        self.mass = mass
        self.velocity = velocity
        self.name = name
        self.color = color

def calculate_single_body_acceleration(bodies, body_index):
    G_const = 6.67408e-11 #m3 kg-1 s-2
    acceleration = point(0,0,0)
    target_body = bodies[body_index]
    for index, external_body in enumerate(bodies):
        if index != body_index:
            r = (target_body.location.x - external_body.location.x)**2 + (target_body.location.y - external_body.location.y)**2 + (target_body.location.z - external_body.location.z)**2
            r = math.sqrt(r)
            tmp = G_const * external_body.mass / r**3
            acceleration.x += tmp * (external_body.location.x - target_body.location.x)
            acceleration.y += tmp * (external_body.location.y - target_body.location.y)
            acceleration.z += tmp * (external_body.location.z - target_body.location.z)

    return acceleration

def compute_velocity(bodies, time_step = 1):
    for body_index, target_body in enumerate(bodies):
        acceleration = calculate_single_body_acceleration(bodies, body_index)

        target_body.velocity.x += acceleration.x * time_step
        target_body.velocity.y += acceleration.y * time_step
        target_body.velocity.z += acceleration.z * time_step 


def update_location(bodies, time_step = 1):
    for target_body in bodies:
        target_body.location.x += target_body.velocity.x * time_step
        target_body.location.y += target_body.velocity.y * time_step
        target_body.location.z += target_body.velocity.z * time_step

def compute_gravity_step(bodies, time_step = 1):
    compute_velocity(bodies, time_step = time_step)
    update_location(bodies, time_step = time_step)

def plot_output(bodies, outfile):
    fig = plot.figure()
    colors = ['yellow', 'red', 'black']
    ax = fig.add_subplot(1,1,1, projection='3d')
    max_range = 0
    for current_body in bodies: 
        print(current_body)
        max_dim = max(max(current_body["x"]),max(current_body["y"]),max(current_body["z"]))
        if max_dim > max_range:
            max_range = max_dim
        ax.plot(current_body["x"], current_body["y"], current_body["z"],  label = current_body["name"], marker = 5, color = current_body['color'])        
    
    ax.set_xlim([-max_range,max_range])    
    ax.set_ylim([-max_range,max_range])
    ax.set_zlim([-max_range,max_range])
    ax.legend()
    plot.show()
    plot.savefig(outfile)


def run_simulation(bodies, names = None, time_step = 1, number_of_steps = 10000, report_freq = 100):

    #create output container for each body
    body_locations_hist = []
    for current_body in bodies:
        body_locations_hist.append({"x":[], "y":[], "z":[], "name":current_body.name, "color":current_body.color})
        
    for i in range(1,number_of_steps):
        compute_gravity_step(bodies, time_step = 1000)            
        
        if i % report_freq == 0:
            for index, body_location in enumerate(body_locations_hist):
                body_location["x"].append(bodies[index].location.x)
                body_location["y"].append(bodies[index].location.y)           
                body_location["z"].append(bodies[index].location.z)       

    return body_locations_hist        
            
#planet data (location (m), mass (kg), velocity (m/s)
sun = {"location":point(0,0,0), "mass":2e30, "velocity":point(0,0,0), "color":"yellow"}
neptune = {"location":point(0,4.5e12,0), "mass":1e26, "velocity":point(5477,0,0), "color":"purple"}
planet_nine = {"location":point(0,3.7e12, 0), "mass":60e24, "velocity":point(4748,0,0), "color":"black"}
if __name__ == "__main__":

    #build list of planets in the simulation, or create your own
    bodies = [
        body( location = planet_nine['location'], mass = planet_nine['mass'], velocity = planet_nine['velocity'], name = 'planet nine', color = planet_nine["color"]),
        body( location = neptune["location"], mass = neptune["mass"], velocity = neptune["velocity"], name = "neptune", color = neptune["color"]),
        body( location = sun["location"], mass = sun["mass"], velocity = sun["velocity"], name = "sun", color = sun['color']),
        ]
    
    motions = run_simulation(bodies, time_step = 10000000, number_of_steps = 80000, report_freq = 1000)
    plot_output(motions, outfile = 'orbits.png')