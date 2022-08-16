from model.RoomDTO import RoomDTO


class RoomDAO:
    """Class to access the DB for any query related to rooms
    """

    def __init__(self, db) -> None:
        """Constructor

        :param db: raw DB connection
        :type db: DB_Mysql class
        """
        self.db = db

        # SQL STATEMENTS
        self.SQL_SELECT = "SELECT Rooms.id_room, Rooms.address, Rooms.description, \
        Rooms.size, Rooms.name, Rooms.active, Categories.name AS 'Room' FROM hotel.Rooms \
        INNER JOIN hotel.Categories ON hotel.Rooms.id_category = hotel.Categories.id_category"
        self.SQL_INSERT = "INSERT INTO Categories (name, description, active) VALUES (%s, %s, %s)"
        self.SQL_DELETE_SOFT = "UPDATE Rooms SET active=false WHERE id_room=%s"
        self.SQL_UPDATE = "UPDATE Rooms SET address=%s, description=%s, size=%s,\
        name=%s, active=%s, id_category=%s WHERE id_room=%s"

#####################SQL##########################


###SELECT####

    def selectAllRooms(self) -> list[RoomDTO]:
        """SELECT all the rooms from the table

        :return: List of DTO objects from result in the DB
        :rtype: list[RoomDTO]
        """
        categories = []
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_SELECT)
        result = cur.fetchall()
        for i in result:
            categories.append(
                RoomDTO(i[1], i[2], i[3], i[4], i[6], i[0], i[5]))
        return categories


##INSERT###

    def insertRoom(self, room: RoomDTO) -> None:
        """INSERT a new room to the DB

        :param room: DTO object to insert
        :type room: RoomDTO
        """
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_INSERT, (room.name,
                    room.description, room.active))
        self.db.cx.commit()

# DELETE
    def deleteRoom(self, id: int) -> None:
        """SOFT DELETE. It will just enable or disable the entry

        :param id: Room ID
        :type id: int
        """
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_DELETE_SOFT, (id,))
        self.db.cx.commit()

# UPDATE
    def updateRoom(self, room: RoomDTO) -> None:
        """UPDATE entry on the DB

        :param room: DTO object with information to update
        :type room: RoomDTO
        """
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_UPDATE, (room.address, room.description, room.size,
                                      room.name, room.active, room.category, room.id))
        self.db.cx.commit()
