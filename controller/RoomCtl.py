from tkinter import StringVar
from model.CategoryDAO import CategoryDAO
from model.RoomDAO import RoomDAO
from model.RoomDTO import RoomDTO
from view.Rooms import Rooms

class RoomCtl:
    def __init__(self, view: Rooms, cx) -> None:
        self.view = view
        self.cx = cx

        ##Create DB object with existing connection
        self.roomDao = RoomDAO(cx)
        #Needed to bring the list of categories for the dropdownmenu
        self.catDao = CategoryDAO(cx)
        self.getAllRooms()


        #Button actions
        self.view.addBtn.config(command=self.add)
        self.view.updateBtn.config(command=self.update)
        self.view.deleteBtn.config(command=self.delete)

        #Click Actions
        self.view.treeTable.bind("<ButtonRelease-1>", self.onOneClick)
    
    def onOneClick(self, e) -> None:
        room = self.getRoomDto()
        self.setText(room.id,self.view.idTextField)
        self.setText(room.address,self.view.addrTextField)
        self.setText(room.description,self.view.descTextField)
        self.setText(room.size,self.view.sizeTextField)
        self.setText(room.name,self.view.nameTextField)
        #Set value of combobox
        index=self.view.options.index(room.category)
        self.view.catDropdown.current(index)
        self.setText(room.active,self.view.actTextField)

    

    def setText(self, text: str, e)->None:
        st = StringVar()
        st.set(text)
        e.config(textvariable=st)
    
    def setOptions(self)->None:
        categories = self.catDao.selectAllCategories()
        names = [i.name for i in categories] #List comprehension
        self.view.options = names
        self.view.catDropdown.config(values=self.view.options)
        self.view.catDropdown.current(0)  

        


    def getRoomDto(self) -> RoomDTO:
        selected = self.view.treeTable.focus()
        values = self.view.treeTable.item(selected, 'values')
        return(RoomDTO(values[0],values[1], values[2], values[3], values[4], selected, values[5]))
         

    def getAllRooms(self) -> None:
        rooms = self.roomDao.selectAllRooms()
        self.setOptions()
        self.refreshTreeTable(rooms)

    def refreshTreeTable(self, data: list[RoomDTO]) -> None:
        ##clean Table
        for i in self.view.treeTable.get_children():
            self.view.treeTable.delete(i)
        ##from database to table
        for i in range(len(data)):
            self.view.treeTable.insert(parent='', index="end", iid=data[i].id, text=data[i].id, \
            values=(data[i].address, data[i].description, data[i].size, \
            data[i].name,data[i].category,data[i].active))
            #print(i, data[i].toString())
    
    def clearAll(self) -> None:
        self.setText("",self.view.idTextField)
        self.setText("",self.view.addrTextField)
        self.setText("",self.view.descTextField)
        self.setText("",self.view.sizeTextField)
        self.setText("",self.view.nameTextField)
        self.view.catDropdown.current(0)
        self.setText("",self.view.actTextField)

        
        
        
        
    def add(self)-> None:
        name = self.view.addrTextField.get()
        desc = self.view.addrTextField.get()
        self.roomDao.insertCategory(CategoryDTO(name, desc))  
        self.getAllRooms()
        self.clearAll()
        

    def update(self)-> None:  
        id = self.view.idTextField.get()
        addr = self.view.addrTextField.get()
        desc = self.view.descTextField.get()
        size = self.view.sizeTextField.get()
        name = self.view.nameTextField.get()
        #Combobox
        cat = self.view.catDropdown.get()
        indexCat = self.view.options.index(cat) + 1 #database index starts in 1 not in 0

        active = self.view.actTextField.get()
        self.roomDao.updateRoom(RoomDTO(addr,desc,size,name,indexCat,id,active))
        
        self.getAllRooms()
        self.clearAll()

    def delete(self)-> None:  
        roomId = self.view.idTextField.get()
        self.roomDao.deleteRoom(roomId)
        self.getAllRooms()
        self.clearAll()