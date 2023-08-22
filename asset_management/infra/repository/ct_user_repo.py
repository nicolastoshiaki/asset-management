from infra.configs import DBConnectionHandler
from infra.entities import Am_user
from datetime import datetime

class AmUserRepository:
    def select(self, login):
        with DBConnectionHandler() as db:
            data = db.session.query(Am_user).where(Am_user.login_user == f'{login}').all()
            return data
        
    def insert(self, login, password, username):
        with DBConnectionHandler() as db:
            data_insert = Am_user(login_user=login, password_user=password, username=username, dt_last_log=datetime.now())
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, login):
        with DBConnectionHandler() as db:
            db.session.query(Am_user).filter(Am_user.login_user == f'{login}').delete()
            db.session.commit()

    def update(self, login, password, username):
        with DBConnectionHandler() as db:
            db.session.query(Am_user).filter(Am_user.login_user == f'{login}').update({Am_user.username: f'{username}', Am_user.password_user: f'{password}'})
            db.session.commit()