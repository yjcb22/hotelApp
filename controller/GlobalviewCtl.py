from model.GlobalviewDTO import GlobalviewDTO
from model.guestDAO import GuestDAO
from view.GlobalView import GlobalView


class GlobalviewCtl:
    def __init__(self, view: GlobalView, guestDao: GuestDAO) -> None:
        self.view = view
        self.guestDao = guestDao
        self.getAllGuests()

    def getAllGuests(self):        
        guestReserve = self.guestDao.selectGuestReserv()
        self.refreshTreeTable(guestReserve)

    def refreshTreeTable(self, data: list[GlobalviewDTO]):
        ##clean Table
        for i in self.view.treeTable.get_children():
            self.view.treeTable.delete(i)
        ##from database to table
        for i in range(len(data)):
            self.view.treeTable.insert(parent='', index="end", iid=data[i].id, text=data[i].id, values=(data[i].name, data[i].lastname, data[i].age, data[i].email, data[i].room))
            #print(i, data[i].toString())