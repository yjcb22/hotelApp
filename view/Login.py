import tkinter as tk


class Login(tk.Tk):
    """View to ask for username and password

    :param tk: Tkinter superclass
    :type tk: _type_
    """

    def __init__(self) -> None:
        """Constructor
        """
        super().__init__()
        self.title("Hotel check-in APP : Login")

        self.username_label = tk.Label(
            self, text="Username", font="none 20 bold")
        self.username_label.grid(row=0, column=0)

        self.username_text_field = tk.Entry(self, width=20)
        self.username_text_field.insert(0, "email1@test1.com")
        self.username_text_field.grid(row=0, column=1)

        self.password_label = tk.Label(
            self, text="Password", font="none 20 bold")
        self.password_label.grid(row=1, column=0)

        self.password_text_field = tk.Entry(self, width=20)
        self.password_text_field.insert(0, "password1")
        self.password_text_field.grid(row=1, column=1)

        self.hint_label = tk.Label(
            self, text="Hint:", font="none 20 bold", foreground='red')
        self.hint_label.grid(row=2, column=0, columnspan=2)

        self.login_btn = tk.Button(self, text="Login", width=10)
        self.login_btn.grid(row=3, column=0, columnspan=2)
