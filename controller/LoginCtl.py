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
        self.guest_dao = GuestDAO(self.cx)

        self.view.login_btn.config(command=self.get_login)
        self.view.login_btn.bind("<Return>", self.get_login)

    def get_login(self, e=None) -> None:
        """Obtain vlaues from GUI and compare with the database

        :param e: Needed for th function binding, defaults to None
        :type e: object, optional
        """

        username = self.view.username_text_field.get()
        password = self.view.password_text_field.get()
        guest = GuestDTO("", "", "", username, password)
        answer = self.login(guest)
        if answer:
            GlobalviewCtl(GlobalView(self.view), self.guest_dao)
            # self.view.withdraw()
        else:
            self.view.hint_label.config(text="Hint: Wrong info!")

    def login(self, guest: GuestDTO) -> list[GuestDTO]:
        """Check agains the database

        :param guest: DTO object from GUI
        :type guest: GuestDTO
        :return: boolean with information from DB.
        :rtype: list[GuestDTO]
        """
        return self.guest_dao.validate_credentials(guest)
