class CategoryDTO:
    
    def __init__(self, name="", description="", id=0, active=1) -> None:
        self.id = id
        self.name = name
        self.description = description  
        self.active = active      
          
    

    def toString(self) -> str:
        return "CategoryDTO{" + "id=" + str(self.id) + ", name=" + self.name + ", description=" + self.description + ", active=" + self.active +'}'