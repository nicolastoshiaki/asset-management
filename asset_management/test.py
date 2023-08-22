from infra.repository.ct_invest_port_repo import CtInvestPortRepository
from infra.repository.ct_prod_type_repo import CtProdTypeRepository
from infra.repository.ct_products_repo import CtProductsRepository
from infra.repository.ct_user_repo import CtUserRepository

repo_user = CtUserRepository()

login = input('Insert login ')

data = repo_user.select(login)
for item in data:
    print(item.id)


