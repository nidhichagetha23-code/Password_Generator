import tkinter as tk
import random

def generate():
    name = name_entry.get()
    dob = dob_entry.get()
    
    special = ['@', '#', '$', '!']
    
    passwords = ""
    for i in range(5):
        pw = name[:3] + random.choice(special) + dob[-4:] + str(random.randint(100,999))
        passwords += pw + "\n"
    
    result_label.config(text=passwords)

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Enter DOB").pack()
dob_entry = tk.Entry(root)
dob_entry.pack()

tk.Button(root, text="Generate Password", command=generate).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()