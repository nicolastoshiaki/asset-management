from infra.configs.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Am_products(Base):
    __tablename__ = 'AM_PRODUCTS'

    product_name = Column(String, nullable=False)
    id_type = Column(Integer, ForeignKey("AM_PROD_TYPE.id_type"))
    id_product = Column(Integer, primary_key=True) #identity, no need to specify in the insert statement

    def __repr__(self):
        return f'AM_PRODUCTS [id_product = {self.id_product}, product_name = {self.product_name}, id_type = {self.id_type}]'