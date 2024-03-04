import numpy as np
from scipy.stats import expon as exponential

import random 
import math
Q_LIMIT=100
BUSY=1
IDLE=0

def expon(mean):
    # return an expon random sample from the exponential distr
    return exponential(scale=mean).rvs()

global next_event_type,num_cust_delayed,num_custs_delayed, num_delays_required, num_events,num_in_q, server_status,area_num_in_q, area_server_status, mean_interarrival, mean_service,sim_time,time_last_event,total_of_delays,infile,outfile

time_arrival=[0.0]*(Q_LIMIT+1)
time_next_event=[0.0]*3


# initialize function 
def init():
    # initialze simulation clock
    sim_time=0.0
    server_status=IDLE
    num_in_q=0
    time_last_event=0.0
    # init statistical counters
    num_cust_delayed=0
    total_of_delays=0.0
    area_num_in_q= 0.0
    area_server_status = 0.0
    '''init event lit. SInce no customers are present, the departure(service completion ) event is eliminated from considerarion '''
    time_next_event[1]=sim_time+expon(mean_interarrival)
    time_next_event[2]=1.0e+30

def timing():
    
    min_time_next_event=1.0e+29
    next_event_type=0
    #determine the event type of the next event to occur
    for i in range(1,num_events+1):
        if (time_next_event[i]<min_time_next_event):
            min_time_next_event=time_next_event[i]
            next_event_type=i
        # check to see whether the event list is empty
    if(next_event_type==0):
       # event list is empty ,so stop the simulation
        outfile.write(f"\n Event list empty at the time {sim_time}")
        exit(1)
    # the event list is not empty so advance the simulation clock
    sim_time=min_time_next_event

def update_time_avg_stats():
    pass

def arrive():
    # schedule the next arriival
    time_next_event[1]=sim_time+expon(mean_interarrival)
    # check if server is busy
    if(server_status==BUSY):
        # INCREMENT no of pple in the queue
        num_in_q+=1
        # check if an overfloe conditin exists
        if(num_in_q>Q_LIMIT):
            # queue has overflowed so stop the simulation
            outfile.write("\n Overflow of the array time arrival at \n")
            outfile.write("\n time: {sim_time}")
            exit(2)
        # there is still room in the queue
        time_arrival[num_in_q]=sim_time
    else:
        # idle server delay=0
        delay=0.0
        total_of_delays+=delay
        # increase the no of cuts delayed and maje server busy
        num_custs_delayed+=1
        server_status=BUSY
        # Schedule a departure service completion 
        time_next_event[2]=sim_time+expon(mean_service)

    

def depart():
    # check if teh queue is empty
    if(num_in_q==0):
        # make server IDLE an eliminate the departure(service completion) event from consideration
        server_status=IDLE
        time_next_event[2]=1.0e+30
    else:
        # the queue is non empty, so decrement the number of customers in the queue
        num_in_q-+1
        # compute delay of customer begining service
        delay =sim_time-time_arrival[1]
        total_of_delays+=delay
        # incrrememnt no of customers delayed and schedule departure
        num_custs_delayed+=1
        time_next_event[2]=sim_time+expon(mean_service)
        # move each customer if any up one place
        for i in range(1,num_in_q+1):
            time_arrival[i]=time_arrival[i+1]
def report():
    pass



def main():
    # open input and outputfile
    global infile
    with open("mm1.in ","r") as infile:
        # read
        input_string=infile.readline()
    global outfile
    outfile=open("mm2.out","w")
    # spectify the num of events for tehr timing function
    num_of_events=2
    # read the inputs of the input file
    values=input_string.split()
    
    mean_interarrival=values[0]
    mean_service=values[1]
    num_delays_required=values[2]

    # write the report filr
    outfile.write("Single-server queueing system:\n\n")
    outfile.write(f"Mean interarrival time minutes::{mean_interarrival} \n\n")
    outfile.write(f"Mean Service time: {mean_service}\n\n")
    outfile.write(f"Number of Customer: {num_delays_required}\n\n")
    # initialize simulation
    init()
    # run simulation while max delays are still needed
    while(num_cust_delayed<num_delays_required):
        # determine next event
        timing()
        # update time-average statistical accummulators
        update_time_avg_stats()
        # invoke the appropriate event function 
        if next_event_type==1:
            arrive()
            break
        elif next_event_type==2:
            depart()
            break
        else:
            break
    # invoke report Generator
    report()
    infile.close()
    outfile.close()
    


if __name__=="__main__":
    main()