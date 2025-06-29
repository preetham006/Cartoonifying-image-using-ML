import tkinter as tk
from tkinter import filedialog, Button, Label
import cv2
import os
import random
from PIL import ImageTk, Image

# Cartoonifier function
def make_cartoon(file_path):
    img = cv2.imread(file_path)
    
    # Get the edges
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    
    # Color smoothing
    color = cv2.bilateralFilter(img, 9, 300, 300)
    
    # Combine edges and color for cartoon effect
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    return cartoon

# Function to save the cartoon image
def save_cartoon(file_path, cartoon_img):
    where = filedialog.asksaveasfilename(filetypes=(('JPEG Files', '.jpg'), ('PNG Files', '.png'), ('All Files', '.')), defaultextension=file_path)
    cartoon_img.save(where)

# Show the save button
def show_save_button(file_path, cartoon_img):
    save_b = Button(top, text='Save to computer', command=lambda: save_cartoon(file_path, cartoon_img), padx=10, pady=5)
    save_b.place(relx=0.69, rely=0.86)

# Function to apply cartoon effect and display the result
def convert(file_path):
    cartoon = make_cartoon(file_path)
    cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
    cartoon_img = Image.fromarray(cartoon)
    cartoon_img.thumbnail((top.winfo_width() / 1.8, top.winfo_height() / 1.8))
    im = ImageTk.PhotoImage(cartoon_img)
    label = Label(top, image=im)
    label.image = im
    label.pack(side="right", expand='yes')
    show_save_button(file_path, cartoon_img)
    
    # Hide the Cartoonify button after click
    convert_b.place_forget()

# Show button to start cartoonification
def show_convert_button(file_path):
    global convert_b
    convert_b = Button(top, text="Cartoonify me", command=lambda: convert(file_path), padx=10, pady=5)
    convert_b.place(relx=0.79, rely=0.46)

# Function to randomly select an image from a directory
def select_random_image():
    # Choose a directory containing images
    directory = filedialog.askdirectory()
    if not directory:
        return
    
    # Get list of all image files in the directory
    image_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.jpg', '.png', '.jpeg'))]
    
    if image_files:
        file_path = random.choice(image_files)
        display_image(file_path)

# Function to upload and display image
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        display_image(file_path)

# Function to display selected image
def display_image(file_path):
    uploaded = Image.open(file_path)
    uploaded.thumbnail((top.winfo_width() / 2.25, top.winfo_height() / 2.25))
    im = ImageTk.PhotoImage(uploaded)
    label = Label(top, image=im)
    label.image = im
    label.pack(side="left", expand='yes')
    show_convert_button(file_path)

# Initialize the GUI
top = tk.Tk()
top.geometry('1000x600')
top.title('Cartoonifier')
top.configure(background='white')

# Center the "Upload an image" button
upload_button = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
upload_button.configure(background='#add8e6', foreground='white', font=('arial', 10, 'bold'))
upload_button.place(relx=0.5, rely=0.86, anchor='center')

# Run the GUI main loop
top.mainloop()
