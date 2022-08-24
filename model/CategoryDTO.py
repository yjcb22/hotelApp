class CategoryDTO:
    """Data Transfer Object to transfer data between DB and APP
    """

    def __init__(self, name="", description="", id=0, active=1) -> None:
        """Constructor

        :param name: Category name, defaults to ""
        :type name: str, optional
        :param description: Category description, defaults to ""
        :type description: str, optional
        :param id: Category id, defaults to 0
        :type id: int, optional
        :param active: Category status, defaults to 1
        :type active: int, optional
        """
        self.id = id
        self.name = name
        self.description = description
        self.active = active

    def toString(self) -> str:
        """Show the object as a String

        :return: String with the object information
        :rtype: str
        """
        return "CategoryDTO{" + "id=" + str(self.id) + ", name=" + self.name + ", description=" + self.description + ", active=" + self.active + '}'
