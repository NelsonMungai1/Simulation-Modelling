import numpy as np
from scipy.stats import expon as exponential


Q_LIMIT=100
BUSY=1
IDLE=0

#init some values
mean_interarrival=0
mean_service=0
num_delays_required=0

# an array of arrivaltime initialized to 0
time_arrival=[0.0]*(Q_LIMIT+1)
time_next_event=[0.0]*3

# function to generate random values exponentially distributed
def expon(mean):
    # return an expon random sample from the exponential distr
    return exponential(scale=mean).rvs()

# initialize function 
def init():
    # global sim_time, server_status, num_in_q, time_last_event,num_cust_delayed, total_of_delays, area_num_in_q, area_server_status
    global sim_time, server_status, num_in_q, time_last_event, num_cust_delayed, total_of_delays, area_num_in_q, area_server_status

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
    '''init event list. Since no customers are present, the departure(service completion ) event is eliminated from considerarion '''
    time_next_event[1]=sim_time+expon(mean_interarrival)
    time_next_event[2]=1.0e+30

def timing():
    global sim_time,next_event_type
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
    global time_last_event ,area_num_in_q,area_server_status
    time_since_last_event=sim_time-time_last_event
    time_last_event=sim_time

    # update area under number-in-queue function
    area_num_in_q+=num_in_q*time_since_last_event
    # update area under server-busy indicator funcrion
    area_server_status+=server_status*time_since_last_event

def arrive():
    global sim_time, num_in_q, server_status, num_cust_delayed, total_of_delays
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
            outfile.write(f"\n time: {sim_time}")
            exit(2)
        # there is still room in the queue
        time_arrival[num_in_q]=sim_time
    else:
        # idle server delay=0
        delay=0.0
        total_of_delays+=delay
        # increase the no of cuts delayed and maje server busy
        num_cust_delayed+=1
        server_status=BUSY
        # Schedule a departure service completion 
        time_next_event[2]=sim_time+expon(mean_service)

    

def depart():
    global sim_time, num_in_q, server_status, num_cust_delayed, total_of_delays
    # check if teh queue is empty
    if(num_in_q==0):
        # make server IDLE and eliminate the departure(service completion) event from consideration
        server_status=IDLE
        # make time of next departure inifinitely big
        time_next_event[2]=1.0e+30
    else:
        # the queue is non empty, so decrement the number of customers in the queue
        num_in_q-=1
        # compute delay of customer begining service
        delay =sim_time-time_arrival[1]
        total_of_delays+=delay
        # incrememnt no of customers delayed and schedule departure
        num_cust_delayed+=1
        time_next_event[2]=sim_time+expon(mean_service)
        # move each customer if any up one place
        for i in range(1,num_in_q+1):
            time_arrival[i]=time_arrival[i+1]
def report():
    global sim_time, total_of_delays, num_cust_delayed, area_num_in_q, area_server_status
    # compute and write estimates of desired measures of performance
    outfile.write(f"\n\n Average delay in queue {(total_of_delays/num_cust_delayed):.4f}\n\n")
    outfile.write(f"Average number in queue {(area_num_in_q/sim_time):4f}\n\n")
    outfile.write(f"Server utilization: {(area_server_status/sim_time):.4f}\n\n")
    outfile.write(f"Time Simulation ended {(sim_time):.4f} minutes")



def main():
    global mean_interarrival,mean_service,num_delays_required,num_events
    with open("mm1.in","r") as infile:
        # read
        input_string=infile.readline()
    global outfile
    outfile=open("mm2.out","w")
    # spectify the num of events for the timing function
    num_events=2
    # read the inputs of the input file
    values=input_string.split()
    
    mean_interarrival=float(values[0])
    mean_service=float(values[1])
    num_delays_required=int(values[2])

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
        elif next_event_type==2:
            depart()
    # invoke report Generator
    report()
    infile.close()
    outfile.close()
    


if __name__=="__main__":
    main()