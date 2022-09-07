import tkinter as tk
from tkinter import ttk


class Rooms:
    """Room view class with TkInter

    :param tk: Tk superclass
    :type tk: TK
    """

    def __init__(self, master=None) -> None:
        """Constructor

        :param master: main Tk window, defaults to None
        :type tk: TK, optional
        """

        self.main_window = tk.Toplevel(master)
        self.main_window.title("Hotel check-in APP: Rooms")

        self.id_label = tk.Label(
            self.main_window, text="ID", font="none 20 bold")
        self.id_label.grid(row=0, column=0)

        self.id_text_field = tk.Entry(self.main_window, width=5)
        self.id_text_field.insert(0, "0")
        self.id_text_field.grid(row=0, column=1)
        self.id_text_field.config(state='readonly')

        self.addr_label = tk.Label(
            self.main_window, text="Address", font="none 20 bold")
        self.addr_label.grid(row=0, column=2)

        self.addr_text_field = tk.Entry(self.main_window, width=20)
        self.addr_text_field.grid(row=0, column=3)

        self.desc_label = tk.Label(
            self.main_window, text="Description", font="none 20 bold")
        self.desc_label.grid(row=0, column=4)

        self.desc_text_field = tk.Entry(self.main_window, width=20)
        self.desc_text_field.grid(row=0, column=5)

        self.size_label = tk.Label(
            self.main_window, text="Size", font="none 20 bold")
        self.size_label.grid(row=1, column=0)

        self.size_text_field = tk.Entry(self.main_window, width=5)
        self.size_text_field.grid(row=1, column=1)

        self.name_label = tk.Label(
            self.main_window, text="Name", font="none 20 bold")
        self.name_label.grid(row=1, column=2)

        self.name_text_field = tk.Entry(self.main_window, width=20)
        self.name_text_field.grid(row=1, column=3)

        self.cat_label = tk.Label(
            self.main_window, text="Category", font="none 20 bold")
        self.cat_label.grid(row=1, column=4)

        self.options = ["one", "two", "three"]
        self.cat_dropdown = ttk.Combobox(self.main_window, values=self.options)
        self.cat_dropdown.current(0)
        self.cat_dropdown.grid(row=1, column=5)
        self.cat_dropdown.config(state='readonly')

        self.act_label = tk.Label(
            self.main_window, text="Active", font="none 20 bold")
        self.act_label.grid(row=2, column=0)

        self.act_text_field = tk.Entry(self.main_window, width=5)
        self.act_text_field.grid(row=2, column=1)

        self.add_btn = tk.Button(self.main_window, text="Add", width=10)
        self.add_btn.grid(row=3, column=2)

        self.update_btn = tk.Button(self.main_window, text="Update", width=10)
        self.update_btn.grid(row=3, column=3)

        self.delete_btn = tk.Button(self.main_window, text="Delete", width=10)
        self.delete_btn.grid(row=3, column=4)

        self.tree_table = ttk.Treeview(self.main_window)
        self.tree_table['columns'] = (
            'Address', 'Description', 'Size', 'Name', 'Category', 'Active')
        self.tree_table.column("#0", width=120, minwidth=25, anchor="center")
        self.tree_table.column("Address", anchor="center")
        self.tree_table.column("Description", anchor="center")
        self.tree_table.column("Size", anchor="center")
        self.tree_table.column("Name", anchor="center")
        self.tree_table.column("Category", anchor="center")
        self.tree_table.column("Active", anchor="center")

        self.tree_table.heading("#0", text="ID", anchor="center")
        self.tree_table.heading("Address", text="Address", anchor="center")
        self.tree_table.heading(
            "Description", text="Description", anchor="center")
        self.tree_table.heading("Size", text="Size", anchor="center")
        self.tree_table.heading("Name", text="Name", anchor="center")
        self.tree_table.heading("Category", text="Category", anchor="center")
        self.tree_table.heading("Active", text="Active", anchor="center")

        self.tree_table.insert(parent='', index="end",
                               iid=0, text="1", values=("test", "test", "test"))
        self.tree_table.insert(parent='', index="end",
                               iid=1, text="2", values=("test", "test", "test"))
        self.tree_table.grid(row=4, column=0, columnspan=6)
