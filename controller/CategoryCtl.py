from tkinter import StringVar
from model.CategoryDAO import CategoryDAO
from model.CategoryDTO import CategoryDTO
from view.Categories import Categories


class CategoryCtl:
    """Controller for the Categories
    """

    def __init__(self, view: Categories, cx) -> None:
        """Constructor

        :param view: Instance of the Categories view class
        :type view: Categories
        :param cx: Instance of the database connection class
        :type cx: raw connection or specific class DAO
        """
        self.view = view
        self.cx = cx

        # Create DB object with existing connection
        self.category_dao = CategoryDAO(cx)
        self.get_all_categories()

        # Button actions
        self.view.add_btn.config(command=self.add)
        self.view.update_btn.config(command=self.update)
        self.view.delete_btn.config(command=self.delete)

        # Click Actions on table
        self.view.tree_table.bind("<ButtonRelease-1>", self.on_one_click)

    def get_category_dto(self) -> CategoryDTO:
        """It will return a category DTO from a click on the table

        :return: Category dto created from the information in the table
        :rtype: CategoryDTO
        """
        selected = self.view.tree_table.focus()
        values = self.view.tree_table.item(selected, 'values')
        return (CategoryDTO(values[0], values[1], selected, values[2]))

    def get_all_categories(self) -> None:
        """Bring al the categories found in the database
        """
        categories = self.category_dao.select_all_categories()
        self.refresh_tree_table(categories)

    def add(self) -> None:
        """Create a new category in the database
        """
        name = self.view.name_text_field.get()
        desc = self.view.desc_text_field.get()
        self.category_dao.insert_category(CategoryDTO(name, desc))
        self.get_all_categories()
        self.clear_all()

    def update(self) -> None:
        """Update an existing entry in the database
        """
        id = self.view.id_text_field.get()
        name = self.view.name_text_field.get()
        desc = self.view.desc_text_field.get()
        active = self.view.active_text_field.get()
        self.category_dao.update_category(CategoryDTO(name, desc, id, active))
        self.get_all_categories()
        self.clear_all()

    def delete(self) -> None:
        """Soft delete an existing category in the db
        """
        catId = self.view.id_text_field.get()
        self.category_dao.delete_category(catId)
        self.get_all_categories()
        self.clear_all()

    ###HELPER FUNCTIONS#

    def refresh_tree_table(self, data: list[CategoryDTO]) -> None:
        """Refresh (clear and repaint) information on TreeTable

        :param data: List of DTOs obtained from the DB
        :type data: list[CategoryDTO]
        """
        # clean Table
        for i in self.view.tree_table.get_children():
            self.view.tree_table.delete(i)
        # from database to table
        for i in range(len(data)):
            self.view.tree_table.insert(parent='', index="end", iid=data[i].id, text=data[i].id, values=(
                data[i].name, data[i].description, data[i].active))
            #print(i, data[i].toString())

    def on_one_click(self, e) -> None:
        """Once an element from the TreeTable is clicked the function will populate the information
        on the next field and dropdown-menu

        :param e: Needed for the Treetable function binding
        :type e: object
        """
        cat = self.get_category_dto()
        self.set_text(cat.id, self.view.id_text_field)
        self.set_text(cat.name, self.view.name_text_field)
        self.set_text(cat.description, self.view.desc_text_field)
        self.set_text(cat.active, self.view.active_text_field)

    def set_text(self, text: str, e) -> None:
        """Set text for TKinter elements

        :param text: Desired text
        :type text: str
        :param e: The destination element where the text should be set
        :type e: object
        """
        st = StringVar()
        st.set(text)
        e.config(textvariable=st)

    def clear_all(self) -> None:
        """Set elements to default values after an action (insert, update, delete) has been performed.
        """
        self.set_text("", self.view.id_text_field)
        self.set_text("", self.view.name_text_field)
        self.set_text("", self.view.desc_text_field)
        self.set_text("", self.view.active_text_field)
