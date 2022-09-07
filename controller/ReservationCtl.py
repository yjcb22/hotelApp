from tkinter import StringVar
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from model.ReservationDAO import ReservationDAO
from model.ReservationDTO import ReservationDTO
from model.RoomDAO import RoomDAO
from model.guestDAO import GuestDAO
from view.Reservations import Reservations
import re


class ReservationsCtl:
    """Controller in the MVC for the rooms in the Hotel. It will handle the logic to transfer
    data between the view and the model/database
    """

    def __init__(self, view: Reservations, cx) -> None:
        """Constructor for the class

        :param view: Instance of the Rooms view class
        :type view: Rooms
        :param cx: Instance of the database connection class
        :type cx: raw connection or specific class DAO
        """
        self.view = view
        self.cx = cx

        # Create DB object with existing connection
        self.reserv_dao = ReservationDAO(cx)
        # Needed to bring the list of rooms for the dropdownmenu
        self.room_dao = RoomDAO(cx)
        # Needed to bring the list of guests for the dropdownmenu
        self.guest_dao = GuestDAO(cx)

        self.populate_data()

        # Button actions
        self.view.add_btn.config(command=self.add)
        self.view.update_btn.config(command=self.update)
        self.view.delete_btn.config(command=self.delete)

        # Click Actions
        self.view.tree_table.bind("<ButtonRelease-1>", self.on_one_click)

    def populate_data(self) -> None:
        """SELECT all the information from database to print it on the view
        """
        # Get reservations
        self.reservations = self.reserv_dao.select_all_reservations()
        #print(*reservations, sep="\n")

        # Get enum values for table columns
        column_data_type = self.reserv_dao.get_column_datatypes()
        # Get list of enum options
        self.score_options = self.enum_to_list(column_data_type["score"])
        self.status_options = self.enum_to_list(column_data_type["status"])
        # Set dropdown meny options for score combobox
        self.set_dropdown_options(self.view.score_dropdown, self.score_options)
        # Set dropdown meny options for status combobox
        self.set_dropdown_options(
            self.view.status_dropdown, self.status_options)

        # Get Rooms
        self.rooms = self.room_dao.select_all_rooms()
        # Extract room names
        self.room_names = [i.name for i in self.rooms if i.active == 1]
        # Set room names in dropdown menu
        self.set_dropdown_options(self.view.room_dropdown, self.room_names)

        # Get guests
        self.guests = self.guest_dao.select_all_SQL()
        # Create list with the names to display in the combobox
        self.guests_names = [i.name+" "+i.lastname +
                             " " + i.email for i in self.guests]
        self.set_dropdown_options(self.view.guest_dropdown, self.guests_names)

        self.refresh_tree_table(self.reservations)

    def add(self) -> None:
        """Create a new Reservation in the database
        """
        start = self.view.start_date.get_date()
        end = self.view.end_date.get_date()
        status = self.view.status_dropdown.get()
        score = self.view.score_dropdown.get()
        room_id = self.get_object_id(
            name=self.view.room_dropdown.get(), options=self.room_names)
        guest_id = self.get_object_id(
            name=self.view.guest_dropdown.get(), options=self.guests_names)
        active = self.view.act_text_field.get()
        self.reserv_dao.insert_reservation(ReservationDTO(start_date=start, devolution_date=end, status=status,
                                                          score=score, id_room=room_id, id_guest=guest_id, active=active))
        self.populate_data()
        self.clear_all()

    def update(self) -> None:
        """UPDATE entry in the DB from the information modified on the GUI
        """
        id = self.view.id_text_field.get()
        start = self.view.start_date.get_date()
        end = self.view.end_date.get_date()
        status = self.view.status_dropdown.get()
        score = self.view.score_dropdown.get()
        room_id = self.get_object_id(
            name=self.view.room_dropdown.get(), options=self.room_names)
        guest_id = self.get_object_id(
            name=self.view.guest_dropdown.get(), options=self.guests_names)
        active = self.view.act_text_field.get()
        self.reserv_dao.update_reservation(ReservationDTO(id=id, start_date=start, devolution_date=end, status=status,
                                                          score=score, id_room=room_id, id_guest=guest_id, active=active))
        self.populate_data()
        self.clear_all()

    def delete(self) -> None:
        """Soft delete a reservation in the database
        """
        reservation_id = self.view.id_text_field.get()
        self.reserv_dao.delete_reservation(reservation_id)
        self.populate_data()
        self.clear_all()

    # ###HELPER FUNCTIONS#

    def refresh_tree_table(self, data: list[ReservationDTO]) -> None:
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
                                        values=(data[i].start_date, data[i].devolution_date, data[i].status,
                                                data[i].score, self.get_room_name(
                                                    data[i].id_room),
                                                self.get_guest_name(data[i].id_guest), data[i].active))

    def on_one_click(self, e) -> None:
        """Once an element from the TreeTable is clicked the function will populate the information
        on the text field an dropdown-menu

        Args:
            e (object): Needed for the Treetable function binding
        """
        reservation = self.get_reservation_dto()
        # print(reservation)

        # ID
        self.set_text(reservation.id, self.view.id_text_field)
        # Set calendar (DateEntry): Start reservation
        self.set_calendar(date=reservation.start_date, e=self.view.start_date)
        # Set calendar (DateEntry): End reservation
        self.set_calendar(date=reservation.devolution_date,
                          e=self.view.end_date)
        # Set combobox: status
        self.set_combobox(text=reservation.status,
                          options=self.status_options, e=self.view.status_dropdown)
        # Set combobox: Score
        self.set_combobox(text=reservation.score,
                          options=self.score_options, e=self.view.score_dropdown)
        # Set combobox: Score
        self.set_combobox(text=reservation.score,
                          options=self.score_options, e=self.view.score_dropdown)
        # Set combobox: Room
        self.set_combobox(text=reservation.room_name,
                          options=self.room_names, e=self.view.room_dropdown)
        # Set combobox: Guest
        self.set_combobox(text=reservation.guest_name,
                          options=self.guests_names, e=self.view.guest_dropdown)
        # Active
        self.set_text(reservation.active, self.view.act_text_field)

    def set_text(self, text: str, e) -> None:
        """Set text for Tkinter elements

        Args:
            text (str): Desired text
            e (object): The destination element where the text should be set
        """
        st = StringVar()
        st.set(text)
        e.config(textvariable=st)

    def set_combobox(self, text: str, e: ttk.Combobox, options: list[str]) -> None:
        """Set option for combobox

        :param text: desired text
        :type text: str
        :param e: comboBox
        :type e: Combobox
        """

        index = options.index(text)
        e.current(index)

    def set_calendar(self, date: str, e: DateEntry):
        """set the date on a Date entry calendar

        :param date: the date in format Y-m-d
        :type date: str
        :param e: DateEntry object
        :type e: DateEntry
        """
        e.set_date(date)

    def set_dropdown_options(self, e: ttk.Combobox, data: list[str]) -> None:
        """Generate and set the items for the Combobox (dropdown-menu)
        """
        # Set score enum options in dropdown menu
        e.config(values=data)
        e.current(0)

    def enum_to_list(self, data: str) -> list[str]:
        """Convert string coming from Mysql as enum to a list so it can be used
        in the combobox

        :param data: string with enum values
        :type data: str
        :return: list of string
        :rtype: list[str]
        """
        column_options = data.split("(")[1]
        column_options = re.sub("[)']", "", column_options).split(",")
        return column_options

    def get_room_name(self, id: str) -> str:
        """Return the name of a room based on the id

        :param id: room id
        :type id: string
        :return: room's name
        :rtype: string
        """
        name = [room.name for room in self.rooms if room.id == id]
        return name[0]

    def get_guest_name(self, id: str) -> str:
        """Return the name of the guest based on the id

        :param id: guest id
        :type id: str
        :return: guest's name
        :rtype: string
        """
        name = [guest.name+" "+guest.lastname+" " +
                guest.email for guest in self.guests if guest.id == id]
        return name[0]

    def get_object_id(self, name: str, options: list[str]) -> int:
        """Return the object id from a list

        :param name: name to check on the list
        :type name: str
        :param options: list of options
        :type options: list[str]
        :return: the object id
        :rtype: int
        """
        # database index starts in 1 not in 0
        return options.index(name) + 1

    def get_reservation_dto(self) -> ReservationDTO:
        """Generate DTO object from clicked element on a Tkinter TreeTable

        Returns:
            RoomDTO: Generated DTO from elements on selected Treetable row
        """
        selected = self.view.tree_table.focus()
        values = self.view.tree_table.item(selected, 'values')
        # print(values)
        return (ReservationDTO(start_date=values[0], devolution_date=values[1], status=values[2],
                               score=values[3], room_name=values[4], guest_name=values[5], active=values[6], id=selected))

    def clear_all(self) -> None:
        """Set elements to default values after an action (insert, update, delete) has been performed.
        """
        self.set_text("", self.view.id_text_field)
        # Set date to today in the expected format
        self.view.start_date.set_date(date.today().strftime("%Y-%m-%d"))
        self.view.end_date.set_date(date.today().strftime("%Y-%m-%d"))
        self.view.status_dropdown.current(0)
        self.view.score_dropdown.current(0)
        self.view.room_dropdown.current(0)
        self.view.guest_dropdown.current(0)
        self.set_text("", self.view.act_text_field)
