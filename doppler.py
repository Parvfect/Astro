import numpy as np 
import matplotlib.pyplot as plt
import math

G = 6.67e-11

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


def get_doppler():
    """Gets the doppler shift as a function of ..."""    

    M_Neptune = 1e26

    #Getting the velocity of the orbiter
    r_p = 3.5e8
    x = np.arange(1.0,10.0,0.1)
    r_a = [r_p*i for i in x]
    a = [(r_p + i)/2 for i in r_a]
    v_som = []
    e_i = []

    for c,i in enumerate(x):
        v_som.append(math.sqrt(G*M_Neptune*((2/r_p)- (1/a[c]))))
        e_i.append((r_a[c] - r_p)/(r_a[c] + r_p))
    
    
	#Getting the velocity of Triton
    r_a_tri = 355000e3
    r_p_tri = r_a_tri
    a_tri = (r_a_tri + r_p_tri)/2
    r_tri = r_p_tri

    v_tri = math.sqrt(G*M_Neptune*((2/r_tri)-(1/a_tri)))
    
   
    #Getting the relative velocities between the orbiter and triton
    v_rel = []
    for i in v_som:
        v_rel.append(i- v_tri)
    
    #Plotting the eccentricity of orbit vs the relative velocities
    plt.plot(e_i, v_rel)
    plt.xlabel("Somerville orbit Eccentricity")
    plt.ylabel("Sommerville flyby velocity at Triton [m/s]")
    plt.show()    

    '''Finding the Doppler Shift'''

    #Frequency of emitted signal
    f_s = 2000
    #Speed of light
    c = 3*10e8
    #Setting the velocity of observer and source
    v_o = v_som
    v_s = v_tri
    f_o = []
    #Frequency recieved by observer
    for i in v_o:
        f_o.append(((c+i)/(c+v_s))*f_s)

    #Plotting the eccentricity of orbit vs the frequency of communications recieved
    plt.plot(e_i, f_o)
    plt.xlabel("Sommerville orbital eccentricity")
    plt.ylabel("Frequency of received communications")
    plt.show()

    #Creating a range of the relative velocities
    v_rel = np.arange(0, 100000, 100)

    f_o_range = []
    for i in v_rel:
        #Imagining the case where Triton is stationary that is Triton's pov
        f_o_range.append(((c+i)/(c))*f_s)


    #Plotting the relative velocities vs the frequency of communications recieved
    plt.plot(v_rel, f_o_range)
    plt.xlabel("Relative velocity between Triton and Sommerville [m/s]")
    plt.ylabel("Frequency of recieved communications")
    plt.show()



get_doppler()