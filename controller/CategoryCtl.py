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

        ##Create DB object with existing connection
        self.categoryDao = CategoryDAO(cx)
        self.getAllCategories()


        #Button actions
        self.view.addBtn.config(command=self.add)
        self.view.updateBtn.config(command=self.update)
        self.view.deleteBtn.config(command=self.delete)

        #Click Actions
        self.view.treeTable.bind("<ButtonRelease-1>", self.onOneClick)
    
    
    def getCategoryDto(self) -> CategoryDTO:
        selected = self.view.treeTable.focus()
        values = self.view.treeTable.item(selected, 'values')
        return(CategoryDTO(values[0],values[1], selected, values[2]))
         

    def getAllCategories(self) -> None:
        categories = self.categoryDao.selectAllCategories()
        self.refreshTreeTable(categories)       
        
        
    def add(self)-> None:
        name = self.view.nameTextField.get()
        desc = self.view.descTextField.get()
        self.categoryDao.insertCategory(CategoryDTO(name, desc))  
        self.getAllCategories()
        self.clearAll()
        

    def update(self)-> None:  
        id = self.view.idTextField.get()
        name = self.view.nameTextField.get()
        desc = self.view.descTextField.get()
        active = self.view.activeTextField.get()
        self.categoryDao.updateCategory(CategoryDTO(name,desc,id,active))
        self.getAllCategories()
        self.clearAll()

    def delete(self)-> None:  
        catId = self.view.idTextField.get()
        self.categoryDao.deleteCategory(catId)
        self.getAllCategories()
        self.clearAll()


    ###HELPER FUNCTIONS#
    def refreshTreeTable(self, data: list[CategoryDTO]) -> None:
        """Refresh (clear and repaint) information on TreeTable

        :param data: List of DTOs obtained from the DB
        :type data: list[CategoryDTO]
        """
        ##clean Table
        for i in self.view.treeTable.get_children():
            self.view.treeTable.delete(i)
        ##from database to table
        for i in range(len(data)):
            self.view.treeTable.insert(parent='', index="end", iid=data[i].id, text=data[i].id, values=(data[i].name, data[i].description, data[i].active))
            #print(i, data[i].toString())


    def onOneClick(self, e) -> None:
        """Once an element from the TreeTable is clicked the function will populate the information
        on the next field and dropdown-menu

        :param e: Needed for the Treetable function binding
        :type e: object
        """
        cat = self.getCategoryDto()
        self.setText(cat.id,self.view.idTextField)
        self.setText(cat.name,self.view.nameTextField)
        self.setText(cat.description,self.view.descTextField)
        self.setText(cat.active,self.view.activeTextField)

    def setText(self, text: str, e)->None:
        """Set text for TKinter elements

        :param text: Desired text
        :type text: str
        :param e: The destination element where the text should be set
        :type e: object
        """
        st = StringVar()
        st.set(text)
        e.config(textvariable=st)

    def clearAll(self) -> None:
        """Set elements to default values after an action (insert, update, delete) has been performed.
        """
        self.setText("",self.view.idTextField)
        self.setText("",self.view.nameTextField)
        self.setText("",self.view.descTextField)
        self.setText("",self.view.activeTextField)