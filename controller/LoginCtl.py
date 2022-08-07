from controller.GlobalviewCtl import GlobalviewCtl
from model.guestDAO import GuestDAO
from model.guestDTO import GuestDTO
from view.GlobalView import GlobalView
from view.Login import Login


class LoginCtl:
    def __init__(self, view: Login, cx) -> None:
        self.view = view
        self.cx = cx
        
        ##Create DB object with existing connection
        self.guestDao = GuestDAO(self.cx)
        
        self.view.loginBtn.config(command=self.getLogin)
        self.view.loginBtn.bind("<Return>", self.getLogin)
        
    def getLogin(self, e=None) -> None:
        username = self.view.usernameTextField.get()
        password = self.view.passwordTextField.get()
        guest = GuestDTO("","","",username,password)
        answer = self.login(guest)
        if answer:            
            GlobalviewCtl(GlobalView(self.view),self.guestDao)
            #self.view.withdraw()
        else:
            self.view.hintLabel.config(text="Hint: Wrong info!")
        
    def login(self, guest: GuestDTO) -> list[GuestDTO]:
        return self.guestDao.validateCredentials(guest)