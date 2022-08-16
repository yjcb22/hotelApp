from optparse import Option
from select import select
import tkinter as tk
from tkinter import StringVar, ttk


class Rooms(tk.Tk):
    """Room view class with TkInter

    :param tk: Tk superclass
    :type tk: TK
    """

    def __init__(self, master=None) -> None:
        """Constructor

        :param master: main Tk window, defaults to None
        :type tk: TK, optional
        """

        self.mainWindow = tk.Toplevel(master)
        self.mainWindow.title("Hotel check-in APP: Rooms")
                
        self.idLabel = tk.Label(self.mainWindow, text="ID", font="none 20 bold")
        self.idLabel.grid(row=0, column=0)
            
        self.idTextField = tk.Entry(self.mainWindow, width=5)
        self.idTextField.insert(0,"0")
        self.idTextField.grid(row=0, column=1)
        self.idTextField.config(state='readonly')
                
        self.addrLabel = tk.Label(self.mainWindow, text="Address", font="none 20 bold")
        self.addrLabel.grid(row=0, column=2)
            
        self.addrTextField = tk.Entry(self.mainWindow, width=20)
        self.addrTextField.grid(row=0, column=3)
        
        self.descLabel = tk.Label(self.mainWindow, text="Description", font="none 20 bold")
        self.descLabel.grid(row=0, column=4)
            
        self.descTextField = tk.Entry(self.mainWindow, width=20)
        self.descTextField.grid(row=0, column=5)
        
        self.sizeLabel = tk.Label(self.mainWindow, text="Size", font="none 20 bold")
        self.sizeLabel.grid(row=1, column=0)
            
        self.sizeTextField = tk.Entry(self.mainWindow, width=5)
        self.sizeTextField.grid(row=1, column=1)
        
        self.nameLabel = tk.Label(self.mainWindow, text="Name", font="none 20 bold")
        self.nameLabel.grid(row=1, column=2)
            
        self.nameTextField = tk.Entry(self.mainWindow, width=20)
        self.nameTextField.grid(row=1, column=3)

        self.catLabel = tk.Label(self.mainWindow, text="Category", font="none 20 bold")
        self.catLabel.grid(row=1, column=4)


        self.options = ["one", "two", "three"] 
        self.catDropdown = ttk.Combobox(self.mainWindow, values=self.options)
        self.catDropdown.current(0)
        self.catDropdown.grid(row=1, column=5)
            
        self.actLabel = tk.Label(self.mainWindow, text="Active", font="none 20 bold")
        self.actLabel.grid(row=2, column=0)
            
        self.actTextField = tk.Entry(self.mainWindow, width=5)
        self.actTextField.grid(row=2, column=1)
        
        self.addBtn = tk.Button(self.mainWindow, text="Add", width=10)
        self.addBtn.grid(row=3, column=2)
            
        self.updateBtn = tk.Button(self.mainWindow, text="Update", width=10)
        self.updateBtn.grid(row=3, column=3)
            
        self.deleteBtn = tk.Button(self.mainWindow, text="Delete", width=10)
        self.deleteBtn.grid(row=3, column=4)
            
        self.hintLabel = tk.Label(self.mainWindow, text="Hint: Click then edit or delete", font="none 20")
        self.hintLabel.grid(row=4, column=0, columnspan=10)
            
        self.treeTable = ttk.Treeview(self.mainWindow)
        self.treeTable['columns'] = ('Address', 'Description', 'Size', 'Name', 'Category', 'Active')
        self.treeTable.column("#0", width=120, minwidth=25, anchor="center")
        self.treeTable.column("Address", anchor="center")
        self.treeTable.column("Description", anchor="center")
        self.treeTable.column("Size", anchor="center")
        self.treeTable.column("Name", anchor="center")
        self.treeTable.column("Category", anchor="center")
        self.treeTable.column("Active", anchor="center")
        
        self.treeTable.heading("#0", text="ID", anchor="center")
        self.treeTable.heading("Address", text="Address", anchor="center")
        self.treeTable.heading("Description", text="Description", anchor="center")
        self.treeTable.heading("Size", text="Size", anchor="center")
        self.treeTable.heading("Name", text="Name", anchor="center")
        self.treeTable.heading("Category", text="Category", anchor="center")
        self.treeTable.heading("Active", text="Active", anchor="center")
            
        self.treeTable.insert(parent='', index="end", iid=0, text="1", values=("test", "test", "test"))
        self.treeTable.insert(parent='', index="end", iid=1, text="2", values=("test", "test", "test"))
        self.treeTable.grid(row=4, column=0, columnspan=6)