from infra.configs.database import Base
from sqlalchemy import Column, String, Integer 

class Am_user(Base):
    __tablename__ = 'AM_USER'

    login_user = Column(String, nullable=False)
    password_user = Column(String, nullable=False)
    username = Column(String, nullable=False)
    dt_last_log = Column(String, nullable=False)
    id_user = Column(Integer, primary_key=True) #identity, no need to specify in the insert statement

    def __repr__(self):
        return f'AM_USER [id_user = {self.id_user}, login_user = {self.login_user}, username = {self.username}]'