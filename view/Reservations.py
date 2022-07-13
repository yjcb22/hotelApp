import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

class Reservations:
    def __init__(self) -> None:
       self.mainWindow = tk.Tk()
       self.mainWindow.title("Hotel check-in APP: Reservations")
             
       self.idLabel = tk.Label(self.mainWindow, text="ID", font="none 20 bold")
       self.idLabel.grid(row=0, column=0)
        
       self.idTextField = tk.Entry(self.mainWindow, width=5)
       self.idTextField.insert(0,"0")
       self.idTextField.grid(row=0, column=1)
       self.idTextField.config(state='disabled')
              
       self.startLabel = tk.Label(self.mainWindow, text="Start", font="none 20 bold")
       self.startLabel.grid(row=0, column=2)
        
       self.startDate = DateEntry(self.mainWindow, width=20)
       self.startDate.grid(row=0, column=3)
       
       self.endLabel = tk.Label(self.mainWindow, text="End", font="none 20 bold")
       self.endLabel.grid(row=0, column=4)
        
       self.endTextField = DateEntry(self.mainWindow, width=20)
       self.endTextField.grid(row=0, column=5)
       
       self.statusLabel = tk.Label(self.mainWindow, text="Status", font="none 20 bold")
       self.statusLabel.grid(row=1, column=2)
        
       self.statusTextField = tk.Entry(self.mainWindow, width=20)
       self.statusTextField.grid(row=1, column=3)
       
       self.scoreLabel = tk.Label(self.mainWindow, text="Score", font="none 20 bold")
       self.scoreLabel.grid(row=1, column=4)
        
       self.scoreTextField = tk.Entry(self.mainWindow, width=20)
       self.scoreTextField.grid(row=1, column=5)      
  
       
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