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
        self.room_dao = RoomDAO(cx)
        # Needed to bring the list of categories for the dropdownmenu
        self.cat_dao = CategoryDAO(cx)

        self.get_all_rooms()

        # Button actions
        self.view.add_btn.config(command=self.add)
        self.view.update_btn.config(command=self.update)
        self.view.delete_btn.config(command=self.delete)

        # Click Actions on the treeTable
        self.view.tree_table.bind("<ButtonRelease-1>", self.on_one_click)

    def get_all_rooms(self) -> None:
        """SELECT all the rooms from database and print them on the TreeTable
        """
        rooms = self.room_dao.select_all_rooms()
        self.set_options()
        self.refresh_tree_table(rooms)

    def add(self) -> None:
        """Create a new entry in the database with a Room
        """
        addr = self.view.addr_text_field.get()
        desc = self.view.desc_text_field.get()
        size = self.view.size_text_field.get()
        name = self.view.name_text_field.get()
        # Combobox
        cat = self.view.cat_dropdown.get()
        # database index starts in 1 not in 0
        index_cat = self.view.options.index(cat) + 1

        active = self.view.act_text_field.get()

        self.room_dao.insert_room(
            RoomDTO(addr, desc, size, name, index_cat, 0, active))
        self.get_all_rooms()
        self.clear_all()

    def update(self) -> None:
        """UPDATE entry in the DB from the information modified on the GUI
        """
        id = self.view.id_text_field.get()
        addr = self.view.addr_text_field.get()
        desc = self.view.desc_text_field.get()
        size = self.view.size_text_field.get()
        name = self.view.name_text_field.get()
        # Combobox
        cat = self.view.cat_dropdown.get()
        # database index starts in 1 not in 0
        index_cat = self.view.options.index(cat) + 1

        active = self.view.act_text_field.get()
        self.room_dao.update_room(
            RoomDTO(addr, desc, size, name, index_cat, id, active))

        self.get_all_rooms()
        self.clear_all()

    def delete(self) -> None:
        """Soft delete a room in the database
        """
        room_id = self.view.id_text_field.get()
        self.room_dao.delete_room(room_id)
        self.get_all_rooms()
        self.clear_all()

    ###HELPER FUNCTIONS#

    def refresh_tree_table(self, data: list[RoomDTO]) -> None:
        """Refresh (clear and repaint) information on TreeTable

        Args:
            data (list[RoomDTO]): List (Array) of DTOs obtained from the DB
        """
        # clean Table
        for i in self.view.tree_table.get_children():
            self.view.tree_table.delete(i)
        # from List to TreeTable
        for i in range(len(data)):
            self.view.tree_table.insert(parent='', index="end", iid=data[i].id, text=data[i].id,
                                        values=(data[i].address, data[i].description, data[i].size,
                                                data[i].name, data[i].category, data[i].active))
            #print(i, data[i].toString())

    def on_one_click(self, e) -> None:
        """Once an element from the TreeTable is clicked the function will populate the information
        on the text field an dropdown-menu

        Args:
            e (object): Needed for the Treetable function binding
        """
        room = self.get_room_dto()
        self.set_text(room.id, self.view.id_text_field)
        self.set_text(room.address, self.view.addr_text_field)
        self.set_text(room.description, self.view.desc_text_field)
        self.set_text(room.size, self.view.size_text_field)
        self.set_text(room.name, self.view.name_text_field)
        # Set value of combobox
        index = self.view.options.index(room.category)
        self.view.cat_dropdown.current(index)
        self.set_text(room.active, self.view.act_text_field)

    def set_text(self, text: str, e) -> None:
        """Set text for Tkinter elements

        Args:
            text (str): Desired text
            e (object): The destination element where the text should be set
        """
        st = StringVar()
        st.set(text)
        e.config(textvariable=st)

    def set_options(self) -> None:
        """Generate and set the items for the Combobox (dropdown-menu)
        """
        categories = self.cat_dao.select_all_categories()
        names = [i.name for i in categories]  # List comprehension
        self.view.options = names
        self.view.cat_dropdown.config(values=self.view.options)
        self.view.cat_dropdown.current(0)

    def get_room_dto(self) -> RoomDTO:
        """Generate DTO object from clicked element on a Tkinter TreeTable

        Returns:
            RoomDTO: Generated DTO from elements on selected Treetable row
        """
        selected = self.view.tree_table.focus()
        values = self.view.tree_table.item(selected, 'values')
        return (RoomDTO(values[0], values[1], values[2], values[3], values[4], selected, values[5]))

    def clear_all(self) -> None:
        """Set elements to default values after an action (insert, update, delete) has been performed.
        """
        self.set_text("", self.view.id_text_field)
        self.set_text("", self.view.addr_text_field)
        self.set_text("", self.view.desc_text_field)
        self.set_text("", self.view.size_text_field)
        self.set_text("", self.view.name_text_field)
        self.view.cat_dropdown.current(0)
        self.set_text("", self.view.act_text_field)
