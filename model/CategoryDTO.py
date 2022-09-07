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

    def __repr__(self):
        return f"{self.__class__.__name__}(id={str(self.id)}, name={self.name}, " \
            f"description={self.description}, active={str(self.active)})"
