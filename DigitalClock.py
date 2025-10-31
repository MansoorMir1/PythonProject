import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("🕒 Digital Clock")
root.geometry("500x200")  # Set default size
root.resizable(False, False)  # Prevent resizing
root.configure(bg="black")  # Background color
root.attributes('-fullscreen', True)


# Function to update time
def time():
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime('%A, %B %d, %Y')
    
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    
    # Call this function again after 1000 ms (1 second)
    clock_label.after(1000, time)

# Create and style clock label
clock_label = tk.Label(root, font=('calibri', 60, 'bold'), background='black', foreground='cyan')
clock_label.place(relx=0.5, rely=0.45, anchor='center')

# Create and style date label
date_label = tk.Label(root, font=('calibri', 20), background='black', foreground='white')
date_label.place(relx=0.5, rely=0.60, anchor='center')


# Start the clock
time()

# Allow user to exit fullscreen with Escape key
root.bind("<Escape>", lambda event: root.destroy())

# Run the application
root.mainloop()
