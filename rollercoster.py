import tkinter as tk
from tkinter import messagebox

def calculate_bill():
    try:
        height = int(height_var.get())
    except:
        messagebox.showerror("Error", "Please enter a valid height!")
        return

    bill = 0

    if height < 160:
        messagebox.showinfo("Result", "Sorry, you must be at least 120 cm to ride.")
        return

    try:
        age = int(age_var.get())
    except:
        messagebox.showerror("Error", "Please enter a valid age!")
        return

    # Age pricing
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif 45 <= age <= 55:
        messagebox.showinfo("Special Offer", "Everything is going to be ok.\nHave a safe ride on us ❤️")
        bill = 0
    else:
        bill = 12

    # Photo
    if photo_var.get() == "Y":
        bill += 3

    messagebox.showinfo("Final Bill", f"Your total bill is: ${bill}")

# WINDOW
root = tk.Tk()
root.title("Rollercoaster Ride Checker")
root.geometry("500x550")
root.config(bg="#0D0D0D")   # Black background

# MAIN FRAME
frame = tk.Frame(root, bg="#1A1A1A", bd=3, relief="ridge")
frame.pack(padx=30, pady=30, fill="both", expand=True)

# TITLE
tk.Label(frame, text="Rollercoaster Ride Checker", 
         font=("Arial", 20, "bold"), fg="red", bg="#1A1A1A").pack(pady=15)


# HEIGHT SECTION
tk.Label(frame, text="Enter Your Height (cm):", 
         font=("Arial", 14, "bold"), fg="green", bg="#1A1A1A").pack(pady=5)

height_var = tk.StringVar()
tk.Entry(frame, textvariable=height_var, font=("Arial", 14), width=15).pack(pady=5)


# AGE SECTION
tk.Label(frame, text="Enter Your Age:", 
         font=("Arial", 14, "bold"), fg="green", bg="#1A1A1A").pack(pady=5)

age_var = tk.StringVar()
tk.Entry(frame, textvariable=age_var, font=("Arial", 14), width=15).pack(pady=5)


# PHOTO OPTION
tk.Label(frame, text="Do you want a photo taken?", 
         font=("Arial", 14, "bold"), fg="green", bg="#1A1A1A").pack(pady=10)

photo_var = tk.StringVar(value="N")

tk.Radiobutton(frame, text="Yes", variable=photo_var, value="Y",
               font=("Arial", 12, "bold"), fg="white", bg="#1A1A1A",
               selectcolor="red").pack(anchor="w", padx=30)

tk.Radiobutton(frame, text="No", variable=photo_var, value="N",
               font=("Arial", 12, "bold"), fg="white", bg="#1A1A1A",
               selectcolor="red").pack(anchor="w", padx=30)


# BUTTON
btn = tk.Button(frame, text="CHECK & CALCULATE BILL", command=calculate_bill,
                font=("Arial", 16, "bold"), bg="red", fg="white", padx=15, pady=8)
btn.pack(pady=25)


root.mainloop()