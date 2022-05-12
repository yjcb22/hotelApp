from model.guestDTO import GuestDTO
from model.persistance.DB_Dic import DB_Dict
from model.persistance.DB_Mysql import DB_Mysql
from model.persistance.DB_SqlLite import DB_Sqlite

class GuestDAO:
    def __init__(self, db) -> None:
        if isinstance(db, DB_Dict):
            self.db = db.database
            self.counter = 0
        elif isinstance(db, DB_Sqlite):
            #SQL STATEMENTS
            self.SQL_INSERT = "INSERT INTO guest (name, lastname, room) VALUES(?, ?, ?)"
            self.db = db
        elif isinstance(db, DB_Mysql): 
            self.SQL_INSERT = "INSERT INTO guest (name, lastname, room) VALUES(%s, %s, %s)"
            self.db = db
        
        
        #SQL STATEMENTS        
        self.SQL_SELECT = "SELECT * FROM guest"
        self.SQL_SELECT_ONE = "SELECT id, name, lastname, room FROM guest WHERE id=?"


##DICTIONARY##
    def insert(self, guest: GuestDTO) -> None:        
        self.db[self.counter] = {'id': self.counter, 
        'name': guest.name,
        'lastname': guest.lastname,
        'room': guest.room
        }
        self.counter += 1
        
    
    
    def selectAll(self) -> list[GuestDTO]:
        guests = []
        for key in self.db:
            guestDto = GuestDTO(self.db[key]['name'],self.db[key]['lastname'],self.db[key]['room'],self.db[key]['id'])
            guests.append(guestDto)
            #print(guestDto.toString())
        return guests
    
   


    def selectById(self, id: int) -> GuestDTO:        
        guestDto = GuestDTO(self.db[id]['name'],self.db[id]['lastname'],self.db[id]['room'])
        return guestDto


    ##DELETE

    ##UPDATE

#####################SQL##########################

    def insertSQL(self, guest: GuestDTO) -> None:  
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_INSERT, (guest.name, guest.lastname, guest.room))
        self.db.cx.commit()
        #self.db.cx.close()        

    def selectAllSQL(self) -> list[GuestDTO]:
        guests = []
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_SELECT)
        result = cur.fetchall()
        for i in result:
            guestDto = GuestDTO(i[1], i[2], i[3], i[0])
            guests.append(guestDto)  
        return guests
    
    
##DELETE

##UPDATE