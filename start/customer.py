import tkinter as tk


def fncNewCustomer(center_frame):
    print("hello world")
    print("~~~~~~~~~~~~")
    f = center_frame
    f.pack_forget()
    customer_entry_labelframe = tk.LabelFrame(center_frame, text="New Customer")
    customer_entry_labelframe.grid(
        row=0,
        column=0,
    )

    customer_entry_label = tk.Label(customer_entry_labelframe, text="First name :")
    customer_entry_label.grid(row=0, column=0)

    customer_entry_register_field = tk.Entry(customer_entry_labelframe)
    customer_entry_register_field.grid(row=0, column=1)

    customer_submitbutton = tk.Button(customer_entry_labelframe)
    customer_submitbutton.grid(row=0, column=2)  # #
