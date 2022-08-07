import tkinter as tk
from tkinter import ttk

class GlobalView(tk.Tk):
    def __init__(self, master = None) -> None:        
        self.mainWindow = tk.Toplevel(master)
        self.mainWindow.title("Hotel check-in APP: Global")
        
        self.categoryBtn = tk.Button(self.mainWindow, text="Categories", width=10)
        self.categoryBtn.grid(row=0, column=0)
        
        self.roomsBtn = tk.Button(self.mainWindow, text="Rooms", width=10)
        self.roomsBtn.grid(row=0, column=1)
        
        self.guestBtn = tk.Button(self.mainWindow, text="Guests", width=10)
        self.guestBtn.grid(row=0, column=2)
        
        self.reservationsBtn = tk.Button(self.mainWindow, text="Reservations", width=10)
        self.reservationsBtn.grid(row=0, column=3)
        
        
        self.treeTable = ttk.Treeview(self.mainWindow)
        self.treeTable['columns'] = ('Name', 'Lastname', 'Age', 'Email', 'Room')
        self.treeTable.column("#0", width=120, minwidth=25, anchor="center")
        self.treeTable.column("Name", anchor="center")
        self.treeTable.column("Lastname", anchor="center")
        self.treeTable.column("Age", anchor="center")
        self.treeTable.column("Email", anchor="center")
        self.treeTable.column("Room", anchor="center")
        
        self.treeTable.heading("#0", text="ID", anchor="center")
        self.treeTable.heading("Name", text="Name", anchor="center")
        self.treeTable.heading("Lastname", text="LastName", anchor="center")
        self.treeTable.heading("Age", text="Age", anchor="center")
        self.treeTable.heading("Email", text="Email", anchor="center")
        self.treeTable.heading("Room", text="Room", anchor="center")
        
        self.treeTable.insert(parent='', index="end", iid=0, text="1", values=("test", "test", "test"))
        self.treeTable.insert(parent='', index="end", iid=1, text="2", values=("test", "test", "test"))
        self.treeTable.grid(row=2, column=0, columnspan=4)