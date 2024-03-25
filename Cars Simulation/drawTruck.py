import tkinter as tk

def draw_lorry(canvas):
    # Draw truck body
    canvas.create_rectangle(50, 150, 250, 250, fill="blue")

    # Draw truck cabin
    canvas.create_rectangle(200, 100, 300, 150, fill="red")

    # Draw windows on the cabin
    canvas.create_rectangle(210, 110, 240, 140, fill="white")
    canvas.create_rectangle(260, 110, 290, 140, fill="white")

    # Draw truck wheels
    canvas.create_oval(75, 225, 125, 275, fill="black")
    canvas.create_oval(225, 225, 275, 275, fill="black")

# Create the main window
root = tk.Tk()
root.title("Lorry Truck")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=350, height=300)
canvas.pack()

# Draw the lorry truck
draw_lorry(canvas)

# Run the Tkinter event loop
root.mainloop()
