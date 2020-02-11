from numpy import *
import numpy as np
from matplotlib import pyplot as plt
import sys

np.set_printoptions(threshold=sys.maxsize) #print the numpy array without truncation



#1 degree = 4 min, for 24 hour scale
r=zeros([360*4])

#theta=arange(0,2*pi,2*pi/1440) #works, but lets use numpy
theta=np.arange(0,2*np.pi,2*np.pi/1440)
width = pi*2/1440

radiii = zeros([1440])

#create a list of empty strings where the length of the list = 1440
timespan_label=[]
for i in range(0,1439):
    timespan_label.append('')



#employees = []
#r1 = [(508,509),(573,578),(629,633),(714,717),(743,765)]
#r2 = [(508,509),(573,578),(629,633),(714,717),(743,765)]
#r3 = [(508,509),(573,578),(629,633),(714,717),(743,765)]
#r4 = [(508,509),(573,578),(629,633),(714,717),(743,765)]

outtimes = [r1,r2,r3,r4]
for k in range (0,len(outtimes)):
    print(k)
    for j in outtimes[k]:
        for i in range(j[0],j[1]+1):
            radiii[i] = j[1]-j[0]
            
            total_outtime = 0
            outtime_durations=[]
            for x in outtimes[0]:
                delta = (x[1]-x[0])
                
                total_outtime = total_outtime + delta

                
                outtime_durations.append(delta)
                
                timespan_label_number = x[0]+(delta//2)
                timespan_label[timespan_label_number] = str(delta)
                #timespan_label.append(str(timespan_label_number))

#print(timespan_label)
print(outtime_durations)
            
fig = plt.figure(figsize=(6,6))
ax = fig.add_axes([0.1, 0.1, 0.75, 0.79], polar=True)
ax = plt.subplot(111, projection='polar')
ax.set_theta_zero_location("S")
ax.set_theta_direction(-1) #now it is clockwise

ax.grid(False)
ax.spines['polar'].set_visible(True) #shows the outer circle
ax.set_yticklabels([])      #removes the y-tick labels( i.e bar heights)

#Arrange the grid into number of sales equal parts in degrees
time_label = ["0:00", "3:00", "6:00", "9:00", "12:00", "15:00", "18:00", "21:00"]
lines, labels = plt.thetagrids(range(0, 360, int(360/len(time_label))), (time_label))
#ax.set_xticks(theta)
#plt.thetagrids['grid.color'] = "deeppink"

plt.title("EBM snacks App \n River,Date: 6th Feb, 2020")

num_outtimes=len(outtimes)
textstr="Total out time = {} min, {} times".format(total_outtime,num_outtimes)
plt.gcf().text(0.3, 0.02, textstr, fontsize=14)


bars = ax.bar(theta, radiii, width=width, bottom=0.0, alpha = 0.8) #edgecolor = "k"
ax.set_ylim(0, min(outtime_durations))

#plt.axis('off') #removes the circle and labels

#getting labels for each timeout stick at the periphery of the circle.
#below block of code is udes to save the full screen figure generated
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()

fig = plt.gcf()  #gcf =get current frame
fig.savefig('ebm_snacks.png', dpi=1000) #, bbox_inches='tight'
plt.show()

'''
#rotations = np.rad2deg(theta)
#for x, bar, rotation, label in zip(theta, bars, rotations, timespan_label ):
   # lab = ax.text(x,min(outtime_durations)+0.05 , label, 
       #      ha='left', va='center', rotation=rotation, rotation_mode="anchor")
'''