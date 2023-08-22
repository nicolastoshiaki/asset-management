from infra.configs.database import Base
from sqlalchemy import Column, String, Integer , ForeignKey

class Am_invest_port(Base):
    __tablename__ = 'AM_INVEST_PORT'

    id_user = Column(Integer, ForeignKey("AM_USER.id_user")) 
    id_product = Column(Integer, ForeignKey("AM_PRODUCTS.id_product"))
    product_quantity = Column(Integer, nullable=False)
    id_invest_port = Column(Integer, primary_key=True) #identity, no need to specify in the insert statement

    def __repr__(self):
        return f'AM_INVEST_PORT [id_user = {self.id_user}, id_product = {self.id_product}, product_quantity = {self.product_quantity}, id_invest_port = {self.id_invest_port}]'    