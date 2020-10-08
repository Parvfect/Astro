import spiceypy as spice
import datetime
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from dateutil.relativedelta import relativedelta

#Meta kernels >>> Loading individually
#Load the kernel for leap seconds
spice.furnsh("/home/parv/Documents/Astro/kernels/naif0012.tls")

#Loading the frame of referance for positioning
spice.furnsh("/home/parv/Documents/Astro/kernels/de405.bsp")
spice.furnsh("/home/parv/Documents/Astro/kernels/nep.bsp")


nowTime = datetime.datetime.now()
nowTimeString = str(nowTime)
#print(nowTimeString)
nowTime_et = spice.str2et(nowTimeString)
#print(nowTime_et)


#List all available frame ID'S and print their names

#for x in spice.bltfrm(-1):
#   print(x, spice.frmnam(x))

referanceFrame = "J2000"
target = "NEPTUNE"
observer = "SUN"

#Returns one way light time between the bodies
[MARSPosition, ltime] = spice.spkpos(target, nowTime_et, referanceFrame, 'NONE', observer)
    
def makePlanetPositionPlot(title, size=8, axisLimit=1.5e+08, sunSize=400):

    #Make the figure
    fig = plt.figure(figsize=(size, size))

    #Make sub plot
    axis3d = fig.add_subplot(111, projection='3d')

    #Set axis limits
    axis3d.set_xlim([-axisLimit*2, axisLimit*2])
    axis3d.set_ylim([-axisLimit*2, axisLimit*2])
    axis3d.set_zlim([-axisLimit*2, axisLimit*2])

    #Set axis labels
    axis3d.set_xlabel('X (km)')
    axis3d.set_ylabel('Y (km)')
    axis3d.set_zlabel('Z (km)')

    #Create the sun
    axis3d.scatter([0.0], [0.0], [0.0], s=sunSize, c="orange")

    #Add a title
    plt.title(title, y=1.025)
    
    #Return the plt
    return axis3d, fig

def addPlanetToPlot(axis3D, planetPosition, size, color):
    return axis3D.scatter([planetPosition[0]], [planetPosition[1]], [planetPosition[2]], s=size, c=color)

#Make the plot
axis3D, fig = makePlanetPositionPlot('MARSs position relative to the Sun')

#Add the earth
addPlanetToPlot(axis3D, MARSPosition, 40, 'red')

#Show the plot
plt.show()

times = [nowTime]
for i in range(1,100):
    times.append(nowTime + relativedelta(weeks = i))

#convert to et
etTimes = [spice.str2et(str(x)) for x in times]

#The SPK system returns the state of the target relative to the observer. 
#The computed position data point from the “observer” to the “target.”
#– The computed velocity is that of the “target” relative to the “observer.”
marsPositions = spice.spkpos(target, etTimes, referanceFrame, 'NONE', observer)[0]
print(marsPositions)
axis3D, fig = makePlanetPositionPlot('mars position relative to the Sun over 52 weeks')

#Add the data
for marsPosition in marsPositions:
    addPlanetToPlot(axis3D, marsPosition, 40, 'red')

#Show the plot
plt.show()