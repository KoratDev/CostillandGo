from tkinter import ttk
from tkinter import *
import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "mayo140501",
            db = ""
        )

        self.cursor = self.connection.cursor()

        print("Conexión establecida exitosamente.")

database = DataBase

class Application:

    def __init__(self, window):
        self.wind = window
        self.wind.title("Application")
        # add new order botton
        self.new_order = ttk.Button(self.wind, text = "New order", command = self.add_order)
        self.new_order.grid(row = 0, column = 1, padx = 5, pady = 5)
        # add new product botton
        self.new_product = ttk.Button(self.wind, text = "New product", command = self.add_product)
        self.new_product.grid(row = 0, column = 2, padx = 5, pady = 5)
        # add new client botton
        self.new_client = ttk.Button(self.wind, text = "New customer", command = self.add_customer)
        self.new_client.grid(row = 0, column = 3, padx = 5, pady = 5)
        # Table
        self.order_table = ttk.Treeview(self.wind, height = 20, columns = ("#1", "#2", "#3", "#4", "#5", "#6"))
        self.order_table.grid(row = 1, column = 0, columnspan = 10, padx = 5, pady = 5)
        self.order_table.heading("#0", text = "Order")
        self.order_table.heading("#1", text = "Product")
        self.order_table.heading("#2", text = "Customer information")
        self.order_table.heading("#3", text = "Total to pay")
        self.order_table.heading("#4", text = "Status")
        self.order_table.heading("#5", text = "Date")
        self.order_table.heading("#6", text = "Changes")
        # Table size
        self.order_table.column("#0", width = 60)
        self.order_table.column("#1", width = 100)
        self.order_table.column("#3", width = 110)
        self.order_table.column("#4", width = 80)
        self.order_table.column("#5", width = 90)
        self.order_table.column("#6", width = 110)

    # Order window
    def add_order(self):
        self.add_order_wind = Toplevel()
        self.add_order_wind.title("New order")

    # Product window
    def add_product(self):
        self.add_product_wind = Toplevel()
        self.add_product_wind.title("New product")
        # Add and edits products | Container
        self.new_product_frame = ttk.LabelFrame(self.add_product_wind, text = "Product name")
        self.new_product_frame.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 20)
        # Name input
        self.name = ttk.Label(self.new_product_frame, text = "Name: ").grid(row = 1, column = 0)
        self.name = ttk.Entry(self.new_product_frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1, columnspan = 3, padx = 5, pady = 5)
        # Price input
        self.price = ttk.Label(self.new_product_frame, text = "Price: ").grid(row = 2, column = 0)
        self.price = ttk.Entry(self.new_product_frame)
        self.price.grid(row = 2, column = 1, padx = 5, pady = 5)
        # Botton add product
        self.add_button = ttk.Button(self.new_product_frame, text = "Add product").grid(row = 3, columnspan = 3, sticky = W + E, pady = 5)
        # Product table
        self.product_table = ttk.Treeview(self.add_product_wind, height = 10, columns = ("#1", "#2"))
        self.product_table.grid(row = 5, column = 0, columnspan = 2)
        self.product_table.heading("#0", text = "Id")
        self.product_table.column("#0", width = 50)
        self.product_table.heading("#1", text = "Product")
        self.product_table.heading("#2", text = "Price")

    # Customer window
    def add_customer(self):
        self.add_customer_wind = Toplevel()
        self.add_customer_wind.title("New customer")
        # Add and edits customers
        self.new_customer_frame = ttk.LabelFrame(self.add_customer_wind, text = "New customer")
        self.new_customer_frame.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 20)
        # Name input
        self.name = ttk.Label(self.new_customer_frame, text = "Name: ").grid(row = 1, column = 0)
        self.name = ttk.Entry(self.new_customer_frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1, columnspan = 3, padx = 5, pady = 5)
        # Phone number input
        self.phone = ttk.Label(self.new_customer_frame, text = "Phone number: ").grid(row = 2, column = 0)
        self.phone = ttk.Entry(self.new_customer_frame)
        self.phone.grid(row = 2, column = 1, columnspan = 3, padx = 5, pady =5)
        # Shipping address input
        self.shipping_address = ttk.Label(self.new_customer_frame, text = "Shipping address: ").grid(row = 3, column = 0)
        self.shipping_address = ttk.Entry(self.new_customer_frame)
        self.shipping_address.grid(row = 3, column = 1, columnspan = 3, padx = 5, pady = 5)
        # Botton add customer
        self.add_button = ttk.Button(self.new_customer_frame, text = "Add customer").grid(row = 4, columnspan = 4, sticky = W + E, pady = 5)
        # Customer table
        self.customer_table = ttk.Treeview(self.add_customer_wind, height = 10, columns = ("#1", "#2", "#3"))
        self.customer_table.grid(row = 6, column = 0, columnspan = 3)
        self.customer_table.heading("#0", text = "Id")
        self.customer_table.column("#0", width = 50)
        self.customer_table.heading("#1", text = "Customer name")
        self.customer_table.heading("#2", text = "Phone number")
        self.customer_table.heading("#3", text = "Shipping address")

window = Tk()
root = Application(window)
window.mainloop()
