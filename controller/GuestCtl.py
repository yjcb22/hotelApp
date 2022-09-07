from tkinter import StringVar
from model.guestDAO import GuestDAO
from model.guestDTO import GuestDTO
from view.Guests import Guests


class GuestCtl:
    """Controller in the MVC for the rooms in the Hotel. It will handle the logic to transfer
    data between the view and the model/database
    """

    def __init__(self, view: Guests, cx) -> None:
        """Constructor for the class

        :param view: Instance of the Guests view class
        :type view: Guests
        :param cx: Instance of the database connection class
        :type cx: raw connection or specific class DAO
        """
        self.view = view
        self.cx = cx

        # Create DB object with existing connection
        self.guest_dao = GuestDAO(cx)

        self.get_all_guests()

    #     # Button actions
        self.view.add_btn.config(command=self.add)
        self.view.update_btn.config(command=self.update)
        self.view.delete_btn.config(command=self.delete)

        # Click Actions
        self.view.tree_table.bind("<ButtonRelease-1>", self.on_one_click)

    def get_all_guests(self) -> None:
        """SELECT all the guests from database and print them on the TreeTable
        """
        guests = self.guest_dao.select_all_SQL()
        self.refresh_tree_table(guests)

    def add(self) -> None:
        """Add a new entry in the database with a guest
        """
        name = self.view.name_text_field.get()
        lastname = self.view.last_text_field.get()
        age = self.view.age_text_field.get()
        email = self.view.email_text_field.get()
        password = self.view.password_text_field.get()
        active = self.view.active_text_field.get()

        self.guest_dao.insert_guest_SQL(GuestDTO(
            id=0, name=name, lastname=lastname, age=age, email=email, password=password, active=active))
        self.get_all_guests()
        self.clear_all()

    def update(self) -> None:
        """UPDATE entry in the DB from the information modified on the GUI
        """
        id = self.view.id_text_field.get()
        name = self.view.name_text_field.get()
        lastname = self.view.last_text_field.get()
        age = self.view.age_text_field.get()
        email = self.view.email_text_field.get()
        password = self.view.password_text_field.get()
        active = self.view.active_text_field.get()

        self.guest_dao.update_guest_SQL(GuestDTO(
            id=id, name=name, lastname=lastname, age=age, email=email, password=password, active=active))

        self.get_all_guests()
        self.clear_all()

    def delete(self) -> None:
        """Soft delete a guest in the database
        """
        guest_id = self.view.id_text_field.get()
        self.guest_dao.delete_guest_SQL(guest_id)
        self.get_all_guests()
        self.clear_all()

    # ###HELPER FUNCTIONS#

    def refresh_tree_table(self, data: list[GuestDTO]) -> None:
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
                                        values=(data[i].name, data[i].lastname, data[i].age,
                                                data[i].email, data[i].password, data[i].active))

    def on_one_click(self, e) -> None:
        """Once an element from the TreeTable is clicked the function will populate the information
        on the text field an dropdown-menu

        Args:
            e (object): Needed for the Treetable function binding
        """
        guest = self.get_guest_dto()
        # print(guest)
        self.set_text(guest.id, self.view.id_text_field)
        self.set_text(guest.name, self.view.name_text_field)
        self.set_text(guest.lastname, self.view.last_text_field)
        self.set_text(guest.age, self.view.age_text_field)
        self.set_text(guest.email, self.view.email_text_field)
        self.set_text(guest.password, self.view.password_text_field)
        self.set_text(guest.active, self.view.active_text_field)

    def set_text(self, text: str, e) -> None:
        """Set text for Tkinter elements

        Args:
            text (str): Desired text
            e (object): The destination element where the text should be set
        """
        st = StringVar()
        st.set(text)
        e.config(textvariable=st)

    def get_guest_dto(self) -> GuestDTO:
        """Generate DTO object from clicked element on a Tkinter TreeTable

        Returns:
            GuestDTO: Generated DTO from elements on selected Treetable row
        """
        selected = self.view.tree_table.focus()
        values = self.view.tree_table.item(selected, 'values')
        # print(values)
        return (GuestDTO(id=selected, name=values[0], lastname=values[1], age=values[2], email=values[3], password=values[4], active=values[5]))

    def clear_all(self) -> None:
        """Set elements to default values after an action (insert, update, delete) has been performed.
        """
        self.set_text("", self.view.id_text_field)
        self.set_text("", self.view.name_text_field)
        self.set_text("", self.view.last_text_field)
        self.set_text("", self.view.age_text_field)
        self.set_text("", self.view.email_text_field)
        self.set_text("", self.view.password_text_field)
        self.set_text("", self.view.active_text_field)
