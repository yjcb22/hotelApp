import tkinter as tk
from tkinter import ttk


class Categories:
    """Categories view class with TKinter
    """

    def __init__(self, master=None) -> None:
        """Constructor

        :param master: main windows, defaults to None
        :type master: Tkinter, optional
        """
        self.main_window = tk.Toplevel(master)
        self.main_window.title("Hotel check-in APP: Categories")

        self.id_label = tk.Label(
            self.main_window, text="ID", font="none 20 bold")
        self.id_label.grid(row=0, column=0)

        self.id_text_field = tk.Entry(self.main_window, width=5)
        self.id_text_field.insert(0, "0")
        self.id_text_field.grid(row=0, column=1)
        self.id_text_field.config(state='readonly')

        self.name_label = tk.Label(
            self.main_window, text="Name", font="none 20 bold")
        self.name_label.grid(row=0, column=2)

        self.name_text_field = tk.Entry(self.main_window, width=20)
        self.name_text_field.grid(row=0, column=3)

        self.desc_label = tk.Label(
            self.main_window, text="Description", font="none 20 bold")
        self.desc_label.grid(row=0, column=4)

        self.desc_text_field = tk.Entry(self.main_window, width=20)
        self.desc_text_field.grid(row=0, column=5)

        self.active_label = tk.Label(
            self.main_window, text="Active", font="none 20 bold")
        self.active_label.grid(row=0, column=6)

        self.active_text_field = tk.Entry(self.main_window, width=5)
        self.active_text_field.grid(row=0, column=7)

        self.add_btn = tk.Button(self.main_window, text="Add", width=10)
        self.add_btn.grid(row=1, column=3)

        self.update_btn = tk.Button(self.main_window, text="Update", width=10)
        self.update_btn.grid(row=1, column=4)

        self.delete_btn = tk.Button(self.main_window, text="Delete", width=10)
        self.delete_btn.grid(row=1, column=5)

        self.tree_table = ttk.Treeview(self.main_window)
        self.tree_table['columns'] = ('Name', 'Description', 'Active')
        self.tree_table.column("#0", width=120, minwidth=25, anchor="center")
        self.tree_table.column("Name", anchor="center")
        self.tree_table.column("Description", anchor="center")
        self.tree_table.column("Active", anchor="center")

        self.tree_table.heading("#0", text="ID", anchor="center")
        self.tree_table.heading("Name", text="Name", anchor="center")
        self.tree_table.heading(
            "Description", text="Description", anchor="center")
        self.tree_table.heading("Active", text="Active", anchor="center")

        self.tree_table.insert(parent='', index="end", iid=0,
                               text="1", values=("test", "test"))
        self.tree_table.insert(parent='', index="end", iid=1,
                               text="2", values=("test", "test"))
        self.tree_table.grid(row=3, column=1, columnspan=7)
