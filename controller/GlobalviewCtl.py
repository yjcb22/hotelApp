from model.CategoryDAO import CategoryDAO
from model.GlobalviewDTO import GlobalviewDTO
from model.guestDAO import GuestDAO
from controller.CategoryCtl import CategoryCtl
from view.Categories import Categories
from view.GlobalView import GlobalView


class GlobalviewCtl:
    def __init__(self, view: GlobalView, cx) -> None:
        self.view = view
        if isinstance(cx, GuestDAO):            
            self.guestDao = cx
        else:
            #Create DB object with existing connection
            self.guestDao = GuestDAO(cx)      
           
        self.getAllGuestsRev()

        #Button actions
        self.view.categoryBtn.config(command=self.openCategory)
        

    def getAllGuestsRev(self) -> None:        
        guestReserve = self.guestDao.selectGuestReserv()
        self.refreshTreeTable(guestReserve)

    def refreshTreeTable(self, data: list[GlobalviewDTO])-> None:
        ##clean Table
        for i in self.view.treeTable.get_children():
            self.view.treeTable.delete(i)
        ##from database to table
        for i in range(len(data)):
            self.view.treeTable.insert(parent='', index="end", iid=data[i].id, text=data[i].id, values=(data[i].name, data[i].lastname, data[i].age, data[i].email, data[i].room))
            #print(i, data[i].toString())
            
    def openCategory(self)-> None: 
        #get the original CX from Dao object
        cx = self.guestDao.db          
        CategoryCtl(Categories(), cx)