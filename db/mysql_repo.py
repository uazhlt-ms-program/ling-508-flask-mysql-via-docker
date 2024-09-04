import mysql.connector
from db.repository import *
from model.lex import Lexentry, POS
import os


class MysqlRepository(Repository):

    def __init__(self):
        """
        Put database configuration options HERE as a way of ENCAPSULATION:

        The rest of the code doesn't need to care about HOW the database is connected,
        just THAT it is connected once it creates a repository.
        """
        super().__init__()
        if os.environ.get('APP_ENV') == 'docker':  # detect when the app is containerized
            config = {
                'user': 'root',
                'password': 'strongpassword',
                'host': 'db',         #  used when the app is containerized
                'port': 3306,
                'database': 'lexicon'
            }
        else:
            config = {
                'user': 'root',
                'password': 'strongpassword',
                'host': 'localhost',  #  used for testing when the app is not yet containerized
                'port': 32000,
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

    def save_item(self, lex_item: Lexentry) -> bool:
        if not POS.__contains__(lex_item.pos):
            raise ValueError('invalid POS of item to be saved')
        sql = ("INSERT INTO lexentries "
               "(written_form, pronunciation, pos, definition) "
               f"VALUES ("
               f"'{lex_item.written_form}', "
               f"N'{lex_item.pronunciation}', "
               f"'{lex_item.pos}', "
               f"'{lex_item.definition}')"
               )
        self.cursor.execute(sql)
        return True
