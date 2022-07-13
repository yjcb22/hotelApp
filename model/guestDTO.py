import email


class GuestDTO:
    
    def __init__(self, name = "", lastname="", age=0, email="", password="", id = 0) -> None:
        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email
        self.password = password        
          
    

    def toString(self) -> str:
        return "GuestDTO{" + "id=" + str(self.id) + ", name=" + self.name + ", lastname=" + self.lastname + ", age=" + str(self.age) + ", email=" + self.email + ", password=" + self.password + '}'