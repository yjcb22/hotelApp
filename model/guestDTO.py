class GuestDTO:
    """Data Transfer Object to transfer data between DB and APP
    """

    def __init__(self, name="", lastname="", age=0, email="", password="", id=0) -> None:
        """Constructor

        :param name: guest name, defaults to ""
        :type name: str, optional
        :param lastname: guest lastname, defaults to ""
        :type lastname: str, optional
        :param age: guest age, defaults to 0
        :type age: int, optional
        :param email: guest email, defaults to ""
        :type email: str, optional
        :param password: guest password, defaults to ""
        :type password: str, optional
        :param id: guest id, defaults to 0
        :type id: int, optional
        """
        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email
        self.password = password

    def toString(self) -> str:
        """Show the object as a String

        :return: String with the object information
        :rtype: str
        """
        return "GuestDTO{" + "id=" + str(self.id) + ", name=" + self.name + ", lastname=" + self.lastname + ", age=" + str(self.age) + ", email=" + self.email + ", password=" + self.password + '}'
