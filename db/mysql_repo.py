import mysql.connector
from db.repository import *


class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'strongpassword',
            'host': 'localhost',  # to run LOCALLY, this should be localhost
            'port': 32000,  # to run LOCALLY, this should be 32000
            'database': 'lexicon'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def load_lexicon(self) -> List[Lexentry]:
        sql = "SELECT * FROM lexentries"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return [Lexentry(*entry) for entry in result]
