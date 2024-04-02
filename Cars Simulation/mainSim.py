import turtle
from turtle import Screen
from tkinter import *
import math 
import vehicles
import random 
# import project modules
import flower
# import drawSUV
# import drawTruck
# import drawCar

def main():
    screen=Screen()

    canvas=screen.getcanvas()

    car_button=Button(canvas.master,text="CAR",width=5,height=1,bg="blue",fg="white",font=("Arial",12),command=None)
    suv_button=Button(canvas.master,text="SUV",width=5,height=1,bg="green",fg="white",font=("Arial",12),command=None)
    truck_button=Button(canvas.master,text="Truck",width=5,height=1,bg="red",fg="white",font=("Arial",12),command=None)

    car_button.pack()
    car_button.place(x=500,y=50)

    suv_button.pack()
    suv_button.place(x=600,y=50)

    truck_button.pack()
    truck_button.place(x=700,y=50)


    flower.main()

if __name__=="__main__":
    main()