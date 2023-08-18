import tkinter as tk


class customer:
    customer_list = []

    def __init__(self, name):
        self.name = name
        print("your name is :" + name)
        customer.customer_list.append(self)
        # for testing purposes , list storing all of the customer objects
        # for c in customer.customer_list:
        #     print(c.name)

    def hello(self):
        n = self.name
        print("Method call within class , your name is :" + n)

    def fncShowCustomerPanel(self):
        name = self.name
        print("fncshowcustomer panel print call :" + name)
        cust_frame = tk.LabelFrame(
            center_frame,
        )
