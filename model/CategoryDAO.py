from model.CategoryDTO import CategoryDTO


class CategoryDAO:
    def __init__(self, db) -> None:
        self.db = db      
        
        #SQL STATEMENTS        
        self.SQL_SELECT_CATEGORY = "SELECT id_category, name, description, active from Categories"
        self.SQL_INSERT_CATEGORY = "INSERT INTO Categories (name, description, active) VALUES (%s, %s, %s)"
        self.SQL_DELETE_SOFT = "UPDATE Categories SET active=false WHERE id_category=%s"
        self.SQL_UPDATE = "UPDATE Categories SET name=%s, description=%s, active=%s WHERE id_category=%s"

#####################SQL##########################


###SELECT####
    def selectAllCategories(self) -> list[CategoryDTO]:
        categories = []
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_SELECT_CATEGORY)
        result = cur.fetchall()
        for i in result:
            categories.append(CategoryDTO(i[1],i[2],i[0],i[3]))
        return categories


   
##INSERT###
    def insertCategory(self, category: CategoryDTO) -> None:
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_INSERT_CATEGORY, (category.name, category.description, category.active))
        self.db.cx.commit()   
    
##DELETE
    def deleteCategory(self, id: int) -> None:
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_DELETE_SOFT, (id,))
        self.db.cx.commit()

##UPDATE
    def updateCategory(self, category: CategoryDTO) -> None:
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_UPDATE, (category.name,category.description,category.active,category.id))
        self.db.cx.commit()