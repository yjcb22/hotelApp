from model.CategoryDTO import CategoryDTO


class CategoryDAO:
    """Class to access the DB for any query related to Categories
    """

    def __init__(self, db) -> None:
        """Constructor

        :param db: raw DB connection
        :type db: DB_Mysql class
        """
        self.db = db

        # SQL STATEMENTS
        self.SQL_SELECT_CATEGORY = "SELECT id_category, name, description, active from Categories"
        self.SQL_INSERT_CATEGORY = "INSERT INTO Categories (name, description, active) VALUES (%s, %s, %s)"
        self.SQL_DELETE_SOFT = "UPDATE Categories SET active=false WHERE id_category=%s"
        self.SQL_UPDATE = "UPDATE Categories SET name=%s, description=%s, active=%s WHERE id_category=%s"

#####################SQL##########################


###SELECT####


    def select_all_categories(self) -> list[CategoryDTO]:
        """SELECT all the categories from the table

        :return: List of DTO objects from result in the DB
        :rtype: list[CategoryDTO]
        """
        categories = []
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_SELECT_CATEGORY)
        result = cur.fetchall()
        for i in result:
            categories.append(CategoryDTO(i[1], i[2], i[0], i[3]))
        return categories


##INSERT###


    def insert_category(self, category: CategoryDTO) -> None:
        """INSERT  new category in the DB

        :param category: DTO object to insert
        :type category: CategoryDTO
        """
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_INSERT_CATEGORY, (category.name,
                    category.description, category.active))
        self.db.cx.commit()

# DELETE
    def delete_category(self, id: int) -> None:
        """SOFT DELETE. It will just enable or disable the entry

        :param id: Category ID
        :type id: int
        """
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_DELETE_SOFT, (id,))
        self.db.cx.commit()

# UPDATE
    def update_category(self, category: CategoryDTO) -> None:
        """UPDATE entry on the DB

        :param category: DTO object with the information to update
        :type category: CategoryDTO
        """
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_UPDATE, (category.name,
                    category.description, category.active, category.id))
        self.db.cx.commit()
