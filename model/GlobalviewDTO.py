class GlobalviewDTO:
    
    def __init__(self, name="", lastname="", email="", id = 0, age=0, room=0) -> None:
        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email        
        self.room = room        
          
    

    def toString(self) -> str:
        return "GlobalviewDTO{" + "id=" + str(self.id) + ", name=" + self.name + ", lastname=" + self.lastname + ", age=" + str(self.age) + ", email=" + self.email + ", room=" + str(self.room) + '}'