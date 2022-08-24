from controller.GlobalviewCtl import GlobalviewCtl
from model.guestDAO import GuestDAO
from model.guestDTO import GuestDTO
from view.GlobalView import GlobalView
from view.Login import Login


class LoginCtl:
    """Controller for the Login process
    """

    def __init__(self, view: Login, cx) -> None:
        """Constructor

        :param view: Instance of the Login view class
        :type view: Login
        :param cx: Instance of the database connection class
        :type cx: raw connection or specific class DAO
        """
        self.view = view
        self.cx = cx

        # Create DB object with existing connection
        self.guestDao = GuestDAO(self.cx)

        self.view.loginBtn.config(command=self.getLogin)
        self.view.loginBtn.bind("<Return>", self.getLogin)

    def getLogin(self, e=None) -> None:
        """Obtain values from GUI and compare with the database

        :param e: Needed for the function binding, defaults to None
        :type e: element clicked, optional
        """
        username = self.view.usernameTextField.get()
        password = self.view.passwordTextField.get()
        guest = GuestDTO("", "", "", username, password)
        answer = self.login(guest)
        if answer:
            GlobalviewCtl(GlobalView(self.view), self.guestDao)
            # self.view.withdraw()
        else:
            self.view.hintLabel.config(text="Hint: Wrong info!")

    def login(self, guest: GuestDTO) -> list[GuestDTO]:
        """Check agains the database

        :param guest: DTO object from GUI
        :type guest: GuestDTO
        :return: boolean with information from DB.
        :rtype: list[GuestDTO]
        """
        return self.guestDao.validateCredentials(guest)
