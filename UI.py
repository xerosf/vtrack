import tkinter as tk
from tkinter import Frame, Label
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("GitGud: Insights")
root.geometry("750x450")  # Optional: set window size

# Create a frame within the main window
frame = Frame(root, width=300, height=450, bg="white")
frame.pack(side="left", anchor="center")  # Adjust padding as necessary

# Load the image using Pillow
image_path = "res\\maps\\Bind.png"  # Replace with your image path
image = Image.open(image_path)

# Resize the image using the new resampling attribute
image = image.resize((300, 65), Image.Resampling.LANCZOS)

# Convert the image to a Tkinter-compatible photo image
photo_image = ImageTk.PhotoImage(image)

# Create a label widget to hold the image
image_label = Label(frame, image=photo_image)

# Place the label in the frame
image_label.pack()

# Run the Tkinter event loop
root.mainloop()