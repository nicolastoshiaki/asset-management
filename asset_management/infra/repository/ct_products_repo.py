from infra.configs import DBConnectionHandler
from infra.entities import Am_products

class AmProductsRepository:
    def select_by_name(self, product_name):
        with DBConnectionHandler() as db:
            data = db.session.query(Am_products).where(Am_products.product_name == f'{product_name}').all()
            return data
     
    def select_by_id(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Am_products).where(Am_products.id_product == id).all()
            return data

    def insert(self, product_name, id_type):
        with DBConnectionHandler() as db:
            data_insert = Am_products(product_name=product_name, id_type=id_type)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, product_name):
        with DBConnectionHandler() as db:
            db.session.query(Am_products).where(Am_products.product_name == f'{product_name}').delete()
            db.session.commit()

    def update(self, product_name, id_type):
        with DBConnectionHandler() as db:
            db.session.query(Am_products).where(Am_products.product_name == f'{product_name}').update({Am_products.id_type: id_type})
            db.session.commit()