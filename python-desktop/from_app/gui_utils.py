import tkinter as tk
from tkinter import messagebox
from db_utils import save_to_db

# Function to create the GUI
def create_gui():
    # Function to save the data from the form
    def save_data():
        # Collect data from fields
        data = (
            name_var.get(), email_var.get(), phone_var.get(), address_var.get(),
            city_var.get(), state_var.get(), zip_code_var.get(),
            country_var.get(), dob_var.get(), occupation_var.get()
        )
        # Save data to the database
        save_to_db(data)
        messagebox.showinfo("Success", "Data saved successfully!")
        clear_fields()

    # Function to clear the form fields
    def clear_fields():
        for var in [name_var, email_var, phone_var, address_var, city_var,
                    state_var, zip_code_var, country_var, dob_var, occupation_var]:
            var.set("")

    # Create the main window
    root = tk.Tk()
    root.title("Single-Page Form")
    root.geometry("400x600")

    # Field variables
    name_var = tk.StringVar()
    email_var = tk.StringVar()
    phone_var = tk.StringVar()
    address_var = tk.StringVar()
    city_var = tk.StringVar()
    state_var = tk.StringVar()
    zip_code_var = tk.StringVar()
    country_var = tk.StringVar()
    dob_var = tk.StringVar()
    occupation_var = tk.StringVar()

    # Form layout
    fields = [
        ("Name", name_var), ("Email", email_var), ("Phone", phone_var),
        ("Address", address_var), ("City", city_var), ("State", state_var),
        ("Zip Code", zip_code_var), ("Country", country_var),
        ("Date of Birth", dob_var), ("Occupation", occupation_var)
    ]

    for label, var in fields:
        tk.Label(root, text=label).pack(anchor="w", padx=10, pady=2)
        tk.Entry(root, textvariable=var).pack(fill="x", padx=10, pady=2)

    # Buttons
    tk.Button(root, text="Save", command=save_data).pack(side="left", padx=10, pady=20)
    tk.Button(root, text="Clear", command=clear_fields).pack(side="right", padx=10, pady=20)

    return root
