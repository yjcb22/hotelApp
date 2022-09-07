from model.GlobalviewDTO import GlobalviewDTO
from model.guestDTO import GuestDTO
from model.persistance.DB_Dic import DB_Dict
from model.persistance.DB_Mysql import DB_Mysql
from model.persistance.DB_SqlLite import DB_Sqlite


class GuestDAO:
    """Class to access the DB for any query related to guests
    """

    def __init__(self, db) -> None:
        """Constructor

        :param db: raw DB connection
        :type db: DB_Mysql class
        """
        if isinstance(db, DB_Dict):
            self.db = db.database
            self.counter = 0
        elif isinstance(db, DB_Sqlite):
            # SQL STATEMENTS
            self.SQL_INSERT = "INSERT INTO guest (name, lastname, room) VALUES(?, ?, ?)"
            self.db = db
        elif isinstance(db, DB_Mysql):
            self.SQL_INSERT = "INSERT INTO guest (name, lastname, room) VALUES(%s, %s, %s)"
            self.db = db

        # SQL STATEMENTS
        self.SQL_SELECT = "SELECT * FROM Guests"
        self.SQL_SELECT_ONE = "SELECT id, name, lastname, room FROM Guests WHERE id=?"
        self.SQL_SELECT_PASSWORD = "SELECT id_guest, name, lastname, age, email, password FROM Guests WHERE email=%s AND password=%s"
        self.SQL_SELECT_GLOBALVIEW = "SELECT Reservations.id_reservation, Guests.name, Guests.lastname, Guests.age, Guests.email, Reservations.id_room FROM hotel.Guests INNER JOIN hotel.Reservations ON hotel.Guests.id_guest = hotel.Reservations.id_guest"
        self.SQL_SELECT_CATEGORY = "SELECT id_category, name, description, active from Categories"

        self.SQL_UPDATE = "UPDATE Guests SET name=%s, lastname=%s, age=%s,\
        email=%s, password=%s, active=%s WHERE id_guest=%s"
        self.SQL_INSERT_GUEST = "INSERT INTO Guests (name, lastname, age, email, password, active) \
        VALUES (%s, %s, %s, %s, %s, %s)"

        self.SQL_INSERT_CATEGORY = "INSERT INTO Categories (name, description) VALUES (%s, %s)"
        self.SQL_DELETE_SOFT = "UPDATE Guests SET active=false WHERE id_guest=%s"


##DICTIONARY##


    def insert(self, guest: GuestDTO) -> None:
        """Insert data to the dictionary that simulates a database

        :param guest: guest dto object to add to the database
        :type guest: GuestDTO
        """
        self.db[self.counter] = {'id': self.counter,
                                 'name': guest.name,
                                 'lastname': guest.lastname,
                                 'room': guest.room
                                 }
        self.counter += 1

    def select_all(self) -> list[GuestDTO]:
        """Bring all the Guest in the database

        :return: a list of objectes with all the guests found in the db
        :rtype: list[GuestDTO]
        """
        guests = []
        for key in self.db:
            guest_dto = GuestDTO(self.db[key]['name'], self.db[key]
                                 ['lastname'], self.db[key]['room'], self.db[key]['id'])
            guests.append(guest_dto)
            # print(guestDto.toString())
        return guests

    def select_by_Id(self, id: int) -> GuestDTO:
        """Return one guest by ID

        :param id: guest id
        :type id: int
        :return: guest dto with database record
        :rtype: GuestDTO
        """
        guest_dto = GuestDTO(
            self.db[id]['name'], self.db[id]['lastname'], self.db[id]['room'])
        return guest_dto

    # DELETE

    # UPDATE

#####################SQL##########################

#############
###SELECT####
############

    def select_all_SQL(self) -> list[GuestDTO]:
        """SELECT all the guests from the table

        :return: List of DTO objects from the result in the DB
        :rtype: list[GuestDTO]
        """
        guests = []
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_SELECT)
        result = cur.fetchall()
        for i in result:
            guest_dto = GuestDTO(
                name=i[1], lastname=i[2], age=i[3], email=i[4], password=i[5], id=i[0], active=i[6])
            guests.append(guest_dto)
        return guests

    def validate_credentials(self, guest: GuestDTO) -> list[GuestDTO]:
        """SELECT used to allow login to the application

        :param guest: DTO with the guest to validate
        :type guest: GuestDTO
        :return: List of matching users
        :rtype: list[GuestDTO]
        """
        guests = []
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_SELECT_PASSWORD, (guest.email, guest.password))
        result = cur.fetchall()
        #print("result ",result)
        for i in result:
            guest_dto = GuestDTO(i[1], i[2], i[3], i[4], i[5], i[0])
            guests.append(guest_dto)
        return guests

    def select_guest_reserv(self) -> list[GlobalviewDTO]:
        """SELECT to bring a summary of the guest with reservations on the glovalview
        uppon login

        :return: List of DTO objects to show in the GlobalView GUI
        :rtype: list[GlobalviewDTO]
        """
        guest_reserve = []
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_SELECT_GLOBALVIEW)
        result = cur.fetchall()
        for i in result:
            guest_reserve.append(GlobalviewDTO(
                i[1], i[2], i[4], i[0], i[3], i[5]))
        return guest_reserve


###############
##INSERT###
##############

    def insert_SQL(self, guest: GuestDTO) -> None:
        """Insert a new entry in the database with SQL lite

        :param guest: guest dto to add in the database
        :type guest: GuestDTO
        """
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_INSERT, (guest.name, guest.lastname, guest.room))
        self.db.cx.commit()
        # self.db.cx.close()

    def insert_guest_SQL(self, guest: GuestDTO) -> None:
        """INSERT a new room to the DB

        :param room: DTO object to insert
        :type room: GuestDTO
        """
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_INSERT_GUEST, (guest.name, guest.lastname,
                    guest.age, guest.email, guest.password, guest.active))
        self.db.cx.commit()


# UPDATE


    def update_guest_SQL(self, guest: GuestDTO) -> None:
        """UPDATE entry on the DB

        :param room: DTO object with information to update
        :type room: GuestDTO
        """
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_UPDATE, (guest.name, guest.lastname,
                    guest.age, guest.email, guest.password, guest.active, guest.id))
        self.db.cx.commit()


# DELETE

    def delete_guest_SQL(self, id: int) -> None:
        """SOFT DELETE. It will just enable or disable the entry

        :param id: Guest ID
        :type id: int
        """
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_DELETE_SOFT, (id,))
        self.db.cx.commit()
