class GuestDTO:
    """Data Transfer Object to transfer data between DB and APP
    """

    def __init__(self, name="", lastname="", age=0, email="", password="", id=0, active=1) -> None:
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
        :param active: enable or disabled entry (1 true 0 false)
        :type active: int, optional
        """
        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email
        self.password = password
        self.active = active

    def __repr__(self):
        return f"{self.__class__.__name__}(id={str(self.id)}, " \
            f"name={str(self.name)}, lastname={str(self.lastname)}, " \
            f"age={str(self.age)}, email={str(self.email)}, " \
            f"password={str(self.password)}, active={str(self.active)})"
