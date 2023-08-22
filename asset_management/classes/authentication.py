from .exceptions import UserNotAuthenticatedError
from infra.repository.ct_user_repo import AmUserRepository
from .user import User

user_repo = AmUserRepository()

class Authenticator:
    def user_authentication(self, login, user_password):
        query = user_repo.select(login)
        for item in query:            
            database_id = item.id_user
            database_username = item.username
            database_login = item.login_user
            database_password = item.password_user
        if database_password == user_password:
            return User(database_id, database_username, database_login, database_password)
        raise UserNotAuthenticatedError       

    def create_new_user(self, login, password, username):
        user_repo.insert(login, password, username)
        return True

    def check_existing_user(self, login):
        query_result = user_repo.select(login)
        if query_result:
            return False
        return True

