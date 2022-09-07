from view.Checkin import Checkin
from model.persistance.DB_Dic import DB_Dict
from model.guestDTO import GuestDTO
from model.guestDAO import GuestDAO


class CheckCtl:
    def __init__(self, view: Checkin, cx) -> None:
        self.view = view
        self.cx = cx

        # Create DB object with existing connection
        self.guestDao = GuestDAO(self.cx)

        self.view.checkInBtn.config(command=self.getGuest)

        self.refreshTreeTable()

    def getGuest(self):
        # print("working!")
        name = self.view.nameTextLabel.get()
        lastname = self.view.lastTextLabel.get()
        room = self.view.roomTextLabel.get()
        guest = GuestDTO(name, lastname, room)
        self.writeToDb(guest)
        self.clearText()
        self.refreshTreeTable()
        #print(name +" " + lastname + " "+room)
        #self.view.treeTable.insert(parent='', index="end", iid=0, text="1", values=(name, lastname, room))

    def writeToDb(self, guest: GuestDTO):
        if isinstance(self.cx, DB_Dict):
            self.guestDao.insert(guest)
        else:
            self.guestDao.insert_SQL(guest)

    def clearText(self):
        self.view.nameTextLabel.delete(0, 'end')
        self.view.lastTextLabel.delete(0, 'end')
        self.view.roomTextLabel.delete(0, 'end')

    def refreshTreeTable(self):
        if isinstance(self.cx, DB_Dict):
            guests = self.guestDao.select_all()
        else:
            guests = self.guestDao.select_all_SQL()

        # clean Table
        for i in self.view.treeTable.get_children():
            self.view.treeTable.delete(i)
        # from database to table
        for i in range(len(guests)):
            self.view.treeTable.insert(parent='', index="end", iid=guests[i].id, text=guests[i].id, values=(
                guests[i].name, guests[i].lastname, guests[i].room))
            #print(i, guests[i].toString())
