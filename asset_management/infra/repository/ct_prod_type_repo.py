from infra.configs import DBConnectionHandler
from infra.entities import Am_prod_type

class AmProdTypeRepository:
    def select_short_types(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Am_prod_type.id_type, Am_prod_type.des_type_short).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Am_prod_type).where(Am_prod_type.id_type == id).all()
            return data
        
    def insert(self, des_type_short, des_type):
        with DBConnectionHandler() as db:
            data_insert = Am_prod_type(des_type_short=des_type_short, des_type=des_type)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, des_type_short):
        with DBConnectionHandler() as db:
            db.session.query(Am_prod_type).where(Am_prod_type.des_type_short == f'{des_type_short}').delete()
            db.session.commit()

    def update(self, des_type_short, des_type):
        with DBConnectionHandler() as db:
            db.session.query(Am_prod_type).where(Am_prod_type.des_type_short == f'{des_type_short}').update({Am_prod_type.des_type: des_type})
            db.session.commit()