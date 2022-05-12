class GuestDTO:
    
    def __init__(self, name: str, lastname: str, room: int, id = 0) -> None:
        self.id = id
        self.name = name
        self.lastname = lastname
        self.room = room 

    def toString(self) -> str:
        return "GuestDTO{" + "id=" + self.id + "name=" + self.name + ", lastname=" + self.lastname + ", room=" + str(self.room) + '}'