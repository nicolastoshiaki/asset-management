from infra.configs.database import Base
from sqlalchemy import Column, String, Integer 

class Am_prod_type(Base):
    __tablename__ = 'AM_PROD_TYPE'

    des_type = Column(String, nullable=False)
    des_type_short = Column(String, nullable=False)
    id_type = Column(Integer, primary_key=True) #identity, no need to specify in the insert statement

    def __repr__(self):
        return f'AM_PROD_TYPE [id_type = {self.id_type}, des_type = {self.des_type}, des_type_short = {self.des_type_short}]'    