class ReservationDTO:
    """Data Transfer Object to transfer data between DB and APP
    """

    def __init__(self, start_date=None, devolution_date=None, score=None, status=None, active=1, id_room=None, room_name=None, id_guest=None, guest_name=None, id=None) -> None:
        """Constructor

        :param start_date: initial date for reservation, defaults to ""
        :type start_date: str, optional
        :param devolution_date: last date for reservation, defaults to ""
        :type devolution_date: str, optional
        :param score: reservation score, defaults to ""
        :type score: str, optional
        :param status: reservation status, defaults to ""
        :type status: str, optional
        :param active: True (1) or False (0), defaults to 1
        :type active: int, optional
        :param id_room: room associated with the reservation, defaults to 0
        :type id_room: int, optional
        :param id_guest: guest associated with the reservation, defaults to 1
        :type id_guest: int, optional
        :param id: reservation internal id, defaults to 0
        :type id: int, optional
        """
        self.id = id
        self.start_date = start_date
        self.devolution_date = devolution_date
        self.score = score
        self.status = status
        self.active = active
        self.id_room = id_room
        self.room_name = room_name
        self.id_guest = id_guest
        self.guest_name = guest_name

    def __repr__(self):
        return f"{self.__class__.__name__}(id={str(self.id)}, start_date={str(self.start_date)}, " \
            f"devolution_date={self.devolution_date}, score={str(self.score)}, " \
            f"status={self.status}, id_room={str(self.id_room)}, room_name={str(self.room_name)}, " \
            f"id_guest={str(self.id_guest)}, guest_name={str(self.guest_name)}, active={str(self.active)})"
