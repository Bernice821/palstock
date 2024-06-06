from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, BigInteger, Identity, DateTime
from init import db 
from datetime import datetime

class New(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    src: Mapped[str] = mapped_column(String(50))
    time_stamp: Mapped[datetime] = mapped_column(default=lambda: datetime.now())
    url: Mapped[str] = mapped_column(String(5000))
    pic_url: Mapped[str] = mapped_column(String(5000))

    def __repr__(self):
        return f'<{self.title}>'
    
    def obj_to_dict(self):
        return{
            'Title' : self.title,
            'Url'   : self.url,
            'ImgUrl': self.pic_url,
            'Time'  : self.time_stamp
        }


class Stock(db.Model):
    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    time_stamp: Mapped[datetime] = mapped_column(default=lambda: datetime.now(), primary_key=True)
    volume: Mapped[int] = mapped_column(default=0)
    trans_amt: Mapped[int] = mapped_column(BigInteger)
    open: Mapped[int] = mapped_column(onupdate=0)
    highest: Mapped[int] = mapped_column(default=0)
    lowest: Mapped[int] = mapped_column(default=0)
    close: Mapped[int] = mapped_column(default=0)
    change: Mapped[int] = mapped_column(default=0)
    trans_num: Mapped[int] = mapped_column(default=0)

    def info_obj_to_dict(self):
        return{
                'time' : self.time_stamp,
                'Open' : self.open,
                'High' : self.highest,
                'Low'  : self.lowest,
                'Close' : self.close
        }
    def index_obj_to_dict(self):
        return{
            'StockName': self.name,
            'StockChart': [
                self.open,
                self.close,
                self.highest,
                self.lowest
            ]
        }
    
    
class Figure(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    volume: Mapped[int] = mapped_column()
    open: Mapped[int] = mapped_column()
    highest: Mapped[int] = mapped_column()
    lowest: Mapped[int] = mapped_column()
    close: Mapped[int] = mapped_column()
    

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(50))

    def __repr__(self):
        return f'<User {self.username}>'
