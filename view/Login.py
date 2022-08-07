import tkinter as tk
from tkinter import ttk

class Login(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Hotel check-in APP : Login")
        
        self.usernameLabel = tk.Label(self, text="Username", font="none 20 bold")
        self.usernameLabel.grid(row=0, column=0)
        
        self.usernameTextField = tk.Entry(self, width=20)
        self.usernameTextField.insert(0,"email1@test1.com")
        self.usernameTextField.grid(row=0, column=1)
        
        self.passwordLabel = tk.Label(self, text="Password", font="none 20 bold")
        self.passwordLabel.grid(row=1, column=0)
        
        self.passwordTextField = tk.Entry(self, width=20)
        self.passwordTextField.insert(0,"password1")
        self.passwordTextField.grid(row=1, column=1)
        
        self.hintLabel = tk.Label(self, text="Hint:", font="none 20 bold", foreground='red')
        self.hintLabel.grid(row=2, column=0, columnspan=2)
                
        self.loginBtn = tk.Button(self, text="Login", width=10)
        self.loginBtn.grid(row=3, column=0, columnspan=2)
        
        
        # self.mainWindow = tk.Tk()
        # self.mainWindow.title("Hotel check-in APP : Login")
        
        # self.usernameLabel = tk.Label(self.mainWindow, text="Username", font="none 20 bold")
        # self.usernameLabel.grid(row=0, column=0)
        
        # self.usernameTextField = tk.Entry(self.mainWindow, width=20)
        # self.usernameTextField.grid(row=0, column=1)
        
        # self.passwordLabel = tk.Label(self.mainWindow, text="Password", font="none 20 bold")
        # self.passwordLabel.grid(row=1, column=0)
        
        # self.passwordTextField = tk.Entry(self.mainWindow, width=20)
        # self.passwordTextField.grid(row=1, column=1)
        
        # self.hintLabel = tk.Label(self.mainWindow, text="Hint:", font="none 20 bold", foreground='red')
        # self.hintLabel.grid(row=2, column=0, columnspan=2)
                
        # self.loginBtn = tk.Button(self.mainWindow, text="Login", width=10)
        # self.loginBtn.grid(row=3, column=0, columnspan=2)