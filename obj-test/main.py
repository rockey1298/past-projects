import tkinter as tk


root = tk.Tk()
root.title("Main page - here we go ")
root.geometry("600x600")


class Elder:
    def __init__(self, master):
        login_frame = tk.Frame(master, bg="orange")
        login_frame.grid(row=0, column=0, padx=20, pady=10)

        login_frame_label_username = tk.Label(login_frame, text="Username", bg="grey")
        login_frame_username_register_field = tk.Entry(login_frame)

        login_frame_label_username.grid(row=0, column=0)
        login_frame_username_register_field.grid(row=0, column=1)

        login_frame_label_password = tk.Label(login_frame, text="Password", bg="grey")
        login_frame_label_password.grid(row=1, column=0)

        login_frame_password_register_field = tk.Entry(login_frame)
        login_frame_password_register_field.grid(row=1, column=1)

        login_submit_button = tk.Button(
            login_frame,
            text="submit",
            command=fncCheckLogin(
                login_frame_username_register_field.get(),
                login_frame_password_register_field.get(),
            ),
        )
        login_submit_button.grid(row=3, column=0, columnspan=2, sticky="news")

        for widget in login_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        login_frame.pack()
        login_frame.place(x=0, y=0)

    def fncCheckLogin(lo, la):
        username = lo
        password = la
        print(f"User and password: {username}{password}")
        if username == "" and password == "":
            pass


e = Elder(root)


root.mainloop()
