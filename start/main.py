import tkinter as tk
import utils
import customer


def fncChecklogin():
    username = login_frame_username_register_field.get()
    password = login_frame_label_password_register_field.get()
    print(f"User and password: {username}{password}")
    if username == "" and password == "":
        login_frame.pack_forget()
        # root.configure(bg="pink")
        user_frame.pack()
        print("login frame to user frame")


def fncNewCustomer():
    print("hello world")
    print("~~~~~~~~~~~~")

    center_frame.pack_forget()
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


def fncCalander():
    print("Hello calander")
    print("~~~~~~~~~~~~~~~~")


root = tk.Tk()
root.title("creating multiple pages")
root.geometry("1920x1080")
# root.configure(bg="orange")

# login frame!


login_frame = tk.Frame(root, bg="grey")
login_frame.grid(row=0, column=0, padx=20, pady=10)

login_frame_label_username = tk.Label(login_frame, text="Username", bg="grey")
login_frame_username_register_field = tk.Entry(login_frame)

login_frame_label_username.grid(row=0, column=0)
login_frame_username_register_field.grid(row=0, column=1)

login_frame_label_password = tk.Label(login_frame, text="Password", bg="grey")
login_frame_label_password.grid(row=1, column=0)

login_frame_label_password_register_field = tk.Entry(login_frame)
login_frame_label_password_register_field.grid(row=1, column=1)

login_submit_button = tk.Button(login_frame, text="submit", command=fncChecklogin)
login_submit_button.grid(row=3, column=0, columnspan=2, sticky="news")

for widget in login_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

login_frame.pack()
login_frame.place(x=900, y=300)

# user frame !!!!!!!!!!!!!!!!!!!!!!!!!!
user_frame = tk.Frame(root, bg="white", height=1080, width=1920)

# navbar

navbar_frame = tk.Frame(
    user_frame, bg="grey", height=utils.height_prct(10), width=utils.width_prct(100)
)
navbar_frame.place(x=0, y=0)

# creating a grid frame to hold buttons in navbar
navbar_nav_btn_list = tk.Frame(
    navbar_frame, bg="orange", height=utils.height_prct(10), width=utils.width_prct(100)
)
navbar_nav_btn_list.place(x=0, y=0)


# first button in navbar
# btn_create_customer = tk.Button(
#     navbar_nav_btn_list,
#     text="New customer",
#     command=customer.fncNewCustomer(frame=center_frame),
# )
# btn_create_customer.place(x=utils.width_prct(15), y=utils.height_prct(7))
# side bar

sidebar_frame = tk.Frame(
    user_frame, bg="pink", height=utils.height_prct(90), width=utils.width_prct(15)
)
sidebar_frame.place(x=0, y=utils.height_prct(10))

# CENTER FRAME IN USER FRAME

center_frame = tk.Frame(
    user_frame, bg="yellow", height=utils.height_prct(90), width=utils.width_prct(85)
)
center_frame.place(x=utils.width_prct(15), y=utils.height_prct(10))

btn_create_customer = tk.Button(
    navbar_nav_btn_list,
    text="New customer",
    command=fncNewCustomer(),
)
btn_create_customer.place(x=utils.width_prct(15), y=utils.height_prct(7))

btn_calender = tk.Button(
    navbar_nav_btn_list,
    text="Calender",
    command=fncCalander,
)
btn_calender.place(x=utils.width_prct(20), y=utils.height_prct(7))

# trying to place code in is going to be a bitch! we need to find a way to use grid within the center frame
# otherwise its going to be a nightmare trying to line everything up with different sizes
# #customer_name_label = tk.Label(
#     center_frame,
#     text="New customer",
#     padx=10,
#     pady=10,
# )
# #customer_name_label.place(x=0, y=0)

# # customer_name_entry = tk.Entry(center_frame, width=20)
# # customer_name_entry.place(x=utils.width_prct(5), y=0)


# customer_entry_labelframe = tk.LabelFrame(center_frame, text="New Customer")
# customer_entry_labelframe.grid(
#     row=0,
#     column=0,
# )

# customer_entry_label = tk.Label(customer_entry_labelframe, text="First name :")
# customer_entry_label.grid(row=0, column=0)

# customer_entry_register_field = tk.Entry(customer_entry_labelframe)
# customer_entry_register_field.grid(row=0, column=1)

# customer_submitbutton = tk.Button(customer_entry_labelframe)
# customer_submitbutton.grid(row=0, column=2)

root.mainloop()
