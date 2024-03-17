from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///monitor.db')

Base = declarative_base()

class MyData(Base):
    __tablename__ = 'data'
    engine = create_engine('sqlite:///monitor.db')

    id = Column(Integer, primary_key=True)
    product = Column(String)
    price = Column(String)
    unit = Column(String)
    remainder = Column(String)

    def insert_data(self,data_dict):
        new_data = MyData(product=data_dict['product'], price=data_dict['price'], unit=data_dict['unit'],
                          remainder=data_dict['remainder'])
        session.add(new_data)
        session.commit()


Base.metadata.create_all(engine)


