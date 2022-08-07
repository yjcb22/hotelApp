from model.CategoryDTO import CategoryDTO
from model.GlobalviewDTO import GlobalviewDTO
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
        self.SQL_SELECT = "SELECT * FROM Guests"
        self.SQL_SELECT_ONE = "SELECT id, name, lastname, room FROM Guests WHERE id=?"
        self.SQL_SELECT_PASSWORD = "SELECT id_guest, name, lastname, age, email, password FROM Guests WHERE email=%s AND password=%s"
        self.SQL_SELECT_GLOBALVIEW = "SELECT Reservations.id_reservation, Guests.name, Guests.lastname, Guests.age, Guests.email, Reservations.id_room FROM hotel.Guests INNER JOIN hotel.Reservations ON hotel.Guests.id_guest = hotel.Reservations.id_guest"
        self.SQL_SELECT_CATEGORY = "SELECT id_category, name, description, active from Categories"

        self.SQL_INSERT_CATEGORY = "INSERT INTO Categories (name, description) VALUES (%s, %s)"
        self.SQL_DELETE_SOFT = "UPDATE Categories SET active=false WHERE id_category=%s"




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

#############
###SELECT####
############
    def selectAllSQL(self) -> list[GuestDTO]:
        guests = []
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_SELECT)
        result = cur.fetchall()
        for i in result:
            guestDto = GuestDTO(i[1], i[2], i[3], i[0])
            guests.append(guestDto)  
        return guests
    
    def validateCredentials(self, guest: GuestDTO) -> list[GuestDTO]:
        guests = []
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_SELECT_PASSWORD,(guest.email, guest.password))
        result = cur.fetchall()
        #print("result ",result)
        for i in result:
            guestDto = GuestDTO(i[1], i[2], i[3], i[4], i[5], i[0])
            guests.append(guestDto)              
        return guests
    
    def selectGuestReserv(self) -> list[GlobalviewDTO]:
        guestReserve = []
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_SELECT_GLOBALVIEW)
        result = cur.fetchall()
        for i in result:
            guestReserve.append(GlobalviewDTO(i[1],i[2],i[4],i[0],i[3],i[5]))
        return guestReserve



###############    
##INSERT###
##############

    def insertSQL(self, guest: GuestDTO) -> None:  
        cur = self.db.cx.cursor()
        cur.execute(self.SQL_INSERT, (guest.name, guest.lastname, guest.room))
        self.db.cx.commit()
        #self.db.cx.close()   

    
##DELETE


##UPDATE