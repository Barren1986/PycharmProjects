import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Front End User Interface")

# Set the size of the window, use geometry method of the TK object
root.geometry("400x400") # width 400 x height 400

# Create a label widget
label = tk.Label(root, text="Hello World!")
label.pack()


# Run the application
root.mainloop()