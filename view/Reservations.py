import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class Reservations:
    """Reservations view class with TkInter

    :param tk: Tk superclass
    :type tk: TK
    """

    def __init__(self, master=None) -> None:
        """Constructor

        :param master: main Tk window, defaults to None
        :type tk: TK, optional
        """
        self.main_window = tk.Toplevel(master)
        self.main_window.title("Hotel check-in APP: Reservations")

        self.id_label = tk.Label(
            self.main_window, text="ID", font="none 20 bold")
        self.id_label.grid(row=0, column=0)

        self.id_text_field = tk.Entry(self.main_window, width=5)
        self.id_text_field.insert(0, "0")
        self.id_text_field.grid(row=0, column=1)
        self.id_text_field.config(state='readonly')

        self.start_label = tk.Label(
            self.main_window, text="Start", font="none 20 bold")
        self.start_label.grid(row=0, column=2)

        self.start_date = DateEntry(
            self.main_window, width=20, date_pattern='y-MM-dd')
        self.start_date.grid(row=0, column=3)

        self.end_label = tk.Label(
            self.main_window, text="End", font="none 20 bold")
        self.end_label.grid(row=0, column=4)

        self.end_date = DateEntry(
            self.main_window, width=20, date_pattern='y-MM-dd')
        self.end_date.grid(row=0, column=5)

        self.status_label = tk.Label(
            self.main_window, text="Status", font="none 20 bold")
        self.status_label.grid(row=1, column=0)

        self.options = ["one", "two", "three"]
        self.status_dropdown = ttk.Combobox(
            self.main_window, values=self.options)
        self.status_dropdown.current(0)
        self.status_dropdown.grid(row=1, column=1)
        self.status_dropdown.config(state='readonly')

        self.score_label = tk.Label(
            self.main_window, text="Score", font="none 20 bold")
        self.score_label.grid(row=1, column=2)

        self.score_dropdown = ttk.Combobox(
            self.main_window, values=self.options)
        self.score_dropdown.current(0)
        self.score_dropdown.grid(row=1, column=3)
        self.score_dropdown.config(state='readonly')

        self.room_label = tk.Label(
            self.main_window, text="Room", font="none 20 bold")
        self.room_label.grid(row=1, column=4)

        self.room_dropdown = ttk.Combobox(
            self.main_window, values=self.options)
        self.room_dropdown.current(0)
        self.room_dropdown.grid(row=1, column=5)
        self.room_dropdown.config(state='readonly')

        self.guest_label = tk.Label(
            self.main_window, text="Guest", font="none 20 bold")
        self.guest_label.grid(row=2, column=0)

        self.guest_dropdown = ttk.Combobox(
            self.main_window, values=self.options)
        self.guest_dropdown.current(0)
        self.guest_dropdown.grid(row=2, column=1)
        self.guest_dropdown.config(state='readonly')

        self.act_label = tk.Label(
            self.main_window, text="Active", font="none 20 bold")
        self.act_label.grid(row=2, column=2)

        self.act_text_field = tk.Entry(self.main_window, width=5)
        self.act_text_field.grid(row=2, column=3)

        self.add_btn = tk.Button(self.main_window, text="Add", width=10)
        self.add_btn.grid(row=3, column=2)

        self.update_btn = tk.Button(self.main_window, text="Update", width=10)
        self.update_btn.grid(row=3, column=3)

        self.delete_btn = tk.Button(self.main_window, text="Delete", width=10)
        self.delete_btn.grid(row=3, column=4)

        self.tree_table = ttk.Treeview(self.main_window)
        self.tree_table['columns'] = (
            'Start', 'End', 'Status', 'Score', 'Room', 'Guest', 'Active')
        self.tree_table.column("#0", width=120, minwidth=25, anchor="center")
        self.tree_table.column("Start", anchor="center")
        self.tree_table.column("End", anchor="center")
        self.tree_table.column("Status", anchor="center")
        self.tree_table.column("Score", anchor="center")
        self.tree_table.column("Room", anchor="center")
        self.tree_table.column("Guest", anchor="center")
        self.tree_table.column("Active", anchor="center")

        self.tree_table.heading("#0", text="ID", anchor="center")
        self.tree_table.heading("Start", text="Start", anchor="center")
        self.tree_table.heading("End", text="End", anchor="center")
        self.tree_table.heading("Status", text="Status", anchor="center")
        self.tree_table.heading("Score", text="Score", anchor="center")
        self.tree_table.heading("Room", text="Room", anchor="center")
        self.tree_table.heading("Guest", text="Guest", anchor="center")
        self.tree_table.heading("Active", text="Active", anchor="center")

        self.tree_table.insert(parent='', index="end",
                               iid=0, text="1", values=("test", "test", "test", "test", "test", "test", "test"))
        self.tree_table.insert(parent='', index="end",
                               iid=1, text="2", values=("test", "test", "test", "test", "test", "test", "test"))
        self.tree_table.grid(row=4, column=0, columnspan=6)
