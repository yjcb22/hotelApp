import tkinter as tk
from tkinter import ttk


class Guests:
    """Guests view class with TkInter

    :param tk: Tk superclass
    :type tk: TK
    """

    def __init__(self, master=None) -> None:
        """Constructor
        """
        self.main_window = tk.Toplevel(master)
        self.main_window.title("Hotel check-in APP: Guests")

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

        self.last_label = tk.Label(
            self.main_window, text="Lastname", font="none 20 bold")
        self.last_label.grid(row=0, column=4)

        self.last_text_field = tk.Entry(self.main_window, width=20)
        self.last_text_field.grid(row=0, column=5)

        self.age_label = tk.Label(
            self.main_window, text="Age", font="none 20 bold")
        self.age_label.grid(row=1, column=0)

        self.age_text_field = tk.Entry(self.main_window, width=20)
        self.age_text_field.grid(row=1, column=1)

        self.email_label = tk.Label(
            self.main_window, text="Email", font="none 20 bold")
        self.email_label.grid(row=1, column=2)

        self.email_text_field = tk.Entry(self.main_window, width=20)
        self.email_text_field.grid(row=1, column=3)

        self.password_label = tk.Label(
            self.main_window, text="Password", font="none 20 bold")
        self.password_label.grid(row=1, column=4)

        self.password_text_field = tk.Entry(self.main_window, width=20)
        self.password_text_field.grid(row=1, column=5)

        self.active_label = tk.Label(
            self.main_window, text="Active", font="none 20 bold")
        self.active_label.grid(row=2, column=0)

        self.active_text_field = tk.Entry(self.main_window, width=5)
        self.active_text_field.grid(row=2, column=1)

        self.add_btn = tk.Button(self.main_window, text="Add", width=10)
        self.add_btn.grid(row=3, column=2)

        self.update_btn = tk.Button(self.main_window, text="Update", width=10)
        self.update_btn.grid(row=3, column=3)

        self.delete_btn = tk.Button(self.main_window, text="Delete", width=10)
        self.delete_btn.grid(row=3, column=4)

        self.tree_table = ttk.Treeview(self.main_window)
        self.tree_table['columns'] = (
            'Name', 'Lastname', 'Age', 'Email', 'Password', 'Active')
        self.tree_table.column("#0", width=120, minwidth=25, anchor="center")
        self.tree_table.column("Name", anchor="center")
        self.tree_table.column("Lastname", anchor="center")
        self.tree_table.column("Age", anchor="center")
        self.tree_table.column("Email", anchor="center")
        self.tree_table.column("Password", anchor="center")
        self.tree_table.column("Active", anchor="center")

        self.tree_table.heading("#0", text="ID", anchor="center")
        self.tree_table.heading("Name", text="Name", anchor="center")
        self.tree_table.heading("Lastname", text="LastName", anchor="center")
        self.tree_table.heading("Age", text="Age", anchor="center")
        self.tree_table.heading("Email", text="Email", anchor="center")
        self.tree_table.heading("Password", text="Password", anchor="center")
        self.tree_table.heading("Active", text="Active", anchor="center")

        self.tree_table.insert(parent='', index="end", iid=0, text="1", values=(
            "test", "test", "test", "test", "test", "test"))
        self.tree_table.insert(parent='', index="end", iid=1, text="2", values=(
            "test", "test", "test", "test", "test", "test"))
        self.tree_table.grid(row=4, column=0, columnspan=6)
