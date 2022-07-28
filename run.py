####MVC###
##https://www.giacomodebidda.com/posts/mvc-pattern-in-python-introduction-and-basicmodel/
##https://www.pythontutorial.net/tkinter/tkinter-mvc/   
##

from controller.LoginCtl import LoginCtl
from model.persistance.DB_Dic import DB_Dict
from model.persistance.DB_Mysql import DB_Mysql
from model.persistance.DB_SqlLite import DB_Sqlite
from model.persistance.config import *
from view.Categories import Categories
from view.Checkin import Checkin
from controller.CheckCtl import CheckCtl
from view.GlobalView import GlobalView
from view.Login import Login
from view.Reservations import Reservations
from view.Rooms import Rooms
from view.Guests import Guests


##TESTING#

#view = Reservations()

#cx = DB_Dict()
# cx = DB_Sqlite("hotelApp.db")
cx = DB_Mysql(HOST, USERNAME, PASSWORD, DATABASE)
view = Login()
controller = LoginCtl(view, cx)
# view = Checkin()
#controller = CheckCtl(view, cx)

#Close the DB connection on "window close"
# def on_closing():
#     print("closing the window")
#     cx.close()
#     view.mainWindow.destroy()
# if not isinstance(cx, DB_Dict):
#     view.mainWindow.protocol("WM_DELETE_WINDOW", on_closing)

view.mainloop()
