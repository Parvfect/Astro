'''So I am gonna just imagine say two bodies and the gf between them that determines
their positions relative to each other.'''
"""So the plan is simple, first I can make a 1d diagram using simple mean distance
and then later I can switch to a 2d one using right ascension, angle and longitude 
of ascending node"""

import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
#I am thinking of representing all the data using a panda frame

class Body:
    """A celestial body class, an object holds its properties"""
    def __init__(self, mass, postion, velocity):
        self.mass = mass
        self.position = postion
        self.velocity = velocity


def compute_force(body1, body2):
    """Calculates the gravitational force of attraction between the bodies"""
    G = 6.674e-11
    force_of_attraction = G*body1.mass*body2.mass/(body1.position.mod()- body2.position.mod())
    return force_of_attraction

def compute_gravity(body, foa):
    """Using the fsorce of attraction, we derive the acceleration of the body"""
    pass

def update_velocity(body):
    """Using the calculated acceleration, we update the velocity vector"""
    pass

def update_position(body, timestamp):
    """Using the current velocity, we update the position for the timestamp"""
    pass

def plot_system(bodies):
    """Plots a one dimensional model of all the bodies"""
    pass

Sun = Body(1.98e+30,0)
Neptune = Body(1.024e+26, 4.47e+10)
PlanetNine = Body(5.9e+27, 8.976e+10)