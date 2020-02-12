from numpy import *
import numpy as np 
from matplotlib import pyplot as plt
import sys
import csvreader


#print the numpy array without truncation
np.set_printoptions(threshold=sys.maxsize)

#outtimes = [(508,509),(573,578),(629,633),(714,717),(743,765)]
#r1 ~ employee name
#r1 = [(508,509),(573,578),(629,633),(714,717),(743,765)]
#r2 = [(508,509),(573,578),(629,633)]
#r3 = [(508,509),(573,578)]
#r4 = [(508,509)]
#employee_data = [r1,r2,r3,r4]

employee_data = csvreader.e_data
print(employee_data)

#1 degree = 4 min, for 24 hour scale
r = zeros([360*4])
theta = np.arange(0,2*np.pi,2*np.pi/1440)
width = np.pi*2/1440

#bar_height = zeros([1440])

#create a list of empty strings where the length of the list = total number of bars(i.e = 1440)
timespan_label=[]
for i in range(0,1440):
    timespan_label.append('')

def plot(outtimes):
    
    total_outtime = 0
    outtime_durations = []
    for j in outtimes:
        delta = j[1] - j[0]
        total_outtime = total_outtime + delta
        outtime_durations.append(delta)
        for i in range(j[0],j[1]+1):
            bar_height[i] = delta
            
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_axes([0.1, 0.1, 0.75, 0.79], polar=True)
    ax = plt.subplot(111, projection='polar')
    ax.set_theta_zero_location("S")
    ax.set_theta_direction(-1) #now it is clockwise
    ax.grid(False)
    ax.spines['polar'].set_visible(True) #shows the outer circle
    ax.set_yticklabels([])      #removes the y-tick labels( i.e bar heights)
    
    #arrange the grid like a clock
    time_label = ["0:00", "3:00", "6:00", "9:00", "12:00", "15:00", "18:00", "21:00"]
    lines, labels = plt.thetagrids(range(0, 360, int(360/len(time_label))), (time_label))
    plt.title("EBM snacks App \n River,Date: 6th Feb, 2020")
    
    num_outtimes = len(outtimes)
    textstr = "Total out time = {} min, {} times".format(total_outtime, num_outtimes)
    plt.gcf().text(0.3, 0.02, textstr, fontsize=14)
    
    
    bars = ax.bar(theta, bar_height, width=width, bottom=0.0, alpha = 0.8) #edgecolor = "k"
    ax.set_ylim(0, min(outtime_durations))
    
    #below block of code is udes to save the full screen figure generated
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    
    fig = plt.gcf()  #gcf =get current frame
    
    fig.savefig('%s.png' %(name)) #, bbox_inches='tight', dpi=1000
    #define this name during the plot function call.it will be inherited here.


    '''
    for h in range(0,len(employee_data)):
        print(o)
        fig.savefig('%s.png' %(h)) #, bbox_inches='tight', dpi=1000
        #plt.show()
    '''

for data in employee_data:
    bar_height = zeros([1440])
    print(data)
    name = str(len(data)) #this name will be inherited to into the funtion call.
    plot(data)
    bar_height = zeros([1440])




        
