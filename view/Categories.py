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
        self.mainWindow = tk.Toplevel(master)
        self.mainWindow.title("Hotel check-in APP: Categories")

        self.idLabel = tk.Label(
            self.mainWindow, text="ID", font="none 20 bold")
        self.idLabel.grid(row=0, column=0)

        self.idTextField = tk.Entry(self.mainWindow, width=5)
        self.idTextField.insert(0, "0")
        self.idTextField.grid(row=0, column=1)
        self.idTextField.config(state='readonly')

        self.nameLabel = tk.Label(
            self.mainWindow, text="Name", font="none 20 bold")
        self.nameLabel.grid(row=0, column=2)

        self.nameTextField = tk.Entry(self.mainWindow, width=20)
        self.nameTextField.grid(row=0, column=3)

        self.descLabel = tk.Label(
            self.mainWindow, text="Description", font="none 20 bold")
        self.descLabel.grid(row=0, column=4)

        self.descTextField = tk.Entry(self.mainWindow, width=20)
        self.descTextField.grid(row=0, column=5)

        self.activeLabel = tk.Label(
            self.mainWindow, text="Active", font="none 20 bold")
        self.activeLabel.grid(row=0, column=6)

        self.activeTextField = tk.Entry(self.mainWindow, width=5)
        self.activeTextField.grid(row=0, column=7)

        self.addBtn = tk.Button(self.mainWindow, text="Add", width=10)
        self.addBtn.grid(row=1, column=3)

        self.updateBtn = tk.Button(self.mainWindow, text="Update", width=10)
        self.updateBtn.grid(row=1, column=4)

        self.deleteBtn = tk.Button(self.mainWindow, text="Delete", width=10)
        self.deleteBtn.grid(row=1, column=5)

        self.hintLabel = tk.Label(
            self.mainWindow, text="Hint: Click then edit or delete", font="none 20")
        self.hintLabel.grid(row=2, column=0, columnspan=7)

        self.treeTable = ttk.Treeview(self.mainWindow)
        self.treeTable['columns'] = ('Name', 'Description', 'Active')
        self.treeTable.column("#0", width=120, minwidth=25, anchor="center")
        self.treeTable.column("Name", anchor="center")
        self.treeTable.column("Description", anchor="center")
        self.treeTable.column("Active", anchor="center")

        self.treeTable.heading("#0", text="ID", anchor="center")
        self.treeTable.heading("Name", text="Name", anchor="center")
        self.treeTable.heading(
            "Description", text="Description", anchor="center")
        self.treeTable.heading("Active", text="Active", anchor="center")

        self.treeTable.insert(parent='', index="end", iid=0,
                              text="1", values=("test", "test"))
        self.treeTable.insert(parent='', index="end", iid=1,
                              text="2", values=("test", "test"))
        self.treeTable.grid(row=3, column=1, columnspan=7)
