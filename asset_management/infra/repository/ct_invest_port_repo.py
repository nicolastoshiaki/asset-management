from infra.configs import DBConnectionHandler
from infra.entities import Am_invest_port

class AmInvestPortRepository:
    def select(self, id_user):
        with DBConnectionHandler() as db:
            data = db.session.query(Am_invest_port).where(Am_invest_port.id_user==id_user).all()
            return data
        
    def insert(self, id_user, id_product, quantity):
        with DBConnectionHandler() as db:
            data_insert = Am_invest_port(id_user=id_user, id_product=id_product, product_quantity=quantity)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, id_user, id_product):
        with DBConnectionHandler() as db:
            db.session.query(Am_invest_port).where(Am_invest_port.id_product==id_product, Am_invest_port.id_user==id_user).delete()
            db.session.commit()

    def update(self, id_user, id_product, quantity):
        with DBConnectionHandler() as db:
            db.session.query(Am_invest_port).where(Am_invest_port.id_product==id_product, Am_invest_port.id_user==id_user).update({Am_invest_port.product_quantity: quantity})
            db.session.commit()