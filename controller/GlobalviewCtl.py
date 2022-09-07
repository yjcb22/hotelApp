from controller.GuestCtl import GuestCtl
from controller.ReservationCtl import ReservationsCtl
from model.GlobalviewDTO import GlobalviewDTO
from model.guestDAO import GuestDAO
from controller.CategoryCtl import CategoryCtl
from controller.RoomCtl import RoomCtl
from view.Categories import Categories
from view.GlobalView import GlobalView
from view.Guests import Guests
from view.Rooms import Rooms
from view.Reservations import Reservations


class GlobalviewCtl:
    """Controller for the Globalview
    """

    def __init__(self, view: GlobalView, cx) -> None:
        """Constructor

        :param view: Instance of the Globalview class
        :type view: GlobalView
        :param cx: Instance of the database connection class
        :type cx: raw connection or specific class DAO
        """
        self.view = view
        # Check if it is a raw database connection
        if isinstance(cx, GuestDAO):
            self.guest_dao = cx
        else:
            # Create DB object with existing connection
            self.guest_dao = GuestDAO(cx)

        # Bring all the information to popularte the view information
        self.get_all_guests_rev()

        # Button actions
        self.view.category_btn.config(command=self.open_category)
        self.view.rooms_btn.config(command=self.open_room)
        self.view.guest_btn.config(command=self.open_guests)
        self.view.reservations_btn.config(command=self.open_reservations)

    def get_all_guests_rev(self) -> None:
        """Get list of DTO objects from the database with clients and reservations
        """
        guest_reserve = self.guest_dao.select_guest_reserv()
        self.refresh_tree_table(guest_reserve)

    def refresh_tree_table(self, data: list[GlobalviewDTO]) -> None:
        """Clear and refresh TreeTable 

        :param data: List of DTO objects to display
        :type data: list[GlobalviewDTO]
        """
        # clean Table
        for i in self.view.tree_table.get_children():
            self.view.tree_table.delete(i)
        # from database to table
        for i in range(len(data)):
            self.view.tree_table.insert(parent='', index="end", iid=data[i].id, text=data[i].id, values=(
                data[i].name, data[i].lastname, data[i].age, data[i].email, data[i].room))

    def open_category(self) -> None:
        """Trigger the new view for Categories
        """
        # get the original CX from Dao object
        cx = self.guest_dao.db
        CategoryCtl(Categories(), cx)

    def open_room(self) -> None:
        """Trigger the new view for Rooms
        """

        # get the original CX from Dao object
        cx = self.guest_dao.db
        RoomCtl(Rooms(), cx)

    def open_guests(self) -> None:
        """Trigger the new view for Guests
        """
        # get the original CX from Dao object
        cx = self.guest_dao.db
        GuestCtl(Guests(), cx)

    def open_reservations(self) -> None:
        """Trigger the new view for Reservations
        """
        # get the original CX from Dao object
        cx = self.guest_dao.db
        ReservationsCtl(Reservations(), cx)
