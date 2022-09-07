from typing import Dict
from model.ReservationDTO import ReservationDTO
from mysql.connector import FieldType

from model.guestDTO import GuestDTO


class ReservationDAO:
    """Class to access the DB for any query related to reservations
    """

    def __init__(self, db) -> None:
        """Constructor

        :param db: raw DB connection
        :type db: DB_Mysql class
        """
        self.db = db

        # SQL STATEMENTS
        self.SQL_SELECT = "SELECT Reservations.id_reservation, Reservations.start_date, Reservations.devolution_date, \
        Reservations.score, Reservations.status, Reservations.active, Reservations.id_room AS 'Room', \
        Reservations.id_guest AS 'Guest' FROM hotel.Reservations"
        self.SQL_DATA_TYPE = "DESCRIBE Reservations"
        self.SQL_INSERT = "INSERT INTO Reservations (start_date, devolution_date, score, status, active, id_room, id_guest) \
        VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.SQL_DELETE_SOFT = "UPDATE Reservations SET active=false WHERE id_reservation=%s"
        self.SQL_UPDATE = "UPDATE Reservations SET start_date=%s, devolution_date=%s, score=%s,\
        status=%s, active=%s, id_room=%s, id_guest=%s WHERE id_reservation=%s"

#####################SQL##########################


###SELECT####

    def select_all_reservations(self) -> list[ReservationDTO]:
        """SELECT all the reservations from the table

        :return: List of DTO objects from result in the DB
        :rtype: list[ReservationDTO]
        """
        reservations = []
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_SELECT)
        result = cur.fetchall()
        for i in result:
            reservations.append(ReservationDTO(
                id=i[0], start_date=i[1], devolution_date=i[2], score=i[3],
                status=i[4], active=i[5], id_room=i[6], id_guest=i[7]))
        return reservations

    def get_column_datatypes(self) -> Dict[str, str]:
        """Return the datatypes of the columns

        :return: dictionary with column name and type 
        :rtype: Dict[str, str]
        """
        column_types = {}
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_DATA_TYPE)
        result = cur.fetchall()
        for i in result:
            column_types[i[0]] = str(i[1], 'UTF-8')
        return column_types


# ##INSERT###

    def insert_reservation(self, reservation: ReservationDTO) -> None:
        """INSERT a new reservation to the DB

        :param reservation: DTO object to insert
        :type reservation: ReservationDTO
        """
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_INSERT, (reservation.start_date, reservation.devolution_date, reservation.score,
                                      reservation.status, reservation.active, reservation.id_room, reservation.id_guest))
        self.db.cx.commit()

# DELETE
    def delete_reservation(self, id: int) -> None:
        """SOFT DELETE. It will just enable or disable the entry

        :param id: Room ID
        :type id: int
        """
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_DELETE_SOFT, (id,))
        self.db.cx.commit()

# UPDATE
    def update_reservation(self, reservation: ReservationDTO) -> None:
        """UPDATE entry on the DB

        :param guest: DTO object with information to update
        :type gues: guestDTO
        """
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_UPDATE, (reservation.start_date, reservation.devolution_date, reservation.score,
                                      reservation.status, reservation.active, reservation.id_room,
                                      reservation.id_guest, reservation.id))
        self.db.cx.commit()
