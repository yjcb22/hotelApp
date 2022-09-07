class GlobalviewDTO:
    """Data Transfer Object to transfer data between DB and APP
    """

    def __init__(self, name="", lastname="", email="", id=0, age=0, room=0) -> None:
        """Constructor

        :param name: guest name, defaults to ""
        :type name: str, optional
        :param lastname: guest lastname, defaults to ""
        :type lastname: str, optional
        :param email: guest email, defaults to ""
        :type email: str, optional
        :param id: guest id, defaults to 0
        :type id: int, optional
        :param age: guest age, defaults to 0
        :type age: int, optional
        :param room: room id, defaults to 0
        :type room: int, optional
        """
        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email
        self.room = room

    def __repr__(self):
        return f"{self.__class__.__name__}(id={str(self.id)}, " \
            f"name={self.name}, lastname={str(self.lastname)}, " \
            f"age={str(self.age)}), email={str(self.email)}, room={str(self.room)})"
