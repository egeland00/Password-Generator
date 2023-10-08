import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import ttkbootstrap as ttkbs
from ttkbootstrap import *
from password_functions import generate_password

def main():
    # Create main window
    root = ttkbs.Window(themename="darkly")
    root.title("Password Generator")
    root.geometry("900x500")

    # Load the image
    logo_image = PhotoImage(file="logo1.png")

    # Display the image in a Label
    logo = ttk.Label(root, image=logo_image)
    logo.pack(pady=20)

    header = ttk.Label(root, text="Password Generator", font=("Helvetica", 20))
    header.pack(pady=20)

    def copy_to_clipboard(event=None):
        """Copy the current password to the clipboard and show a 'Copied!' message."""
        # Backup the current password
        current_password = password_var.get()
        
        # Copy the password to the clipboard
        root.clipboard_clear()  # Clear the current clipboard contents
        root.clipboard_append(current_password)  # Add the password to the clipboard
        root.update()  # This is necessary to finalize the clipboard update
        
        # Update the display to show "Copied!"
        password_display.config(foreground="lightgreen")
        password_var.set("Copied!")
        
        # Reset the display back to the password after 1.5 seconds (1500 milliseconds)
        root.after(1500, lambda: password_var.set(current_password))

    # Password Display
    password_var = ttkbs.StringVar()
    password_var.set("Password will appear here")  # initial text
    
    password_display = ttkbs.Label(root, textvariable=password_var, bootstyle="warning", font=("Helvetica", 14))
    password_display.pack(pady=20)
    
    # Generate Password Button
    generate_btn = ttkbs.Button(root, bootstyle="success", text="Generate Password")
    generate_btn.pack(pady=20)
    password_display.bind("<Button-1>", copy_to_clipboard)  # Bind the copy_to_clipboard function to the password_display Label
    
    # Checkboxes
    checkboxes_frame = ttkbs.Frame(root)
    checkboxes_frame.pack(padx=20, anchor="w")
    
    symbols_var = ttkbs.BooleanVar()
    numbers_var = ttkbs.BooleanVar()
    capitals_var = ttkbs.BooleanVar()

    symbols_chk = ttkbs.Checkbutton(checkboxes_frame, bootstyle="success", text="Symbols", variable=symbols_var)
    numbers_chk = ttkbs.Checkbutton(checkboxes_frame, bootstyle="success", text="Numbers", variable=numbers_var)
    capitals_chk = ttkbs.Checkbutton(checkboxes_frame, bootstyle="success", text="Capital Letters", variable=capitals_var)
    
    symbols_chk.pack(anchor="w")
    numbers_chk.pack(anchor="w")
    capitals_chk.pack(anchor="w")
    
    def update_slider_value(val):
        slider_value.set(f"Character Length: {int(float(val))}")


    # Text above the slider
    password_length_label = ttkbs.Label(root, text="Password Length")
    password_length_label.pack(pady=10)

    # Slider
    length_slider = ttkbs.Scale(root, bootstyle="success", from_=0, to=100, orient="horizontal", length=100, command=update_slider_value)
    length_slider.set(50)  # set initial value
    length_slider.pack(pady=10)

    # Dynamic label to show the current slider value
    slider_value = ttkbs.StringVar()
    slider_value.set(f"Length: {length_slider.get()}")  # set the initial value
    slider_value_label = ttkbs.Label(root, textvariable=slider_value)
    slider_value_label.pack(pady=10)

    def on_generate_click():
        # Retrieve the values from GUI elements
        length = int(length_slider.get())  # convert to int
        use_symbols = symbols_var.get()
        use_numbers = numbers_var.get()
        use_capitals = capitals_var.get()
        
        # Call the generate_password function
        generated_password = generate_password(length, use_symbols, use_numbers, use_capitals)

        # Display the generated password in the GUI
        password_var.set(generated_password)

    # Link the on_generate_click function to the "Generate Password" button:
    generate_btn.config(command=on_generate_click)
    
    root.mainloop()

if __name__ == "__main__":
    main()