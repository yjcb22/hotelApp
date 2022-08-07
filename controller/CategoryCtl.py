from tkinter import StringVar
from model.CategoryDAO import CategoryDAO
from model.CategoryDTO import CategoryDTO
from view.Categories import Categories


class CategoryCtl:
    def __init__(self, view: Categories, cx) -> None:
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
    
    def onOneClick(self, e) -> None:
        cat = self.getCategoryDto()
        self.setText(cat.id,self.view.idTextField)
        self.setText(cat.name,self.view.nameTextField)
        self.setText(cat.description,self.view.descTextField)
        self.setText(cat.active,self.view.activeTextField)
    

    def setText(self, text: str, e)->None:
        st = StringVar()
        st.set(text)
        e.config(textvariable=st)


    def getCategoryDto(self) -> CategoryDTO:
        selected = self.view.treeTable.focus()
        values = self.view.treeTable.item(selected, 'values')
        return(CategoryDTO(values[0],values[1], selected, values[2]))
         

    def getAllCategories(self) -> None:
        categories = self.categoryDao.selectAllCategories()
        self.refreshTreeTable(categories)

    def refreshTreeTable(self, data: list[CategoryDTO]) -> None:
        ##clean Table
        for i in self.view.treeTable.get_children():
            self.view.treeTable.delete(i)
        ##from database to table
        for i in range(len(data)):
            self.view.treeTable.insert(parent='', index="end", iid=data[i].id, text=data[i].id, values=(data[i].name, data[i].description, data[i].active))
            #print(i, data[i].toString())
    
    def clearAll(self) -> None:
        self.setText("",self.view.idTextField)
        self.setText("",self.view.nameTextField)
        self.setText("",self.view.descTextField)
        self.setText("",self.view.activeTextField)

        
        
        
        
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