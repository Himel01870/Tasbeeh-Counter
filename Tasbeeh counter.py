import tkinter as tk

# Function to increment the counter
def increment():
    global count
    count += 1
    counter_label.config(text=str(count))

# Function to reset the counter
def reset():
    global count
    count = 0
    counter_label.config(text=str(count))

# Function to exit the application
def quit_app():
    root.destroy()

# Initialize the main window
root = tk.Tk()
root.title("Tasbeeh Counter")
root.geometry("300x200")

# Initialize the counter
count = 0

# Create and place a label to display the counter
counter_label = tk.Label(root, text="0", font=("Arial", 36), fg="green")
counter_label.pack(pady=20)

# Create and place the buttons
increment_button = tk.Button(root, text="Count", command=increment, font=("Arial", 14), bg="lightblue")
increment_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 14), bg="lightcoral")
reset_button.pack(pady=5)

quit_button = tk.Button(root, text="Quit", command=quit_app, font=("Arial", 14), bg="lightgray")
quit_button.pack(pady=5)

# Run the application
root.mainloop()
