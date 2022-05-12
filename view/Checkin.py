import tkinter as tk
from tkinter import ttk

class Checkin:
    def __init__(self) -> None:
        self.mainWindow = tk.Tk()
        self.mainWindow.title("Hotel check-in")
        
        self.nameLabel = tk.Label(self.mainWindow, text="Name", font="none 20 bold")
        self.nameLabel.grid(row=0, column=0)
        
        self.nameTextLabel = tk.Entry(self.mainWindow, width=10)
        self.nameTextLabel.grid(row=0, column=1)
        
        self.lastLabel = tk.Label(self.mainWindow, text="LastName", font="none 20 bold")
        self.lastLabel.grid(row=0, column=2)
        
        self.lastTextLabel = tk.Entry(self.mainWindow, width=10)
        self.lastTextLabel.grid(row=0, column=3)
        
        self.roomLabel = tk.Label(self.mainWindow, text="Room", font="none 20 bold")
        self.roomLabel.grid(row=0, column=4)

        self.roomTextLabel = tk.Entry(self.mainWindow, width=10)
        self.roomTextLabel.grid(row=0, column=5)
        
        self.checkInBtn = tk.Button(self.mainWindow, text="Check-in", width=10)
        self.checkInBtn.grid(row=1, column=2)

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
        
        #self.treeTable.insert(parent='', index="end", iid=0, text="1", values=("test", "test", "test"))
        #self.treeTable.insert(parent='', index="end", iid=1, text="2", values=("test", "test", "test"))
        self.treeTable.grid(row=2, column=0, columnspan=6)