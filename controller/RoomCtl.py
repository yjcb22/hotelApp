from tkinter import StringVar
from model.CategoryDAO import CategoryDAO
from model.RoomDAO import RoomDAO
from model.RoomDTO import RoomDTO
from view.Rooms import Rooms


class RoomCtl:
    """Controller in the MVC for the rooms in the Hotel. It will handle the logic to transfer
    data between the view and the model/database
    """

    def __init__(self, view: Rooms, cx) -> None:
        """Constructor for the class

        :param view: Instance of the Rooms view class
        :type view: Rooms
        :param cx: Instance of the database connection class
        :type cx: raw connection or specific class DAO
        """
        self.view = view
        self.cx = cx

        # Create DB object with existing connection
        self.roomDao = RoomDAO(cx)
        # Needed to bring the list of categories for the dropdownmenu
        self.catDao = CategoryDAO(cx)
        self.getAllRooms()

        # Button actions
        self.view.addBtn.config(command=self.add)
        self.view.updateBtn.config(command=self.update)
        self.view.deleteBtn.config(command=self.delete)

        # Click Actions
        self.view.treeTable.bind("<ButtonRelease-1>", self.onOneClick)

    def getAllRooms(self) -> None:
        """SELECT all the rooms from database and print them on the TreeTable
        """
        rooms = self.roomDao.selectAllRooms()
        self.setOptions()
        self.refreshTreeTable(rooms)

    def add(self) -> None:
        name = self.view.addrTextField.get()
        desc = self.view.addrTextField.get()
        self.roomDao.insertCategory(CategoryDTO(name, desc))
        self.getAllRooms()
        self.clearAll()

    def update(self) -> None:
        """UPDATE entry in the DB from the information modified on the GUI
        """
        id = self.view.idTextField.get()
        addr = self.view.addrTextField.get()
        desc = self.view.descTextField.get()
        size = self.view.sizeTextField.get()
        name = self.view.nameTextField.get()
        # Combobox
        cat = self.view.catDropdown.get()
        # database index starts in 1 not in 0
        indexCat = self.view.options.index(cat) + 1

        active = self.view.actTextField.get()
        self.roomDao.updateRoom(
            RoomDTO(addr, desc, size, name, indexCat, id, active))

        self.getAllRooms()
        self.clearAll()

    def delete(self) -> None:
        roomId = self.view.idTextField.get()
        self.roomDao.deleteRoom(roomId)
        self.getAllRooms()
        self.clearAll()

    ###HELPER FUNCTIONS#

    def refreshTreeTable(self, data: list[RoomDTO]) -> None:
        """Refresh (clear and repaint) information on TreeTable

        Args:
            data (list[RoomDTO]): List (Array) of DTOs obtained from the DB
        """
        # clean Table
        for i in self.view.treeTable.get_children():
            self.view.treeTable.delete(i)
        # from List to TreeTable
        for i in range(len(data)):
            self.view.treeTable.insert(parent='', index="end", iid=data[i].id, text=data[i].id,
                                       values=(data[i].address, data[i].description, data[i].size,
                                               data[i].name, data[i].category, data[i].active))
            #print(i, data[i].toString())

    def onOneClick(self, e) -> None:
        """Once an element from the TreeTable is clicked the function will populate the information
        on the text field an dropdown-menu

        Args:
            e (object): Needed for the Treetable function binding
        """
        room = self.getRoomDto()
        self.setText(room.id, self.view.idTextField)
        self.setText(room.address, self.view.addrTextField)
        self.setText(room.description, self.view.descTextField)
        self.setText(room.size, self.view.sizeTextField)
        self.setText(room.name, self.view.nameTextField)
        # Set value of combobox
        index = self.view.options.index(room.category)
        self.view.catDropdown.current(index)
        self.setText(room.active, self.view.actTextField)

    def setText(self, text: str, e) -> None:
        """Set text for Tkinter elements

        Args:
            text (str): Desired text
            e (object): The destination element where the text should be set
        """
        st = StringVar()
        st.set(text)
        e.config(textvariable=st)

    def setOptions(self) -> None:
        """Generate and set the items for the Combobox (dropdown-menu)
        """
        categories = self.catDao.selectAllCategories()
        names = [i.name for i in categories]  # List comprehension
        self.view.options = names
        self.view.catDropdown.config(values=self.view.options)
        self.view.catDropdown.current(0)

    def getRoomDto(self) -> RoomDTO:
        """Generate DTO object from clicked element on a Tkinter TreeTable

        Returns:
            RoomDTO: Generated DTO from elements on selected Treetable row
        """
        selected = self.view.treeTable.focus()
        values = self.view.treeTable.item(selected, 'values')
        return (RoomDTO(values[0], values[1], values[2], values[3], values[4], selected, values[5]))

    def clearAll(self) -> None:
        """Set elements to default values after an action (insert, update, delete) has been performed.
        """
        self.setText("", self.view.idTextField)
        self.setText("", self.view.addrTextField)
        self.setText("", self.view.descTextField)
        self.setText("", self.view.sizeTextField)
        self.setText("", self.view.nameTextField)
        self.view.catDropdown.current(0)
        self.setText("", self.view.actTextField)
