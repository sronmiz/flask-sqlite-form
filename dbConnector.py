import db_config
import sqlite3

class dbConnector():
    def __init__(self):
        self.db_path = db_config.DB_PATH
        self.table_name = db_config.TABLE_NAME
        self.create_table = db_config.CREATE_TABLE

    def build_table(self):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute(self.create_table)
            conn.commit()
    
    def add_values(self,values):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute(f'''INSERT INTO {self.table_name} VALUES {values}''')
            conn.commit()
    