import numpy as np
from scipy.stats import expon as exponential

Q_LIMIT = 100
BUSY = 1
IDLE = 0

mean_interarrival = 0
mean_service = 0
num_delays_required = 0

def expon(mean):
    return exponential(scale=mean).rvs()

time_arrival = [0.0] * (Q_LIMIT + 1)
time_next_event = [0.0] * 3

def init():
    global sim_time, server_status, num_in_q, time_last_event, num_cust_delayed, total_of_delays, area_num_in_q, area_server_status
    sim_time = 0.0
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0
    num_cust_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0
    time_next_event[1] = sim_time + expon(mean_interarrival)
    time_next_event[2] = 1.0e+30

def timing():
    global sim_time, next_event_type
    min_time_next_event = 1.0e+29
    next_event_type = 0
    for i in range(1, num_events + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i
    if next_event_type == 0:
        print("Event list empty at time", sim_time)
        exit(1)
    sim_time = min_time_next_event

def update_time_avg_stats():
    global sim_time, time_last_event, area_num_in_q, area_server_status
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time

    area_num_in_q += num_in_q * time_since_last_event
    area_server_status += server_status * time_since_last_event

def arrive():
    global sim_time, num_in_q, server_status, num_cust_delayed, total_of_delays
    time_next_event[1] = sim_time + expon(mean_interarrival)
    if server_status == BUSY:
        num_in_q += 1
        if num_in_q > Q_LIMIT:
            print("Overflow of the array time arrival at time", sim_time)
            exit(2)
        time_arrival[num_in_q] = sim_time
    else:
        delay = 0.0
        total_of_delays += delay
        num_cust_delayed += 1
        server_status = BUSY
        time_next_event[2] = sim_time + expon(mean_service)

def depart():
    global sim_time, num_in_q, server_status, num_cust_delayed, total_of_delays
    if num_in_q == 0:
        server_status = IDLE
        time_next_event[2] = 1.0e+30
    else:
        num_in_q -= 1
        delay = sim_time - time_arrival[1]
        total_of_delays += delay
        num_cust_delayed += 1
        time_next_event[2] = sim_time + expon(mean_service)
        
        for i in range(1, num_in_q + 1):
            time_arrival[i] = time_arrival[i + 1]

def report():
    global sim_time, total_of_delays, num_cust_delayed, area_num_in_q, area_server_status
    outfile.write(f"\n\n Average delay in queue, {total_of_delays / num_cust_delayed}\n\n")
    outfile.write(f"Average number in queue, {area_num_in_q / sim_time}\n\n")
    outfile.write(f"Server utilization:, {area_server_status / sim_time}\n\n")
    outfile.write(f"Time Simulation ended, {sim_time}, minutes")

def main():
    global mean_interarrival, mean_service, num_delays_required, num_events
    with open("mm1.in ", "r") as infile:
        input_string = infile.readline()
    global outfile
    outfile = open("mm2.out", "w")
    num_events = 2
    values = input_string.split()
    mean_interarrival = float(values[0])
    mean_service = float(values[1])
    num_delays_required = int(values[2])
    outfile.write("Single-server queueing system:\n\n")
    outfile.write(f"Mean interarrival time minutes::{mean_interarrival} \n\n")
    outfile.write(f"Mean Service time: {mean_service}\n\n")
    outfile.write(f"Number of Customer: {num_delays_required}\n\n")
    init()
    while num_cust_delayed < num_delays_required:
        timing()
        update_time_avg_stats()
        if next_event_type == 1:
            arrive()
        elif next_event_type == 2:
            depart()
    report()
    infile.close()
    outfile.close()

if __name__ == "__main__":
    main()
