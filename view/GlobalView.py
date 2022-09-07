import tkinter as tk
from tkinter import ttk


class GlobalView(tk.Tk):
    """Globalview class shown after login with TKinter

    :param tk: TK superclass
    :type tk: TK
    """

    def __init__(self, master=None) -> None:
        """Constructor

        :param master: main TK windows, defaults to None
        :type master: TK, optional
        """

        self.main_window = tk.Toplevel(master)
        self.main_window.title("Hotel check-in APP: Global")

        self.category_btn = tk.Button(
            self.main_window, text="Categories", width=10)
        self.category_btn.grid(row=0, column=0)

        self.rooms_btn = tk.Button(self.main_window, text="Rooms", width=10)
        self.rooms_btn.grid(row=0, column=1)

        self.guest_btn = tk.Button(self.main_window, text="Guests", width=10)
        self.guest_btn.grid(row=0, column=2)

        self.reservations_btn = tk.Button(
            self.main_window, text="Reservations", width=10)
        self.reservations_btn.grid(row=0, column=3)

        self.tree_table = ttk.Treeview(self.main_window)
        self.tree_table['columns'] = (
            'Name', 'Lastname', 'Age', 'Email', 'Room')
        self.tree_table.column("#0", width=120, minwidth=25, anchor="center")
        self.tree_table.column("Name", anchor="center")
        self.tree_table.column("Lastname", anchor="center")
        self.tree_table.column("Age", anchor="center")
        self.tree_table.column("Email", anchor="center")
        self.tree_table.column("Room", anchor="center")

        self.tree_table.heading("#0", text="ID", anchor="center")
        self.tree_table.heading("Name", text="Name", anchor="center")
        self.tree_table.heading("Lastname", text="LastName", anchor="center")
        self.tree_table.heading("Age", text="Age", anchor="center")
        self.tree_table.heading("Email", text="Email", anchor="center")
        self.tree_table.heading("Room", text="Room", anchor="center")

        self.tree_table.insert(parent='', index="end",
                               iid=0, text="1", values=("test", "test", "test"))
        self.tree_table.insert(parent='', index="end",
                               iid=1, text="2", values=("test", "test", "test"))
        self.tree_table.grid(row=2, column=0, columnspan=4)
