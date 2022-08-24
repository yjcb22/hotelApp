import tkinter as tk
from tkinter import ttk

class Guests:
    """Guests view class with TKinter
    """
    def __init__(self) -> None:
        """Constructor
        """
        self.mainWindow = tk.Tk()
        self.mainWindow.title("Hotel check-in APP: Guests")
                
        self.idLabel = tk.Label(self.mainWindow, text="ID", font="none 20 bold")
        self.idLabel.grid(row=0, column=0)

        self.idTextField = tk.Entry(self.mainWindow, width=5)
        self.idTextField.insert(0,"0")
        self.idTextField.grid(row=0, column=1)
        self.idTextField.config(state='disabled')
                
        self.nameLabel = tk.Label(self.mainWindow, text="Name", font="none 20 bold")
        self.nameLabel.grid(row=0, column=2)

        self.nameTextField = tk.Entry(self.mainWindow, width=20)
        self.nameTextField.grid(row=0, column=3)

        self.lastLabel = tk.Label(self.mainWindow, text="Lastname", font="none 20 bold")
        self.lastLabel.grid(row=0, column=4)

        self.lastTextField = tk.Entry(self.mainWindow, width=20)
        self.lastTextField.grid(row=0, column=5)

        self.ageLabel = tk.Label(self.mainWindow, text="Age", font="none 20 bold")
        self.ageLabel.grid(row=1, column=2)

        self.ageTextField = tk.Entry(self.mainWindow, width=20)
        self.ageTextField.grid(row=1, column=3)

        self.emailLabel = tk.Label(self.mainWindow, text="Email", font="none 20 bold")
        self.emailLabel.grid(row=1, column=4)

        self.emailTextField = tk.Entry(self.mainWindow, width=20)
        self.emailTextField.grid(row=1, column=5)

        self.passwordLabel = tk.Label(self.mainWindow, text="Password", font="none 20 bold")
        self.passwordLabel.grid(row=2, column=2)

        self.passwordTextField = tk.Entry(self.mainWindow, width=20)
        self.passwordTextField.grid(row=2, column=3)

        self.addBtn = tk.Button(self.mainWindow, text="Add", width=10)
        self.addBtn.grid(row=3, column=2)

        self.editBtn = tk.Button(self.mainWindow, text="Edit", width=10)
        self.editBtn.grid(row=3, column=3)

        self.deleteBtn = tk.Button(self.mainWindow, text="Delete", width=10)
        self.deleteBtn.grid(row=3, column=4)

        self.hintLabel = tk.Label(self.mainWindow, text="Hint: Click on the entry to fill-in the information before editing", font="none 20")
        self.hintLabel.grid(row=4, column=0, columnspan=10)

        self.treeTable = ttk.Treeview(self.mainWindow)
        self.treeTable['columns'] = ('Name', 'Lastname', 'Room')
        self.treeTable.column("#0", width=120, minwidth=25, anchor="center")
        self.treeTable.column("Name", anchor="center")
        self.treeTable.column("Lastname", anchor="center")
        self.treeTable.column("Room", anchor="center")

        self.treeTable.heading("#0", text="ID", anchor="center")
        self.treeTable.heading("Name", text="Name", anchor="center")
        self.treeTable.heading("Lastname", text="LastName", anchor="center")
        self.treeTable.heading("Room", text="Room", anchor="center")

        self.treeTable.insert(parent='', index="end", iid=0, text="1", values=("test", "test", "test"))
        self.treeTable.insert(parent='', index="end", iid=1, text="2", values=("test", "test", "test"))
        self.treeTable.grid(row=4, column=0, columnspan=6)