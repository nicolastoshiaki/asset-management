from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-1RI92GB\SQLEXPRESS;DATABASE=dbo_carteira;trusted_connection=yes"
        self.__connection_url = URL.create(
    "mssql+pyodbc", query={"odbc_connect": self.__connection_string})
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_url)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()