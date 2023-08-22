from dataclasses import dataclass, field
from infra.repository import AmInvestPortRepository, AmProductsRepository, AmProdTypeRepository

repo_invest_port = AmInvestPortRepository()
repo_product = AmProductsRepository()
repo_prod_type = AmProdTypeRepository()

@dataclass
class User:
    id: int
    username: str
    login: str
    password: str = field(repr=False)
    portfolio = {}

    def is_password_correct(self, user_password):
        if user_password == self.password:
            return True
        return False

    def insert_asset(self, new_asset, quantity):
        query_get_product_id = repo_product.select_by_name(new_asset)
        for item in query_get_product_id:
            user_new_asset_id = item.id_product
        repo_invest_port.insert(self.id, user_new_asset_id, quantity)
        return True

    def remove_asset(self, asset_to_delete):   
        query_get_product_id = repo_product.select_by_name(asset_to_delete)
        previous_quantity = self.portfolio.get(asset_to_delete)[1]    
        for item in query_get_product_id:
            user_asset_to_delete_id = item.id_product
        repo_invest_port.delete(self.id, user_asset_to_delete_id)
        return previous_quantity


    def update_asset_quantity_in_portfolio(self, asset_to_update, new_quantity):
        query_get_product_id = repo_product.select_by_name(asset_to_update)
        previous_quantity = self.portfolio.get(asset_to_update)[1]    
        for item in query_get_product_id:
            user_asset_to_update_id = item.id_product
        repo_invest_port.update(self.id, user_asset_to_update_id, new_quantity)
        return previous_quantity, new_quantity


    def get_porfolio(self):
        query_portfolio = repo_invest_port.select(self.id)
        for item in query_portfolio:
            database_id_product = item.id_product
            database_quantity = item.product_quantity
            query_products = repo_product.select_by_id(database_id_product)
            for item in query_products:
                database_name = item.product_name
                database_id_type = item.id_type
            query_type = repo_prod_type.select(database_id_type)
            for item in query_type:
                database_shot_type = item.des_type
            key = database_name        
            values = [database_shot_type, database_quantity, 0.0]
            self.portfolio[key] = values
        return self.portfolio

    # def create_portfolio(self, con):
    #    new_asset = input(
    #        'Qual ativo deseja incluir (favor colocar o código, exemplo: PETR4)?')
    #    query_check_asset = f"SELECT ID_PRODUCT, ID_TYPE FROM CT_PRODUCTS WHERE PRODUCT_NAME = '{new_asset}'"
    #    result_query_check_asset = con.execute(query_check_asset)
    #    for item in result_query_check_asset:
    #        id_product, id_type = item
    #    if not id_product:
    #        query_product_dont_exists = 'SELECT ID_TYPE, DES_TYPEFROM CT_PROD_TYPE'
    #        result = con.execute(query_product_dont_exists)
    #        for item in result:
    #            id_type, type = item
    #            print(id_type, type)
    #        new_type = input(
    #            'Qual o tipo de ativo inserido, digite o numero correspondente:')
    #    else:
    #        new_type = id_type
    #    new_quantity = input('Qual a quantidade que deseja inserir?')
    #    print('Criando novo portfolio...')
    #    query_insert_new_portfolio = f'INSERT INTO CT_PORTFOLIO VALUES ({self.id},{},{new_quantity})'
