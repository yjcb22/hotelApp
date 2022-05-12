####MVC###
##https://www.giacomodebidda.com/posts/mvc-pattern-in-python-introduction-and-basicmodel/
##https://www.pythontutorial.net/tkinter/tkinter-mvc/   
##

from model.persistance.DB_Dic import DB_Dict
from model.persistance.DB_Mysql import DB_Mysql
from model.persistance.DB_SqlLite import DB_Sqlite
from model.persistance.config import *
from view.Checkin import Checkin
from controller.CheckCtl import CheckCtl



#cx = DB_Dict()
cx = DB_Sqlite("hotelApp.db")
#cx = DB_Mysql(HOST, USERNAME, PASSWORD, DATABASE)
view = Checkin()
controller = CheckCtl(view, cx)

#Close the DB connection on "window close"
def on_closing():
    print("closing the window")
    cx.close()
    view.mainWindow.destroy()
if not isinstance(cx, DB_Dict):
    view.mainWindow.protocol("WM_DELETE_WINDOW", on_closing)

view.mainWindow.mainloop()

