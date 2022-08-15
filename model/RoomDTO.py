class RoomDTO:
    
    def __init__(self, address="", description="", size="", name="", category="", id=0, active=1) -> None:
        self.id = id
        self.address = address
        self.description = description  
        self.size = size
        self.name = name
        self.category = category
        self.active = active      
          
    

    def toString(self) -> str:
        return "RoomDTO{" + "id=" + str(self.id) + ", address=" + str(self.address) + \
            ", description=" + self.description + ", size=" + str(self.size) + \
            ", name=" + self.name + ", category=" + str(self.category) + \
            ", active=" + str(self.active) + '}'