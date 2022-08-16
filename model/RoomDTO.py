class RoomDTO:
    """Data Transfer Object to transfer data between DB and APP
    """

    def __init__(self, address="", description="", size="", name="", category=0, id=0, active=1) -> None:
        """Constuctor

        :param address: room address, defaults to ""
        :type address: str, optional
        :param description: room description, defaults to ""
        :type description: str, optional
        :param size: room size, defaults to ""
        :type size: str, optional
        :param name: room name, defaults to ""
        :type name: str, optional
        :param category: room category, defaults to ""
        :type category: int, optional
        :param id: room id, defaults to 0
        :type id: int, optional
        :param active: room status, defaults to 1
        :type active: int, optional
        """
        self.id = id
        self.address = address
        self.description = description
        self.size = size
        self.name = name
        self.category = category
        self.active = active

    def toString(self) -> str:
        """Show the object as a String

        :return: String with the object information
        :rtype: str
        """
        return "RoomDTO{" + "id=" + str(self.id) + ", address=" + str(self.address) + \
            ", description=" + self.description + ", size=" + str(self.size) + \
            ", name=" + self.name + ", category=" + str(self.category) + \
            ", active=" + str(self.active) + '}'
